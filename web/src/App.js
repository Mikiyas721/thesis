import './App.css';
import React from "react";
import CollapsibleCities from "./components/CollapsibleCities";
import NavBar from "./components/NavBar";
import Table from "./components/Table";

const App = () => {
    return (
        <div>
            <NavBar title="Traffic Control"/>
            <div className="flexbox-container"
                 style={{display: "flex", flexDirection: "row"}}>
                <CollapsibleCities className="SideList"/>
                <Table locationDetails={
                    {
                        city: "A.A.",
                        subCity: "N.S.",
                        latitude: "2° 29'E",
                        longitude: "5° 45'N",
                        name: "Adey Ababa",
                    }
                } list={[
                    {
                        side: 'b',
                        laneNumber: '1',
                        count: '10',
                        date: '9/03/21',
                        time: '11:46AM'
                    },
                    {
                        side: 'a',
                        laneNumber: '1',
                        count: '40',
                        date: '9/04/21',
                        time: '09:46AM'
                    },
                    {
                        side: 'c',
                        laneNumber: '2',
                        count: '15',
                        date: '19/03/21',
                        time: '11:30PM'
                    },
                    {
                        side: 'd',
                        laneNumber: '1',
                        count: '35',
                        date: '9/06/21',
                        time: '02:46AM'
                    },
                    {
                        side: 'b',
                        laneNumber: '1',
                        count: '10',
                        date: '9/03/21',
                        time: '11:46AM'
                    },
                    {
                        side: 'a',
                        laneNumber: '1',
                        count: '40',
                        date: '9/04/21',
                        time: '09:46AM'
                    },
                    {
                        side: 'c',
                        laneNumber: '2',
                        count: '15',
                        date: '19/03/21',
                        time: '11:30PM'
                    },
                    {
                        side: 'd',
                        laneNumber: '1',
                        count: '35',
                        date: '9/06/21',
                        time: '02:46AM'
                    },
                ]}/>
            </div>


        </div>
    );
}

export default App;
