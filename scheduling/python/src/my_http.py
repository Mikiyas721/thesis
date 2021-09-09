import requests
import src.config as config

cross_road_id = 'string'

post_request = requests.post(
    config.api_base_url + '/vehicle_counts?access_token=' + config.access_token, data=
    {
        "side": "b",
        "lane_number": 2,
        "vehicle_number": 22,
        "cross_road_id": cross_road_id,
    })

vehicle_count_data = requests.post(
    config.api_base_url + '/vehicle_counts/getVehicleCountByRoadId/' + cross_road_id + '?access_token=' + config.access_token)

print(vehicle_count_data.json()['type'])
