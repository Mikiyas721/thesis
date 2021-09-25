import time

import src.hw.hardware_manipulator as hw
from src.classifier.classifier import Classifier
from src.http.http_client import HttpClient
from src.scheduler.assigned_state import AssignedState
from src.scheduler.density_state import DensityState
from src.scheduler.scheduler import Scheduler


def main():
    classifier = Classifier()

    density_state = DensityState(
        car_density=[classifier.count_cars('./test_images/0.jpg'),
                     classifier.count_cars('./test_images/1.jpg'),
                     classifier.count_cars('./test_images/2.jpg'),
                     classifier.count_cars('./test_images/3.jpg'),
                     classifier.count_cars('./test_images/4.jpg'),
                     classifier.count_cars('./test_images/5.jpg'),
                     classifier.count_cars('./test_images/6.jpg'),
                     classifier.count_cars('./test_images/7.jpg')],
    )
    scheduler = Scheduler(AssignedState(), density_state)
    assigned_state = scheduler.calculate()
    scheduler = Scheduler(assigned_state, density_state)
    while True:
        # Adding data and sending to API
        lane_data: [HttpClient] = []
        for lane_index in density_state.car_density:
            lane_data.append(HttpClient(density_state.get_lane_data(lane_index)))

        for lane in lane_data:
            lane.add_record()

        # controlling Lights
        hw.turn_greens_on(assigned_state.get_on_led_s())
        sleep(assigned_state.allocated_time)

        hw.turn_yellows_on(assigned_state.get_on_led_s())
        sleep(3)

        # In actual application order cameras to take pictures and stores them in test_images folder labeled 0-7

        # re-calculate
        density_state = DensityState(
            car_density=[classifier.count_cars('./test_images/0.jpg'),
                         classifier.count_cars('./test_images/1.jpg'),
                         classifier.count_cars('./test_images/2.jpg'),
                         classifier.count_cars('./test_images/3.jpg'),
                         classifier.count_cars('./test_images/4.jpg'),
                         classifier.count_cars('./test_images/5.jpg'),
                         classifier.count_cars('./test_images/6.jpg'),
                         classifier.count_cars('./test_images/7.jpg')],
        )
        assigned_state = scheduler.calculate()
        scheduler = Scheduler(assigned_state, density_state)
        pass


if __name__ == "__main__":
    main()
