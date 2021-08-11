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

bool canPassTogether(int x, int y) {
  if ((x < y) && (y == x + 4 || y == x + 1 || y == (x + 7) % 8)) return true;
  if ((x > y) && (y == (x + 4) % 8 || y == x - 1 || y == (x - 7) % 8))
    return true;
  return false;
}

calculate(DensityState densityState, AssignedState previousAssignedState) {
  List<int> waitedLongLanes = previousAssignedState.waitedLongLanes();
  if (waitedLongLanes.length > 2) {
    throw Exception("More than two lanes waited long");
    //TODO handle appropriately
  } else if (waitedLongLanes.length > 0 && waitedLongLanes.length < 3) {
    if (canPassTogether(waitedLongLanes[0], waitedLongLanes[1])) {
      if (densityState.car_density[waitedLongLanes[0]] > 1 &&
          densityState.car_density[waitedLongLanes[0]] > 1) {}
    } else {
      //
    }
  } else {
    List<int> denseLanes = densityState.getDenseLanePair();
    int dense1 = densityState.car_density[denseLanes[0]];
    int dense2 = densityState.car_density[denseLanes[1]];
    if (dense1 > 20 || dense2 > 20) {
      if (previousAssignedState.closestWaitingTimeToMax() < 40) {
        //TODO Assign closestWaitingTimeToMax-2 to denseLanes
      }
    } else {
      int timeToAllocate = dense1 > dense2 ? dense1 * 2 : dense2 * 2;
      //TODO Assign timeToAllocate to denseLanes
    }
  }
}
