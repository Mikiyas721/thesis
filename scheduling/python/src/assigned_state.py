maximum_waiting_time = 120
maximum_assignable_time = 40


class AssignedState(object):

    def __init__(self, led_state=[False] * 8, waiting_time=[0] * 8,
                 critically_waiting=[], allocated_time=0):
        self.led_state: list = led_state,
        self.waiting_time: list = waiting_time,
        self.critically_waiting: list = critically_waiting,
        self.allocated_time: int = allocated_time,

    def waited_long_lanes(self):
        waited_long_list = []
        for i in range(0, 8):
            if self.waiting_time[0][i] > maximum_waiting_time - 15:
                waited_long_list.append(i)
        return waited_long_list

    def get_lanes_reaching_limit(self) -> [int]:
        reaching_limit: [int] = []
        for i in range(0, 8):
            if self.waiting_time[0][i] >= maximum_waiting_time - maximum_assignable_time:
                reaching_limit.append(i)
        return reaching_limit

    def closest_waiting_time_to_max(self, selected_lane1: int, selected_lane2: int) -> int:
        # Not effective when two lanes waited long but cant pass together
        closest: int = maximum_waiting_time
        for i in range(0, 8):
            if i == selected_lane1 | i == selected_lane2:
                continue
            elif ((self.waiting_time[0][i] != maximum_waiting_time) and
                  closest > maximum_waiting_time - self.waiting_time[0][i]):
                closest = maximum_waiting_time - self.waiting_time[0][i]
        return closest

    def get_on_led_s(self) -> [int]:
        on_led_s: [int] = []
        for i in range(0, 8):
            if self.led_state[0][i]:
                on_led_s.append(i)
        return on_led_s

    def state_string(self) -> str:
        led: str = ''
        waiting_time_str: str = ''
        for i in range(0, 8):
            led += '1    ' if self.led_state[0][i] else '0    '
            waiting_time_str += str(self.waiting_time[0][i]) + '   '
        return led + '\n' + waiting_time_str + '   Allocated Time ' + str(self.allocated_time[0]) + ' sec' + '\n\n'
