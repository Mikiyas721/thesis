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
                <Table/>
            </div>


        </div>
    );
}

export default App;
