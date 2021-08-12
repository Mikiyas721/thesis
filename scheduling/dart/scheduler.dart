import 'dart:core';

import 'assigned_state.dart';
import 'density_state.dart';
import 'dart:math';

void main() {
  DensityState densityState = DensityState(
    car_density: [
      5,
      25,
      19,
      18,
      10,
      12,
      20,
      15,
    ],
  );
  AssignedState assignedState = calculate(densityState, AssignedState());
  int i = 0;
  while (i < 10) {
    print(densityState.carDensityString());
    print(assignedState.stateString());

    List<int> onLEDs = assignedState.getOnLEDs();
    int crossedCars = assignedState.allocatedTime ~/ 2;

    densityState.car_density[onLEDs[0]] > crossedCars
        ? densityState.car_density[onLEDs[0]] -= crossedCars
        : densityState.car_density[onLEDs[0]] = 0;

    densityState.car_density[onLEDs[1]] > crossedCars
        ? densityState.car_density[onLEDs[1]] -= crossedCars
        : densityState.car_density[onLEDs[1]] = 0;

    densityState = getRandomDensity(densityState.car_density);

    final newState = calculate(densityState, assignedState);
    assignedState = newState;
  }
}

DensityState getRandomDensity(List<int> previousDensity) {
  List<int> densityState = [];
  for (int i = 0; i < 8; i++) {
    densityState.add(previousDensity[i] + Random().nextInt(25));
  }
  return DensityState(car_density: densityState);
}

AssignedState calculate(DensityState densityState,
    AssignedState previousAssignedState) {
  List<int> waitedLongLanes = previousAssignedState.waitedLongLanes();
  if (previousAssignedState.critically_waiting.length > 0) {
    //TODO handle critically waiting lanes
  }
  if (waitedLongLanes.length > 2) {
    throw Exception("More than two lanes waited long");
    //TODO handle appropriately
  }
  if (waitedLongLanes.length > 0 && waitedLongLanes.length < 3) {
    if (canPassTogether(waitedLongLanes[0], waitedLongLanes[1])) {
      int lane1Density = densityState.car_density[waitedLongLanes[0]];
      int lane2Density = densityState.car_density[waitedLongLanes[1]];
      if (lane1Density == 0 && lane2Density == 0) {
        return calculate(
            densityState,
            AssignedState(
              allocatedTime: 0,
              waiting_time: getUpdatedWaitingTime(
                  waitedLongLanes[0],
                  waitedLongLanes[1],
                  0,
                  previousAssignedState.waiting_time,
                  densityState.car_density),
              ledState: previousAssignedState.ledState,
            ));
      }
      if (densityState
          .prime_capacities[getAcceptingRoadIndex(waitedLongLanes[0])] <
          10 ||
          densityState
              .prime_capacities[getAcceptingRoadIndex(waitedLongLanes[1])] <
              10) {
        return calculate(
            densityState,
            AssignedState(
              allocatedTime: 0,
              waiting_time: getUpdatedWaitingTime(
                waitedLongLanes[0],
                waitedLongLanes[1],
                0,
                previousAssignedState.waiting_time,
                densityState.car_density,
              ),
              ledState: previousAssignedState.ledState,
            ));
      }
      throw Exception("waited long but no accepting road");
      //TODO handle appropriately
    } else {
      throw Exception("The two lanes that waited long can not cross together");
      //TODO handle appropriately
    }
  }
  List<int> denseLanes = densityState.getDenseLanePair();
  return evaluateForTwoLanes(
    denseLanes[0],
    denseLanes[1],
    previousAssignedState,
    densityState,
  );
}

AssignedState evaluateForTwoLanes(int lane1Index, int lane2Index,
    AssignedState previousAssignedState, DensityState densityState) {
  int lane1Density = densityState.car_density[lane1Index];
  int lane2Density = densityState.car_density[lane2Index];
  if (lane1Density >= 20 || lane2Density >= 20) {
    int closestWaitingTimeToMax =
    previousAssignedState.closestWaitingTimeToMax();
    if (closestWaitingTimeToMax < 40) {
      return AssignedState(
        allocatedTime: closestWaitingTimeToMax - 2,
        waiting_time: getUpdatedWaitingTime(
            lane1Index,
            lane2Index,
            closestWaitingTimeToMax - 2,
            previousAssignedState.waiting_time,
            densityState.car_density),
        ledState: getUpdatedLEDState(lane1Index, lane2Index),
      );
    }
    return AssignedState(
      allocatedTime: maximum_assignable_time,
      waiting_time: getUpdatedWaitingTime(
          lane1Index,
          lane2Index,
          maximum_assignable_time,
          previousAssignedState.waiting_time,
          densityState.car_density),
      ledState: getUpdatedLEDState(lane1Index, lane2Index),
    );
  }
  int timeToAllocate =
  lane1Density > lane2Density ? lane1Density * 2 : lane2Density * 2;
  return AssignedState(
    allocatedTime: timeToAllocate,
    waiting_time: getUpdatedWaitingTime(
      lane1Index,
      lane2Index,
      timeToAllocate,
      previousAssignedState.waiting_time,
      densityState.car_density,
    ),
    ledState: getUpdatedLEDState(lane1Index, lane2Index),
  );
}

List<int> getUpdatedWaitingTime(int led1Index,
    int led2Index,
    int timeToAllocate,
    List<int> previousWaitingTime,
    List<int> previousCarDensity,) {
  List<int> waitingTime = List.filled(8, 0);
  for (int i = 0; i < 8; i++) {
    if (!(i == led1Index || i == led2Index) && previousCarDensity[i] > 0)
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


int getAcceptingRoadIndex(int laneIndex) {
  if (laneIndex % 2 == 1) return int.parse(((laneIndex - 1) / 2).toString());
  return laneIndex ~/ 2;
}

bool canPassTogether(int x, int y) {
  if ((x < y) && (y == x + 4 || y == x + 1 || y == (x + 7) % 8)) return true;
  if ((x > y) && (y == (x + 4) % 8 || y == x - 1 || y == (x - 7) % 8))
    return true;
  return false;
}
