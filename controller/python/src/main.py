# import src.hardware_manipulator as hw
from src.classifier.classifier import Classifier
from src.scheduler.assigned_state import AssignedState
from src.scheduler.density_state import DensityState
from src.scheduler.scheduler import Scheduler


def main():
    # Multiple Randomized scenarios
    density_state = DensityState(car_density=[5, 25, 19, 18, 10, 12, 20, 15])
    scheduler = Scheduler(AssignedState(), density_state)
    assigned_state = scheduler.calculate()
    scheduler = Scheduler(assigned_state, density_state)
    while True:
        # print states
        print(density_state.car_density_string())
        print(assigned_state.state_string())

        # hw.turn_greens_on(assigned_state.get_on_led_s())
        # sleep(assigned_state.allocated_time)
        #
        # hw.turn_yellows_on(assigned_state.get_on_led_s())
        # sleep(3)

        density_state = \
            scheduler.get_random_density()
        assigned_state = scheduler.calculate()
        scheduler = Scheduler(assigned_state, density_state)
    pass


if __name__ == "__main__":
    main()
