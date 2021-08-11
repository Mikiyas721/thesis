const int maximum_waiting_time = 120;
const int maximum_assignable_time = 40;

class AssignedState {
  List<int>
      waiting_time; // better to use timestamp of when the side got blocked

  bool is_a1_on;
  bool is_a2_on;
  bool is_b1_on;
  bool is_b2_on;
  bool is_c1_on;
  bool is_c2_on;
  bool is_d1_on;
  bool is_d2_on;

  AssignedState({
    this.is_a1_on = false,
    this.is_a2_on = false,
    this.is_b1_on = false,
    this.is_b2_on = false,
    this.is_c1_on = false,
    this.is_c2_on = false,
    this.is_d1_on = false,
    this.is_d2_on = false,
    this.waiting_time = const [],
  });

  List<int> waitedLongLanes() {
    List<int> waitedLongList = [];
    for (int i = 0; i < 8; i++) {
      if (i > maximum_waiting_time - 15) waitedLongList.add(i);
    }
    return waitedLongList;
  }

  int closestWaitingTimeToMax() {
    int closest = maximum_waiting_time;
    for (int i = 0; i < 8; i++) {
      if (closest > maximum_waiting_time - waiting_time[i])
        closest = maximum_waiting_time - waiting_time[i];
    }
    return closest;
  }
}
