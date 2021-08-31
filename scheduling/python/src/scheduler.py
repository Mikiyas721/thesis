import random
from time import sleep

from src.assigned_state import AssignedState
from src.assigned_state import maximum_assignable_time
from src.density_state import DensityState

import src.hardware_manipulator as hw


def when_time_is_up(assigned_state: AssignedState, density_state: DensityState):
    print(density_state.car_density_string())
    print(assigned_state.state_string())

    on_led_s: [int] = assigned_state.get_on_led_s()
    crossed_cars: int = assigned_state.allocated_time // 2

    if density_state.car_density[on_led_s[0]] > crossed_cars:
        density_state.car_density[on_led_s[0]] -= crossed_cars
    else:
        density_state.car_density[on_led_s[0]] = 0

    if density_state.car_density[on_led_s[1]] > crossed_cars:
        density_state.car_density[on_led_s[1]] -= crossed_cars
    else:
        density_state.car_density[on_led_s[1]] = 0

    density_state = get_random_density(density_state.car_density, assigned_state.allocated_time)


def get_random_density(density_state: DensityState, assigned_state: AssignedState) -> DensityState:
    on_led_s: [int] = assigned_state.get_on_led_s()
    crossed_cars: int = assigned_state.allocated_time[0] // 2  # TODO check
    if density_state.car_density[0][on_led_s[0]] > crossed_cars:
        density_state.car_density[0][on_led_s[0]] -= crossed_cars
    else:
        density_state.car_density[0][on_led_s[0]] = 0
    if density_state.car_density[0][on_led_s[1]] > crossed_cars:
        density_state.car_density[0][on_led_s[1]] -= crossed_cars
    else:
        density_state.car_density[0][on_led_s[1]] = 0

    random_density_state: [int] = []
    for i in range(0, 8):
        if assigned_state.allocated_time[0] // 4 == 0:
            to_be_added = 0
        else:
            to_be_added = random.random() * assigned_state.allocated_time[0] // 3
        if to_be_added > 4:
            to_be_subtracted = random.random() * to_be_added // 2
        else:
            to_be_subtracted = 0
        random_density_state.append(density_state.car_density[0][i] + to_be_added - to_be_subtracted)
    return DensityState(car_density=random_density_state)


def calculate(density_state: DensityState, previous_assigned_state: AssignedState) -> AssignedState:
    if len(previous_assigned_state.critically_waiting[0]) > 0:
        raise Exception("Lane is waiting critically")
        # TODO handle critically waiting lanes
    waited_long_lanes: list = previous_assigned_state.waited_long_lanes()
    if len(waited_long_lanes) > 2:
        raise Exception("More than two lanes waited long")
        # TODO handle appropriately
    if 0 < len(waited_long_lanes) < 3:
        if len(waited_long_lanes) == 2:
            if can_pass_together(waited_long_lanes[0], waited_long_lanes[1]):
                lane1_density: int = density_state.car_density[0][waited_long_lanes[0]]
                lane2_density: int = density_state.car_density[0][waited_long_lanes[1]]
                if lane1_density == 0 and lane2_density == 0:
                    return calculate(
                        density_state,
                        AssignedState(
                            allocated_time=0,
                            waiting_time=get_updated_waiting_time(
                                waited_long_lanes[0],
                                waited_long_lanes[1],
                                0,
                                previous_assigned_state.waiting_time,
                                density_state.car_density),
                            led_state=previous_assigned_state.led_state,
                        ))
                if lane1_density == 0:
                    return calculate(
                        density_state,
                        AssignedState(
                            allocated_time=0,
                            waiting_time=get_updated_waiting_time_when_1_empty_lane(
                                waited_long_lanes[0],
                                0,
                                previous_assigned_state.waiting_time,
                                density_state.car_density),
                            led_state=previous_assigned_state.led_state,
                        ))
                if lane2_density == 0:
                    return calculate(
                        density_state,
                        AssignedState(
                            allocated_time=0,
                            waiting_time=get_updated_waiting_time_when_1_empty_lane(
                                waited_long_lanes[1],
                                0,
                                previous_assigned_state.waiting_time,
                                density_state.car_density),
                            led_state=previous_assigned_state.led_state,
                        ))
                if (density_state.prime_capacities[0][get_accepting_road_index(waited_long_lanes[0])] > 10 or
                        density_state.prime_capacities[
                            get_accepting_road_index(waited_long_lanes[1])] > 10):
                    return evaluate_for_two_lanes(waited_long_lanes[0], waited_long_lanes[1],
                                                  previous_assigned_state, density_state)
                    raise Exception("waited long but no accepting road")
                    # TODO handle appropriately

            else:
                chosen_lane_index: int
                if previous_assigned_state.waiting_time[0][waited_long_lanes[0]] == waited_long_lanes[1]:
                    chosen_lane_index = waited_long_lanes[0] \
                        if density_state.car_density[waited_long_lanes[0]] > \
                           density_state.car_density[waited_long_lanes[1]] else \
                        waited_long_lanes[1]

                else:
                    chosen_lane_index = waited_long_lanes[0] \
                        if previous_assigned_state.waiting_time[0][waited_long_lanes[0]] > \
                           previous_assigned_state.waiting_time[0][waited_long_lanes[1]] else \
                        waited_long_lanes[1]

                chosen_lane_pair_index: int = get_best_pair_for_waited_long(
                    chosen_lane_index, previous_assigned_state, density_state)
                return evaluate_for_two_lanes(chosen_lane_index, chosen_lane_pair_index,
                                              previous_assigned_state, density_state)
        return evaluate_for_two_lanes(
            waited_long_lanes[0],
            get_best_pair_for_waited_long(
                waited_long_lanes[0],
                previous_assigned_state,
                density_state,
            ),
            previous_assigned_state,
            density_state,
        )

    limit_reaching_lanes: list = previous_assigned_state.get_lanes_reaching_limit()
    if len(limit_reaching_lanes) > 2:
        best_limit_reaching_pair: list = density_state.get_best_limit_reaching_pair(limit_reaching_lanes)
        return evaluate_for_two_lanes(best_limit_reaching_pair[0],
                                      best_limit_reaching_pair[1], previous_assigned_state, density_state)

    dense_lanes: list = density_state.get_dense_lane_pair()
    return evaluate_for_two_lanes(
        dense_lanes[0],
        dense_lanes[1],
        previous_assigned_state,
        density_state,
    )


def evaluate_for_two_lanes(lane1_index: int, lane2_index: int, previous_assigned_state: AssignedState,
                           density_state: DensityState) -> AssignedState:
    lane1_density: int = density_state.car_density[0][lane1_index]
    lane2_density: int = density_state.car_density[0][lane2_index]
    if lane1_density >= 20 or lane2_density >= 20:
        closest_waiting_time_to_max: int = previous_assigned_state.closest_waiting_time_to_max(lane1_index,
                                                                                               lane2_index)
        if closest_waiting_time_to_max < 40:
            return AssignedState(
                allocated_time=closest_waiting_time_to_max - 2,
                waiting_time=get_updated_waiting_time(
                    lane1_index,
                    lane2_index,
                    closest_waiting_time_to_max - 2,
                    previous_assigned_state.waiting_time,
                    density_state.car_density),
                led_state=get_updated_led_state(lane1_index, lane2_index),
            )
        return AssignedState(
            allocated_time=maximum_assignable_time,
            waiting_time=get_updated_waiting_time(
                lane1_index,
                lane2_index,
                maximum_assignable_time,
                previous_assigned_state.waiting_time,
                density_state.car_density),
            led_state=get_updated_led_state(lane1_index, lane2_index),
        )
    time_to_allocate: int
    if lane1_density > lane2_density:
        time_to_allocate = lane1_density * 2
    else:
        time_to_allocate = lane2_density * 2
    return AssignedState(
        allocated_time=time_to_allocate,
        waiting_time=get_updated_waiting_time(
            lane1_index,
            lane2_index,
            time_to_allocate,
            previous_assigned_state.waiting_time,
            density_state.car_density,
        ),
        led_state=get_updated_led_state(lane1_index, lane2_index),
    )


def get_updated_waiting_time(led_1_index: int, led_2_index: int, time_to_allocate: int,
                             previous_waiting_time: list, previous_car_density: list) -> list:
    waiting_time: [int] = [0] * 8
    for i in range(0, 8):
        if not (i == led_1_index or i == led_2_index) and previous_car_density[0][i] > 0:
            waiting_time[i] = previous_waiting_time[0][i] + time_to_allocate
    return waiting_time


def get_updated_waiting_time_when_1_empty_lane(led_index: int, time_to_allocate: int,
                                               previous_waiting_time: list,
                                               previous_car_density: list, ) -> list:
    waiting_time: [int] = [0] * 8
    for i in range(0, 8):
        if i != led_index and previous_car_density[i] > 0:
            waiting_time[i] = previous_waiting_time[i] + time_to_allocate
    return waiting_time


def get_updated_led_state(led_1_index: int, led_2_index: int) -> list:
    led_states: [bool] = [False] * 8
    led_states[led_1_index] = True
    led_states[led_2_index] = True
    return led_states


def get_accepting_road_index(lane_index: int):
    if lane_index % 2 == 1:
        return (lane_index - 1) // 2
    return lane_index // 2


def can_pass_together(x: int, y: int):
    if (x < y) and (y == x + 4 or y == x + 1 or y == (x + 7) % 8):
        return True
    if (x > y) and (y == (x + 4) % 8 or y == x - 1 or y == (x - 7) % 8):
        return True
    return False


def get_best_pair_for_waited_long \
                (x: int, assigned_state: AssignedState, density_state: DensityState) -> int:
    best_pair: int = 0
    # Might cause problem, used to remove null value error
    max_density: int = 0
    max_waiting_time: int = 0
    pairs: [int] = get_lane_pairs(x)
    for pair in pairs:
        if (assigned_state.waiting_time[0][pair] > max_waiting_time and
                density_state.car_density[0][pair] > 0):
            max_waiting_time = assigned_state.waiting_time[0][pair]
            max_density = density_state.car_density[0][pair]
            best_pair = pair
        elif (assigned_state.waiting_time[0][pair] == max_waiting_time and
              density_state.car_density[0][pair] > max_density):
            max_waiting_time = assigned_state.waiting_time[0][pair]
            max_density = density_state.car_density[0][pair]
            best_pair = pair
    return best_pair


def get_lane_pairs(x: int) -> list:
    possible_pairs: [int] = []
    if x % 2 == 0:
        possible_pairs.append(x + 1)
        possible_pairs.append((x - 1) % 8)
    else:
        possible_pairs.append(x - 1)
        possible_pairs.append((x + 1) % 8)
    if x <= 3:
        possible_pairs.append(x + 4)
    else:
        possible_pairs.append(x - 4)
    return possible_pairs


def re_evaluate_time(waiting_time: list) -> list:
    print("Re-evaluating")
    for i in range(0, 8):
        if waiting_time[i] > 40:
            waiting_time[i] -= 40
    return waiting_time


def main():
    # Multiple Randomized scenarios
    density_state = DensityState(car_density=[5, 25, 19, 18, 10, 12, 20, 15])
    assigned_state: AssignedState = calculate(density_state, AssignedState())

    while True:
        # print states
        print(density_state.car_density_string())
        print(assigned_state.state_string())

        hw.turn_greens_on(assigned_state.get_on_led_s())
        sleep(assigned_state.allocated_time)

        hw.turn_yellows_on(assigned_state.get_on_led_s())
        sleep(3)

        density_state = \
            get_random_density(density_state, assigned_state)
        new_state = calculate(density_state, assigned_state)
        assigned_state = new_state


main()
