class DensityState(object):

    def __init__(self, car_density=[], prime_capacities=[100] * 4):
        self.car_density: list = car_density,
        self.prime_capacities: list = prime_capacities,

    def get_dense_lane_pair(self) -> [int]:
        pair: [int] = []
        largest_density: int = 0
        if self.car_density[0][1] + self.car_density[0][5] > largest_density:
            largest_density = self.car_density[0][1] + self.car_density[0][5]
            pair = [1, 5]
        if self.car_density[0][3] + self.car_density[0][7] > largest_density:
            largest_density = self.car_density[0][3] + self.car_density[0][7]
            pair = [3, 7]
        if self.car_density[0][0] + self.car_density[0][1] > largest_density:
            largest_density = self.car_density[0][0] + self.car_density[0][1]
            pair = [0, 1]
        if self.car_density[0][2] + self.car_density[0][3] > largest_density:
            largest_density = self.car_density[0][2] + self.car_density[0][3]
            pair = [2, 3]
        if self.car_density[0][4] + self.car_density[0][5] > largest_density:
            largest_density = self.car_density[0][4] + self.car_density[0][5]
            pair = [4, 5]
        if self.car_density[0][6] + self.car_density[0][7] > largest_density:
            largest_density = self.car_density[0][6] + self.car_density[0][7]
            pair = [6, 7]
        if self.car_density[0][0] + self.car_density[0][7] > largest_density:
            largest_density = self.car_density[0][0] + self.car_density[0][7]
            pair = [0, 7]
        if self.car_density[0][2] + self.car_density[0][7] > largest_density:
            largest_density = self.car_density[0][2] + self.car_density[0][7]
            pair = [2, 7]
        if self.car_density[0][4] + self.car_density[0][3] > largest_density:
            largest_density = self.car_density[0][4] + self.car_density[0][3]
            pair = [4, 3]
        if self.car_density[0][6] + self.car_density[0][5] > largest_density:
            largest_density = self.car_density[0][6] + self.car_density[0][5]
            pair = [6, 5]
        if self.car_density[0][0] + self.car_density[0][4] > largest_density:
            largest_density = self.car_density[0][0] + self.car_density[0][4]
            pair = [0, 4]
        if self.car_density[0][2] + self.car_density[0][6] > largest_density:
            pair = [2, 6]
        return pair

    def get_best_limit_reaching_pair(self, limit_reaching_lanes: [int]):
        # TODO use the getLanePairs method instead of checking all
        best_pair: [int] = []
        largest_density: int = 0
        if ((1 in limit_reaching_lanes and 5 in limit_reaching_lanes) and
                (self.car_density[0][1] + self.car_density[0][5] > largest_density)):
            largest_density = self.car_density[0][1] + self.car_density[0][5]
            best_pair = [1, 5]
        if ((3 in limit_reaching_lanes and 7 in limit_reaching_lanes) and
                (self.car_density[0][3] + self.car_density[0][7] > largest_density)):
            largest_density = self.car_density[0][3] + self.car_density[0][7]
            best_pair = [3, 7]
        if ((0 in limit_reaching_lanes and 1 in limit_reaching_lanes) and
                (self.car_density[0][0] + self.car_density[0][1] > largest_density)):
            largest_density = self.car_density[0][0] + self.car_density[0][1]
            best_pair = [0, 1]
        if ((2 in limit_reaching_lanes and 3 in limit_reaching_lanes) and
                (self.car_density[0][2] + self.car_density[0][3] > largest_density)):
            largest_density = self.car_density[0][2] + self.car_density[0][3]
            best_pair = [2, 3]
        if ((4 in limit_reaching_lanes and 5 in limit_reaching_lanes) and
                (self.car_density[0][4] + self.car_density[0][5] > largest_density)):
            largest_density = self.car_density[0][4] + self.car_density[0][5]
            best_pair = [4, 5]
        if ((6 in limit_reaching_lanes and 7 in limit_reaching_lanes) and
                (self.car_density[0][6] + self.car_density[0][7] > largest_density)):
            largest_density = self.car_density[0][6] + self.car_density[0][7]
            best_pair = [6, 7]
        if ((0 in limit_reaching_lanes and 7 in limit_reaching_lanes) and
                (self.car_density[0][0] + self.car_density[0][7] > largest_density)):
            largest_density = self.car_density[0][0] + self.car_density[0][7]
            best_pair = [0, 7]
        if ((2 in limit_reaching_lanes and 7 in limit_reaching_lanes) and
                (self.car_density[0][2] + self.car_density[0][7] > largest_density)):
            largest_density = self.car_density[0][2] + self.car_density[0][7]
            best_pair = [2, 7]
        if ((4 in limit_reaching_lanes and 3 in limit_reaching_lanes) and
                (self.car_density[0][4] + self.car_density[0][3] > largest_density)):
            largest_density = self.car_density[0][4] + self.car_density[0][3]
            best_pair = [4, 3]
        if ((6 in limit_reaching_lanes and 5 in limit_reaching_lanes) and
                (self.car_density[0][6] + self.car_density[0][5] > largest_density)):
            largest_density = self.car_density[0][6] + self.car_density[0][5]
            best_pair = [6, 5]
        if ((0 in limit_reaching_lanes and 4 in limit_reaching_lanes) and
                (self.car_density[0][0] + self.car_density[0][4] > largest_density)):
            largest_density = self.car_density[0][0] + self.car_density[0][4]
            best_pair = [0, 4]
        if ((2 in limit_reaching_lanes and 6 in limit_reaching_lanes) and
                (self.car_density[0][2] + self.car_density[0][6] > largest_density)):
            best_pair = [2, 6]
        return best_pair

    def car_density_string(self) -> str:
        label: str = ''
        density: str = ''
        for i in range(0, 8):
            label += self.map_index_to_label(i) + '   '
            density += str(self.car_density[0][i]) + '   '
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
