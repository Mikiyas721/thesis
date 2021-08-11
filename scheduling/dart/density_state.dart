class DensityState {
  List<int> car_density;

  List<int> prime_capacities;

  DensityState({
    this.car_density = const [],
    this.prime_capacities = const [],
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
}
