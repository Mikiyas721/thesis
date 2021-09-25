import random

from src.scheduler.assigned_state import AssignedState
from src.scheduler.assigned_state import maximum_assignable_time
from src.scheduler.density_state import DensityState


class Scheduler:

    def __init__(self, assigned_state: AssignedState, density_state: DensityState):
        self.assigned_state = assigned_state
        self.density_state = density_state
        pass

    def calculate(self) -> AssignedState:
        if len(self.assigned_state.critically_waiting) > 0:
            raise Exception("Lane is waiting critically")
            # TODO handle critically waiting lanes
        waited_long_lanes: list = self.assigned_state.waited_long_lanes()
        if len(waited_long_lanes) > 2:
            raise Exception("More than two lanes waited long")
            # TODO handle appropriately
        if 0 < len(waited_long_lanes) < 3:
            if len(waited_long_lanes) == 2:
                if self.can_pass_together(waited_long_lanes[0], waited_long_lanes[1]):
                    lane1_density: int = self.density_state.car_density[waited_long_lanes[0]]
                    lane2_density: int = self.density_state.car_density[waited_long_lanes[1]]
                    if lane1_density == 0 or lane2_density == 0:
                        waiting_time = self.get_updated_waiting_time(
                            waited_long_lanes[0],
                            waited_long_lanes[
                                1]) if lane1_density == 0 and lane2_density == 0 \
                            else self.get_updated_waiting_time_when_1_empty_lane(
                            waited_long_lanes[0] if lane1_density == 0 else waited_long_lanes[1])

                        self.__setattr__('assigned_state', AssignedState(
                            allocated_time=0,
                            waiting_time=waiting_time,
                            led_state=self.assigned_state.led_state,
                        ))

                        return self.calculate()
                    if (self.density_state.prime_capacities[self.get_accepting_road_index(waited_long_lanes[0])] > 10 or
                            self.density_state.prime_capacities[
                                self.get_accepting_road_index(waited_long_lanes[1])] > 10):
                        return self.evaluate_for_two_lanes(waited_long_lanes[0],
                                                           waited_long_lanes[1])
                    raise Exception("waited long but no accepting road")
                    # TODO handle appropriately

                else:
                    chosen_lane_index: int
                    if self.assigned_state.waiting_time[waited_long_lanes[0]] == waited_long_lanes[1]:
                        chosen_lane_index = waited_long_lanes[0] \
                            if self.density_state.car_density[waited_long_lanes[0]] > \
                            self.density_state.car_density[waited_long_lanes[1]] else \
                            waited_long_lanes[1]

                    else:
                        chosen_lane_index = waited_long_lanes[0] \
                            if self.assigned_state.waiting_time[waited_long_lanes[0]] > \
                            self.assigned_state.waiting_time[waited_long_lanes[1]] else \
                            waited_long_lanes[1]

                    chosen_lane_pair_index: int = self.get_best_pair_for_waited_long(chosen_lane_index)
                    return self.evaluate_for_two_lanes(chosen_lane_index, chosen_lane_pair_index)
            return self.evaluate_for_two_lanes(
                waited_long_lanes[0],
                self.get_best_pair_for_waited_long(
                    waited_long_lanes[0]
                )
            )

        limit_reaching_lanes: list = self.assigned_state.get_lanes_reaching_limit()
        if len(limit_reaching_lanes) > 2:
            best_limit_reaching_pair: list = self.density_state.get_best_limit_reaching_pair(limit_reaching_lanes)
            return self.evaluate_for_two_lanes(best_limit_reaching_pair[0],
                                               best_limit_reaching_pair[1])

        dense_lanes: list = self.density_state.get_dense_lane_pair()
        return self.evaluate_for_two_lanes(
            dense_lanes[0],
            dense_lanes[1])

    def evaluate_for_two_lanes(self, lane1_index: int, lane2_index: int) -> AssignedState:
        lane1_density: int = self.density_state.car_density[lane1_index]
        lane2_density: int = self.density_state.car_density[lane2_index]

        closest_waiting_time_to_max: int = self.assigned_state.closest_waiting_time_to_max(lane1_index, lane2_index)
        density_based_time: int = maximum_assignable_time if (lane1_density >= 20 or lane2_density >= 20) else (
            lane1_density * 2 if lane1_density > lane2_density else lane2_density * 2)

        allocated_time: int = (density_based_time if density_based_time < closest_waiting_time_to_max
                               else closest_waiting_time_to_max) \
            if closest_waiting_time_to_max < 40 else density_based_time

        return AssignedState(
            allocated_time=allocated_time,
            waiting_time=self.get_updated_waiting_time(
                lane1_index,
                lane2_index),
            led_state=self.get_updated_led_state(lane1_index, lane2_index),
        )

    def get_random_density(self) -> DensityState:
        on_led_s: [int] = self.assigned_state.get_on_led_s()
        crossed_cars: int = self.assigned_state.allocated_time // 2  # TODO check

        lane1_density = self.density_state.car_density[on_led_s[0]]
        lane2_density = self.density_state.car_density[on_led_s[1]]

        self.density_state.car_density[
            on_led_s[0]] = lane1_density - crossed_cars if lane1_density > crossed_cars else 0
        self.density_state.car_density[
            on_led_s[1]] = lane2_density - crossed_cars if lane2_density > crossed_cars else 0

        random_density_state: [int] = []
        for i in range(0, 8):
            to_be_added = 0 if self.assigned_state.allocated_time // 4 == 0 \
                else random.random() * self.assigned_state.allocated_time // 3
            to_be_subtracted = random.random() * to_be_added // 2 if to_be_added > 4 else 0
            random_density_state.append(self.density_state.car_density[i] + to_be_added - to_be_subtracted)
        return DensityState(car_density=random_density_state)

    def get_updated_waiting_time(self, led_1_index: int, led_2_index: int) -> list:
        waiting_time: [int] = [0] * 8
        for i in range(0, 8):
            if not (i == led_1_index or i == led_2_index) and self.density_state.car_density[i] > 0:
                waiting_time[i] = self.assigned_state.waiting_time[i] + self.assigned_state.allocated_time
        return waiting_time

    def get_updated_waiting_time_when_1_empty_lane(self, led_index: int) -> list:
        waiting_time: [int] = [0] * 8
        for i in range(0, 8):
            if i != led_index and self.density_state.car_density[i] > 0:
                waiting_time[i] = self.assigned_state.waiting_time[i] + self.assigned_state.allocated_time
        return waiting_time

    def get_best_pair_for_waited_long(self, x: int) -> int:
        best_pair: int = 0
        # Might cause problem, used to remove null value error
        # Check with code before refactor
        max_density: int = 0
        max_waiting_time: int = 0
        pairs: [int] = self.get_lane_pairs(x)
        for pair in pairs:
            if ((self.assigned_state.waiting_time[pair] > max_waiting_time and
                 self.density_state.car_density[pair] > 0) or
                    (self.assigned_state.waiting_time[pair] == max_waiting_time and
                     self.density_state.car_density[pair] > max_density)):
                max_waiting_time = self.assigned_state.waiting_time[pair]
                max_density = self.density_state.car_density[pair]
                best_pair = pair
        return best_pair

    def when_time_is_up(self):
        print(self.density_state.car_density_string())
        print(self.assigned_state.state_string())

        on_led_s: [int] = self.assigned_state.get_on_led_s()
        crossed_cars: int = self.assigned_state.allocated_time // 2

        lane1_density = self.density_state.car_density[on_led_s[0]]
        lane2_density = self.density_state.car_density[on_led_s[1]]

        self.density_state.car_density[
            on_led_s[0]] = lane1_density - crossed_cars if lane1_density > crossed_cars else 0
        self.density_state.car_density[
            on_led_s[1]] = lane2_density - crossed_cars if lane2_density > crossed_cars else 0

        density_state = self.get_random_density()

    @staticmethod
    def get_updated_led_state(led_1_index: int, led_2_index: int) -> list:
        led_states: [bool] = [False] * 8
        led_states[led_1_index] = True
        led_states[led_2_index] = True
        return led_states

    @staticmethod
    def get_accepting_road_index(lane_index: int):
        return (lane_index - 1) // 2 if lane_index % 2 == 1 else lane_index // 2

    @staticmethod
    def can_pass_together(x: int, y: int):
        return (y == x + 4 or y == x + 1 or y == (x + 7) % 8) if x < y else (
                y == (x + 4) % 8 or y == x - 1 or y == (x - 7) % 8)

    @staticmethod
    def get_lane_pairs(x: int) -> list:
        pair = [x + 1, (x - 1) % 8] if x % 2 == 0 else [x - 1, (x + 1) % 8]
        pair.append(x + 4 if x <= 3 else x - 4)
        return pair

    @staticmethod
    def re_evaluate_time(waiting_time: list) -> list:
        print("Re-evaluating")
        for i in range(0, 8):
            if waiting_time[i] > 40:
                waiting_time[i] -= 40
        return waiting_time
