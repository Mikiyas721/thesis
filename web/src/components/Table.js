import React from 'react';
import HeaderTitle from '../components/HeaderTitle'

const Table = (props) => {
    return (
        <div className="row">
            <div className="col">
                <div className="card darken-1">
                    <div className="card-content">
                        <div className="card-title"
                             style={{
                                 display: "flex",
                                 flexDirection: "row",
                             }}>
                            <HeaderTitle title="City" content="A.A."/>
                            <HeaderTitle title="SubCity" content="N.S."/>
                            <HeaderTitle title="Latitude" content="2° 29'E"/>
                            <HeaderTitle title="Longitude" content="5° 45'N"/>
                            <HeaderTitle title="Common Name" content="Adey Ababa"/>
                        </div>
                        <table style={{width: "900px"}}>
                            <thead>
                            <tr>
                                <th>#</th>
                                <th>Side</th>
                                <th>Lane Number</th>
                                <th>Vehicle Count</th>
                                <th>Date</th>
                                <th>Time</th>
                            </tr>
                            </thead>

                            <tbody>
                            <tr>
                                <td>1</td>
                                <td>b</td>
                                <td>1</td>
                                <td>40</td>
                                <td>9/03/21</td>
                                <td>9:23 PM</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td>a</td>
                                <td>1</td>
                                <td>30</td>
                                <td>9/04/21</td>
                                <td>4:23 AM</td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td>d</td>
                                <td>2</td>
                                <td>18</td>
                                <td>7/23/21</td>
                                <td>10:23 PM</td>
                            </tr>
                            <tr>
                                <td>4</td>
                                <td>b</td>
                                <td>1</td>
                                <td>40</td>
                                <td>9/03/21</td>
                                <td>9:23 PM</td>
                            </tr>
                            <tr>
                                <td>5</td>
                                <td>a</td>
                                <td>1</td>
                                <td>30</td>
                                <td>9/04/21</td>
                                <td>4:23 AM</td>
                            </tr>
                            <tr>
                                <td>6</td>
                                <td>d</td>
                                <td>2</td>
                                <td>18</td>
                                <td>7/23/21</td>
                                <td>10:23 PM</td>
                            </tr>
                            <tr>
                                <td>7</td>
                                <td>b</td>
                                <td>1</td>
                                <td>40</td>
                                <td>9/03/21</td>
                                <td>9:23 PM</td>
                            </tr>
                            <tr>
                                <td>8</td>
                                <td>a</td>
                                <td>1</td>
                                <td>30</td>
                                <td>9/04/21</td>
                                <td>4:23 AM</td>
                            </tr>
                            <tr>
                                <td>9</td>
                                <td>d</td>
                                <td>2</td>
                                <td>18</td>
                                <td>7/23/21</td>
                                <td>10:23 PM</td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Table;