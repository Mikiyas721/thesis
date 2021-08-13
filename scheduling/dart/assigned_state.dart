const int maximum_waiting_time = 120;
const int maximum_assignable_time = 40;

class AssignedState {
  List<int>
      waiting_time; // better to use timestamp of when the side got blocked
  List<int> critically_waiting;
  int allocatedTime;
  List<bool> ledState;

  AssignedState({
    this.ledState = const [
      false,
      false,
      false,
      false,
      false,
      false,
      false,
      false
    ],
    this.waiting_time = const [0, 0, 0, 0, 0, 0, 0, 0],
    this.critically_waiting = const [],
    this.allocatedTime = 0,
  });

  List<int> waitedLongLanes() {
    List<int> waitedLongList = [];
    for (int i = 0; i < 8; i++) {
      if (waiting_time[i] > maximum_waiting_time - 15) waitedLongList.add(i);
    }
    return waitedLongList;
  }

  List<int> getLanesReachingLimit() {
    List<int> reachingLimit = [];
    for (int i = 0; i < 8; i++) {
      if (waiting_time[i] >= maximum_waiting_time - maximum_assignable_time)
        reachingLimit.add(i);
    }
    return reachingLimit;
  }

  int closestWaitingTimeToMax() {
    int closest = maximum_waiting_time;
    for (int i = 0; i < 8; i++) {
      if (!(waiting_time[i] == maximum_waiting_time) &&
          closest > maximum_waiting_time - waiting_time[i])
        closest = maximum_waiting_time - waiting_time[i];
    }
    return closest;
  }

  List<int> getOnLEDs() {
    List<int> onLEDs = [];
    for (int i = 0; i < 8; i++) {
      if (ledState[i]) onLEDs.add(i);
    }
    return onLEDs;
  }

  String stateString() {
    String led = '';
    String waitingTime = '';
    for (int i = 0; i < 8; i++) {
      led += '${ledState[i] ? 1 : 0}    ';
      waitingTime += '${waiting_time[i]}   ';
    }
    return led + '\n' + waitingTime + '\n\n';
  }
}
