class DensityState {
  List<int> car_density;

  List<int> prime_capacities;

  DensityState({
    this.car_density = const [],
    this.prime_capacities = const [100, 100, 100, 100],
  });

  List<int> getDenseLanePair() {
    List<int> pair = [];
    int largest_density = 0;
    if (car_density[1] + car_density[5] > largest_density) {
      largest_density = car_density[1] + car_density[5];
      pair = [1, 5];
    }
    if (car_density[3] + car_density[7] > largest_density) {
      largest_density = car_density[3] + car_density[7];
      pair = [3, 7];
    }
    if (car_density[0] + car_density[1] > largest_density) {
      largest_density = car_density[0] + car_density[1];
      pair = [0, 1];
    }
    if (car_density[2] + car_density[3] > largest_density) {
      largest_density = car_density[2] + car_density[3];
      pair = [2, 3];
    }
    if (car_density[4] + car_density[5] > largest_density) {
      largest_density = car_density[4] + car_density[5];
      pair = [4, 5];
    }
    if (car_density[6] + car_density[7] > largest_density) {
      largest_density = car_density[6] + car_density[7];
      pair = [6, 7];
    }
    if (car_density[0] + car_density[7] > largest_density) {
      largest_density = car_density[0] + car_density[7];
      pair = [0, 7];
    }
    if (car_density[2] + car_density[7] > largest_density) {
      largest_density = car_density[2] + car_density[7];
      pair = [2, 7];
    }
    if (car_density[4] + car_density[3] > largest_density) {
      largest_density = car_density[4] + car_density[3];
      pair = [4, 3];
    }
    if (car_density[6] + car_density[5] > largest_density) {
      largest_density = car_density[6] + car_density[5];
      pair = [6, 5];
    }
    if (car_density[0] + car_density[4] > largest_density) {
      largest_density = car_density[0] + car_density[4];
      pair = [0, 4];
    }
    if (car_density[2] + car_density[6] > largest_density) {
      largest_density = car_density[2] + car_density[6];
      pair = [2, 6];
    }
    return pair;
  }

  List<int> getBestLimitReachingPair(List<int> limitReachingLanes) {
    //TODO use the getLanePairs method instead of checking all
    List<int> bestPair = [];
    int largest_density = 0;
    if ((limitReachingLanes.contains(1) && limitReachingLanes.contains(5)) &&
        (car_density[1] + car_density[5] > largest_density)) {
      largest_density = car_density[1] + car_density[5];
      bestPair = [1, 5];
    }
    if ((limitReachingLanes.contains(3) && limitReachingLanes.contains(7)) &&
        (car_density[3] + car_density[7] > largest_density)) {
      largest_density = car_density[3] + car_density[7];
      bestPair = [3, 7];
    }
    if ((limitReachingLanes.contains(0) && limitReachingLanes.contains(1)) &&
        (car_density[0] + car_density[1] > largest_density)) {
      largest_density = car_density[0] + car_density[1];
      bestPair = [0, 1];
    }
    if ((limitReachingLanes.contains(2) && limitReachingLanes.contains(3)) &&
        (car_density[2] + car_density[3] > largest_density)) {
      largest_density = car_density[2] + car_density[3];
      bestPair = [2, 3];
    }
    if ((limitReachingLanes.contains(4) && limitReachingLanes.contains(5)) &&
        (car_density[4] + car_density[5] > largest_density)) {
      largest_density = car_density[4] + car_density[5];
      bestPair = [4, 5];
    }
    if ((limitReachingLanes.contains(6) && limitReachingLanes.contains(7)) &&
        (car_density[6] + car_density[7] > largest_density)) {
      largest_density = car_density[6] + car_density[7];
      bestPair = [6, 7];
    }
    if ((limitReachingLanes.contains(0) && limitReachingLanes.contains(7)) &&
        (car_density[0] + car_density[7] > largest_density)) {
      largest_density = car_density[0] + car_density[7];
      bestPair = [0, 7];
    }
    if ((limitReachingLanes.contains(2) && limitReachingLanes.contains(7)) &&
        (car_density[2] + car_density[7] > largest_density)) {
      largest_density = car_density[2] + car_density[7];
      bestPair = [2, 7];
    }
    if ((limitReachingLanes.contains(4) && limitReachingLanes.contains(3)) &&
        (car_density[4] + car_density[3] > largest_density)) {
      largest_density = car_density[4] + car_density[3];
      bestPair = [4, 3];
    }
    if ((limitReachingLanes.contains(6) && limitReachingLanes.contains(5)) &&
        (car_density[6] + car_density[5] > largest_density)) {
      largest_density = car_density[6] + car_density[5];
      bestPair = [6, 5];
    }
    if ((limitReachingLanes.contains(0) && limitReachingLanes.contains(4)) &&
        (car_density[0] + car_density[4] > largest_density)) {
      largest_density = car_density[0] + car_density[4];
      bestPair = [0, 4];
    }
    if ((limitReachingLanes.contains(2) && limitReachingLanes.contains(6)) &&
        (car_density[2] + car_density[6] > largest_density)) {
      largest_density = car_density[2] + car_density[6];
      bestPair = [2, 6];
    }
    return bestPair;
  }

  String carDensityString() {
    String label = '';
    String density = '';
    for (int i = 0; i < 8; i++) {
      label += '${mapIndexToLabel(i)}   ';
      density += '${car_density[i]}   ';
    }
    return label + '\n' + density;
  }

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
}
