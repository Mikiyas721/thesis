import React from "react";
import 'materialize-css/dist/css/materialize.min.css'

const CollapsibleCities = (props) => {
    return (
        <div style={{margin: "0 0 0 50px", width: "350px"}}>
            <ul className="collapsible">
                <li>
                    <div className="collapsible-header">
                        <i className="material-icons">navigate_next</i>Dire Dawa
                    </div>
                    <div className="collapsible-body" style={{margin:"0"}}>
                        <div className="row">
                            <div className="col s12 m12">
                                <ul className="collapsible" data-collapsible="accordion" >
                                    <li>
                                        <div className="collapsible-header">
                                            <i className="material-icons">filter_drama</i>Nested First
                                        </div>
                                        <div className="collapsible-body">
                                            <p>Lorem ipsum dolor sit amet.</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div className="collapsible-header">
                                            <i className="material-icons">place</i>Nested Second
                                        </div>
                                        <div className="collapsible-body">
                                            <p>Lorem ipsum dolor sit amet.</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div className="collapsible-header">
                                            <i className="material-icons">whatshot</i>Nested Third
                                        </div>
                                        <div className="collapsible-body">
                                            <p>Lorem ipsum dolor sit amet.</p>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </li>
                <li>
                    <div className="collapsible-header"><i className="material-icons">expand_more</i>Addis Ababa</div>
                    <div className="collapsible-body"><span>Lorem ipsum dolor sit amet.</span></div>
                </li>
            </ul>
        </div>
    );
}

export default CollapsibleCities;