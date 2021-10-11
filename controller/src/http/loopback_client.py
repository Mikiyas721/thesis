import requests
from src.config import config


class LoopbackClient:
    def __init__(self, lane_data):
        self.lane_data: LaneData = lane_data

    def add_record(self):
        post_request = requests.post(
            config.configs['api_base_url'] + '/vehicle_counts?access_token=' + config.configs['access_token'],
            data={
                "side": self.lane_data.side,
                "lane_number": self.lane_data.lane_number,
                "vehicle_number": self.lane_data.vehicle_count,
                "cross_road_id": self.lane_data.cross_road_id,
            })
        return post_request


class LaneData:
    def __init__(self, side, lane_number, vehicle_count, cross_road_id=None):
        self.side: str = side
        self.lane_number: int = lane_number
        self.vehicle_count: int = vehicle_count
        self.cross_road_id: str = 'string' if cross_road_id is None else cross_road_id


httpClient = LoopbackClient(lane_data=LaneData(
    side='a',
    lane_number=2,
    vehicle_count=15,
))

httpClient.add_record()
