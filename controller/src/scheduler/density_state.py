from src.http.loopback_client import LaneData

possible_lane_pairs = [
    [1, 5],
    [3, 7],
    [0, 1],
    [2, 3],
    [4, 5],
    [6, 7],
    [0, 7],
    [2, 7],
    [4, 3],
    [6, 5],
    [0, 4],
    [2, 6],
]


class DensityState(object):

    def __init__(self,
                 car_density=None):
        self.car_density: list[int] = [] if car_density is None else car_density

    def get_dense_lane_pair(self) -> [int]:
        dense_pair: [int] = []
        largest_density: int = 0

        for pair in possible_lane_pairs:
            if self.car_density[pair[0]] + self.car_density[pair[1]] > largest_density:
                largest_density = self.car_density[pair[0]] + self.car_density[pair[1]]
                dense_pair = pair
        return dense_pair

    def get_best_limit_reaching_pair(self, limit_reaching_lanes: [int]):
        best_pair: [int] = []
        largest_density: int = 0

        for pair in possible_lane_pairs:
            if ((pair[0] in limit_reaching_lanes and pair[1] in limit_reaching_lanes) and
                    (self.car_density[pair[0]] + self.car_density[pair[1]] > largest_density)):
                largest_density = self.car_density[pair[0]] + self.car_density[pair[1]]
                best_pair = pair
        return best_pair

    def car_density_string(self) -> str:
        label: str = ''
        density: str = ''
        for i in range(0, 8):
            label += DensityState.map_index_to_label(i) + '   '
            density += str(self.car_density[i]) + '   '
        return label + '\n' + density

    def get_lane_data(self, lane_index: int) -> LaneData:
        if lane_index == 0:
            return LaneData(side="a", lane_number=1, vehicle_count=self.car_density[lane_index])
        elif lane_index == 1:
            return LaneData(side="a", lane_number=2, vehicle_count=self.car_density[lane_index])
        elif lane_index == 2:
            return LaneData(side="b", lane_number=1, vehicle_count=self.car_density[lane_index])
        elif lane_index == 3:
            return LaneData(side="b", lane_number=2, vehicle_count=self.car_density[lane_index])
        elif lane_index == 4:
            return LaneData(side="c", lane_number=1, vehicle_count=self.car_density[lane_index])
        elif lane_index == 5:
            return LaneData(side="c", lane_number=2, vehicle_count=self.car_density[lane_index])
        elif lane_index == 6:
            return LaneData(side="d", lane_number=1, vehicle_count=self.car_density[lane_index])
        elif lane_index == 7:
            return LaneData(side="d", lane_number=2, vehicle_count=self.car_density[lane_index])
        else:
            raise Exception("Invalid lane index")

    @staticmethod
    def map_index_to_label(index: int) -> str:
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


