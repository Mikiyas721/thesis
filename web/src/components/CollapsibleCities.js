import React from "react";
import 'materialize-css/dist/css/materialize.min.css'

const noLocationMessage = 'No Location Registered Under this Sub-city';
const CollapsibleCities = (props) => {
    return (
        <div style={{margin: "0 0 0 50px", width: "350px"}}>
            <ul className="collapsible">
                <li>
                    <div className="collapsible-header">
                        <i className="material-icons">navigate_next</i>Addis Ababa
                    </div>
                    <div className="collapsible-body" style={{margin: "0",padding:"10"}}>
                        <div className="row">
                            <div className="col s12 m12">
                                <ul className="collapsible" data-collapsible="accordion" style={{margin:"0"}}>
                                    <li>
                                        <div className="collapsible-header">
                                            <i className="material-icons">navigate_next</i>Addis Ketema
                                        </div>
                                        <div className="collapsible-body">
                                            <p>{noLocationMessage}</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div className="collapsible-header">
                                            <i className="material-icons">navigate_next</i>Akaki Kality
                                        </div>
                                        <div className="collapsible-body">
                                            <p>{noLocationMessage}</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div className="collapsible-header">
                                            <i className="material-icons">navigate_next</i>Arada
                                        </div>
                                        <div className="collapsible-body">
                                            <p>{noLocationMessage}</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div className="collapsible-header">
                                            <i className="material-icons">navigate_next</i>Bole
                                        </div>
                                        <div className="collapsible-body">
                                            <p>{noLocationMessage}</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div className="collapsible-header">
                                            <i className="material-icons">navigate_next</i>Gulele
                                        </div>
                                        <div className="collapsible-body">
                                            <p>{noLocationMessage}</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div className="collapsible-header">
                                            <i className="material-icons">navigate_next</i>Kirkos
                                        </div>
                                        <div className="collapsible-body">
                                            <p>{noLocationMessage}</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div className="collapsible-header">
                                            <i className="material-icons">navigate_next</i>Kolfe Keranyo
                                        </div>
                                        <div className="collapsible-body">
                                            <p>{noLocationMessage}</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div className="collapsible-header">
                                            <i className="material-icons">navigate_next</i>Lideta
                                        </div>
                                        <div className="collapsible-body">
                                            <p>{noLocationMessage}</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div className="collapsible-header">
                                            <i className="material-icons">navigate_next</i>Nefas Silk
                                        </div>
                                        <div className="collapsible-body">
                                            <i className="material-icons">location_on</i>Adey Ababa
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    );
}

export default CollapsibleCities;