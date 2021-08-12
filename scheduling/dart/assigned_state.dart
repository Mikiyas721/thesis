const int maximum_waiting_time = 120;
const int maximum_assignable_time = 40;

class AssignedState {
  List<int>
      waiting_time; // better to use timestamp of when the side got blocked

  int allocatedTime;
  List<bool> ledState;

  AssignedState({
    this.ledState = const [],
    this.waiting_time = const [],
    this.allocatedTime = 0,
  });

  List<int> waitedLongLanes() {
    List<int> waitedLongList = [];
    for (int i = 0; i < 8; i++) {
      if (waiting_time[i] > maximum_waiting_time - 15) waitedLongList.add(i);
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

