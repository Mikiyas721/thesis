import './App.css';
import React, {Component} from "react";
import CollapsibleCities from "./components/CollapsibleCities";
import NavBar from "./components/NavBar";
import MyTable from "./components/MyTable";
import axios from "axios";
import {accessToken, apiBaseUrl} from './congif'

class App extends Component {
    state = {
        isLoading: false,
        vehicleCountData: [],
        locationDetails: {},
        locationId: 'string'
    }

    async componentDidMount() {
        try {
            this.setState({isLoading: true});
            const response = await axios.post(
                `${apiBaseUrl}/vehicle_counts/getVehicleCountByRoadId/${this.state.locationId}?access_token=${accessToken}`);
            const data = response.data.type;
            const crossRoadDetails = data.crossRoadDetails
console.log(crossRoadDetails)
            this.setState({
                isLoading: false,
                vehicleCountData: data.vehicleCountDetails,
                locationDetails: {
                    cross_road_id: crossRoadDetails.cross_road_id,
                    city: crossRoadDetails.city,
                    subCity: crossRoadDetails.sub_city,
                    latitude: crossRoadDetails.latitude,
                    longitude: crossRoadDetails.longitude,
                    name: crossRoadDetails.common_name,
                    id: crossRoadDetails.id,
                    createdAt: crossRoadDetails.createdAt,
                    updatedAt: crossRoadDetails.updatedAt
                },
            });
        } catch (e) {
            console.log(e);
        }

    }


    render() {
        return (
            <div className="App">
                <NavBar title="Traffic Control"/>
                <div className="flexbox-container"
                     style={{display: "flex", flexDirection: "row"}}>
                    <CollapsibleCities className="SideList"/>
                    <MyTable isLoading={this.state.isLoading}
                             locationDetails={this.state.locationDetails}
                             list={this.state.vehicleCountData}
                    />
                </div>
            </div>
        );
    }
}

export default App;
