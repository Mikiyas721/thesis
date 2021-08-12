import 'dart:core';

import 'assigned_state.dart';
import 'density_state.dart';

void main() {}

String mapIndexToLabel(int index) {
  if (index == 0)
    return "a1";
  else if (index == 1)
    return "a2";
  else if (index == 2)
    return "b1";
  else if (index == 3)
    return "b2";
  else if (index == 4)
    return "c1";
  else if (index == 5)
    return "c2";
  else if (index == 6)
    return "d1";
  else if (index == 7)
    return "d2";
  else
    throw Exception("Invalid lane index");
}
int getAcceptingRoadIndex(int laneIndex){
  if(laneIndex%2==1) return int.parse(((laneIndex - 1)/2).toString());
  return int.parse((laneIndex/2).toString());
}
bool canPassTogether(int x, int y) {
  if ((x < y) && (y == x + 4 || y == x + 1 || y == (x + 7) % 8)) return true;
  if ((x > y) && (y == (x + 4) % 8 || y == x - 1 || y == (x - 7) % 8))
    return true;
  return false;
}

AssignedState calculate(DensityState densityState,
    AssignedState previousAssignedState) {
  List<int> waitedLongLanes = previousAssignedState.waitedLongLanes();
  if (waitedLongLanes.length > 2) {
    throw Exception("More than two lanes waited long");
    //TODO handle appropriately
  }
  if (waitedLongLanes.length > 0 && waitedLongLanes.length < 3) {
    if (canPassTogether(waitedLongLanes[0], waitedLongLanes[1])) {
      int lane1Density = densityState.car_density[waitedLongLanes[0]];
      int lane2Density = densityState.car_density[waitedLongLanes[1]];
      if (lane1Density == 0 && lane2Density == 0) {
        return calculate(densityState, AssignedState(
          allocatedTime: 0,
          waiting_time: getUpdatedWaitingTime(
            waitedLongLanes[0],
            waitedLongLanes[1],
            0,
            previousAssignedState.waiting_time,
          ),
          ledState: previousAssignedState.ledState,
        ));
      }
      if (densityState.prime_capacities[getAcceptingRoadIndex(waitedLongLanes[0])]<10||
          densityState.prime_capacities[getAcceptingRoadIndex(waitedLongLanes[1])]<10) {
        throw Exception("Waited long but no accepting space");
        //TODO handle appropriately
      }
      return evaluateForTwoLanes(lane1Density, lane2Density, previousAssignedState);
    } else {
      throw Exception("The two lanes that waited long can not cross together");
      //TODO handle appropriately
    }
  }
  List<int> denseLanes = densityState.getDenseLanePair();
  int dense1 = densityState.car_density[denseLanes[0]];
  int dense2 = densityState.car_density[denseLanes[1]];
  return evaluateForTwoLanes(dense1, dense2, previousAssignedState);
}

AssignedState evaluateForTwoLanes(int lane1Density, int lane2Density,
    AssignedState previousAssignedState) {
  if (lane1Density > 20 || lane2Density > 20) {
    int closestWaitingTimeToMax =
    previousAssignedState.closestWaitingTimeToMax();
    if (closestWaitingTimeToMax < 40) {
      return AssignedState(
        allocatedTime: closestWaitingTimeToMax - 2,
        waiting_time: getUpdatedWaitingTime(
          lane1Density,
          lane2Density,
          closestWaitingTimeToMax - 2,
          previousAssignedState.waiting_time,
        ),
        ledState: getUpdatedLEDState(lane1Density, lane2Density),
      );
    }
    return AssignedState(
      allocatedTime: maximum_assignable_time,
      waiting_time: getUpdatedWaitingTime(
        lane1Density,
        lane2Density,
        maximum_assignable_time,
        previousAssignedState.waiting_time,
      ),
      ledState: getUpdatedLEDState(lane1Density, lane2Density),
    );
  }
  int timeToAllocate = lane1Density > lane2Density
      ? lane1Density * 2
      : lane2Density * 2;
  return AssignedState(
    allocatedTime: timeToAllocate,
    waiting_time: getUpdatedWaitingTime(
      lane1Density,
      lane2Density,
      timeToAllocate,
      previousAssignedState.waiting_time,
    ),
    ledState: getUpdatedLEDState(lane1Density, lane2Density),
  );
}

List<int> getUpdatedWaitingTime(int led1Index, int led2Index,
    int timeToAllocate, List<int> previousWaitingTime) {
  List<int> waitingTime = List.filled(8, 0);
  for (int i = 0; i < 8; i++) {
    if (!(i == led1Index || i == led2Index))
      waitingTime[i] = previousWaitingTime[i] + timeToAllocate;
  }
  return waitingTime;
}

List<bool> getUpdatedLEDState(int led1Index, int led2Index) {
  List<bool> ledStates = List.filled(8, false);
  ledStates[led1Index] = true;
  ledStates[led2Index] = true;
  return ledStates;
}
