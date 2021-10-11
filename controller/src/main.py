from time import sleep
from datetime import datetime

# import src.hw.hardware_manipulator as hw
from src.classifier.classifier import Classifier
from src.http.loopback_client import LoopbackClient
from src.scheduler.assigned_state import AssignedState
from src.scheduler.density_state import DensityState
from src.scheduler.scheduler import Scheduler


def main():
    classifier = Classifier()

    lane_densities = [
        [7, 10, 12, 10, 10, 20, 8, 15],
        [10, 0, 8, 15, 5, 0, 7, 15],
        [10, 15, 8, 15, 7, 15, 8, 15],
    ]
    lane_waiting_times = [
        [0]*8,
        [40, 120, 40, 0, 0, 120, 80, 80],
        [40, 80, 40, 40, 40, 80, 40, 40],
    ]

    density_state = DensityState(
        car_density=[classifier.count_cars('E:\\Files\\Code\\Thesis\\controller\\src\\classifier\\test_images\\0.jpg'),
                     classifier.count_cars('E:\\Files\\Code\\Thesis\\controller\\src\\classifier\\test_images\\1.jpg'),
                     classifier.count_cars('E:\\Files\\Code\\Thesis\\controller\\src\\classifier\\test_images\\2.jpg'),
                     classifier.count_cars('E:\\Files\\Code\\Thesis\\controller\\src\\classifier\\test_images\\3.jpg'),
                     classifier.count_cars('E:\\Files\\Code\\Thesis\\controller\\src\\classifier\\test_images\\4.jpg'),
                     classifier.count_cars('E:\\Files\\Code\\Thesis\\controller\\src\\classifier\\test_images\\1.jpg'),
                     classifier.count_cars('E:\\Files\\Code\\Thesis\\controller\\src\\classifier\\test_images\\0.jpg'),
                     classifier.count_cars('E:\\Files\\Code\\Thesis\\controller\\src\\classifier\\test_images\\2.jpg')],
    )

    scheduler = Scheduler(AssignedState(), density_state)
    assigned_state = scheduler.calculate()
    scheduler = Scheduler(assigned_state, density_state)

    now = datetime.now()

    i = 0
    while i < 3:
        # log state
        # print(density_state.car_density_string())
        # print(assigned_state.state_string())

        # Adding data and sending to API
        if divmod((datetime.now() - now).total_seconds(), 3600)[0] >= 1:
            lane_data: [LoopbackClient] = []
            for lane_index in density_state.car_density:
                lane_data.append(LoopbackClient(density_state.get_lane_data(lane_index)))

            for lane in lane_data:
                lane.add_record()

            now = datetime.now()

        # controlling Lights
        # hw.turn_greens_on(assigned_state.get_on_led_s())
        # sleep(assigned_state.allocated_time)

        # hw.turn_yellows_on(assigned_state.get_on_led_s())
        # sleep(3)

        # In actual application order cameras to take pictures and stores them in test_images folder labeled 0-7

        density_state = DensityState(car_density=lane_densities[i])
        assigned_state = AssignedState(waiting_time=lane_waiting_times[i])

        # re-calculate
        scheduler = Scheduler(assigned_state, density_state)
        assigned_state = scheduler.calculate()

        # log state
        print(density_state.car_density_string())
        print(assigned_state.state_string())

        i += 1
        pass


if __name__ == "__main__":
    main()
