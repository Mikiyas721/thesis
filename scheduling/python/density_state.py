class DensityState:

    def __int__(self, car_density=[], prime_capacities=[100, 100, 100, 100]):
        self.car_density = car_density,
        self.prime_capacities = prime_capacities,

    def get_dense_lane_pair(self) -> [int]:
        pair: [int] = []
        largest_density: int = 0
        if self.car_density[1] + self.car_density[5] > largest_density:
            largest_density = self.car_density[1] + self.car_density[5]
            pair = [1, 5]
        if self.car_density[3] + self.car_density[7] > largest_density:
            largest_density = self.car_density[3] + self.car_density[7]
            pair = [3, 7]
        if self.car_density[0] + self.car_density[1] > largest_density:
            largest_density = self.car_density[0] + self.car_density[1]
            pair = [0, 1]
        if self.car_density[2] + self.car_density[3] > largest_density:
            largest_density = self.car_density[2] + self.car_density[3]
            pair = [2, 3]
        if self.car_density[4] + self.car_density[5] > largest_density:
            largest_density = self.car_density[4] + self.car_density[5]
            pair = [4, 5]
        if self.car_density[6] + self.car_density[7] > largest_density:
            largest_density = self.car_density[6] + self.car_density[7]
            pair = [6, 7]
        if self.car_density[0] + self.car_density[7] > largest_density:
            largest_density = self.car_density[0] + self.car_density[7]
            pair = [0, 7]
        if self.car_density[2] + self.car_density[7] > largest_density:
            largest_density = self.car_density[2] + self.car_density[7]
            pair = [2, 7]
        if self.car_density[4] + self.car_density[3] > largest_density:
            largest_density = self.car_density[4] + self.car_density[3]
            pair = [4, 3]
        if self.car_density[6] + self.car_density[5] > largest_density:
            largest_density = self.car_density[6] + self.car_density[5]
            pair = [6, 5]
        if self.car_density[0] + self.car_density[4] > largest_density:
            largest_density = self.car_density[0] + self.car_density[4]
            pair = [0, 4]
        if self.car_density[2] + self.car_density[6] > largest_density:
            pair = [2, 6]
        return pair

    def get_best_limit_reaching_pair(self, limit_reaching_lanes: [int]):
        # TODO use the getLanePairs method instead of checking all
        best_pair: [int] = []
        largest_density: int = 0
        if ((limit_reaching_lanes.contains(1) and limit_reaching_lanes.contains(5)) and
                (self.car_density[1] + self.car_density[5] > largest_density)):
            largest_density = self.car_density[1] + self.car_density[5]
            best_pair = [1, 5]
        if ((limit_reaching_lanes.contains(3) and limit_reaching_lanes.contains(7)) and
                (self.car_density[3] + self.car_density[7] > largest_density)):
            largest_density = self.car_density[3] + self.car_density[7]
            best_pair = [3, 7]
        if ((limit_reaching_lanes.contains(0) and limit_reaching_lanes.contains(1)) and
                (self.car_density[0] + self.car_density[1] > largest_density)):
            largest_density = self.car_density[0] + self.car_density[1]
            best_pair = [0, 1]
        if ((limit_reaching_lanes.contains(2) and limit_reaching_lanes.contains(3)) and
                (self.car_density[2] + self.car_density[3] > largest_density)):
            largest_density = self.car_density[2] + self.car_density[3]
            best_pair = [2, 3]
        if ((limit_reaching_lanes.contains(4) and limit_reaching_lanes.contains(5)) and
                (self.car_density[4] + self.car_density[5] > largest_density)):
            largest_density = self.car_density[4] + self.car_density[5]
            best_pair = [4, 5]
        if ((limit_reaching_lanes.contains(6) and limit_reaching_lanes.contains(7)) and
                (self.car_density[6] + self.car_density[7] > largest_density)):
            largest_density = self.car_density[6] + self.car_density[7]
            best_pair = [6, 7]
        if ((limit_reaching_lanes.contains(0) and limit_reaching_lanes.contains(7)) and
                (self.car_density[0] + self.car_density[7] > largest_density)):
            largest_density = self.car_density[0] + self.car_density[7]
            best_pair = [0, 7]
        if ((limit_reaching_lanes.contains(2) and limit_reaching_lanes.contains(7)) and
                (self.car_density[2] + self.car_density[7] > largest_density)):
            largest_density = self.car_density[2] + self.car_density[7]
            best_pair = [2, 7]
        if ((limit_reaching_lanes.contains(4) and limit_reaching_lanes.contains(3)) and
                (self.car_density[4] + self.car_density[3] > largest_density)):
            largest_density = self.car_density[4] + self.car_density[3]
            best_pair = [4, 3]
        if ((limit_reaching_lanes.contains(6) and limit_reaching_lanes.contains(5)) and
                (self.car_density[6] + self.car_density[5] > largest_density)):
            largest_density = self.car_density[6] + self.car_density[5]
            best_pair = [6, 5]
        if ((limit_reaching_lanes.contains(0) and limit_reaching_lanes.contains(4)) and
                (self.car_density[0] + self.car_density[4] > largest_density)):
            largest_density = self.car_density[0] + self.car_density[4]
            best_pair = [0, 4]
        if ((limit_reaching_lanes.contains(2) and limit_reaching_lanes.contains(6)) and
                (self.car_density[2] + self.car_density[6] > largest_density)):
            best_pair = [2, 6]
        return best_pair

    def car_density_string(self) -> str:
        label: str = ''
        density: str = ''
        for i in range(0, 8):
            label += '${mapIndexToLabel(i)}   '
            density += '${car_density[i]}   '
        return label + '\n' + density

    def map_index_to_label(self, index: int) -> str:
        if index == 0:
            return "a1"
        elif index == 1:
            return "a2"
        elif index == 2:
            return "b1"
        elif index == 3:
            return "b2"
        elif index == 4:
            return "c1"
        elif index == 5:
            return "c2"
        elif index == 6:
            return "d1"
        elif index == 7:
            return "d2"
        else:
            raise Exception("Invalid lane index")
