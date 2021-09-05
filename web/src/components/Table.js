import React from 'react';
import HeaderTitle from './HeaderTitle'

const Table = ({locationDetails, list}) => {
    return (
        <div className="row">
            <div className="col">
                <div className="card darken-1">
                    <div className="card-content">
                        <div className="card-title"
                             style={{
                                 display: "flex",
                                 flexDirection: "row"
                             }}>
                            <HeaderTitle title="City" content={locationDetails.city}/>
                            <HeaderTitle title="SubCity" content={locationDetails.subCity}/>
                            <HeaderTitle title="Latitude" content={locationDetails.latitude}/>
                            <HeaderTitle title="Longitude" content={locationDetails.longitude}/>
                            <HeaderTitle title="Common Name" content={locationDetails.name}/>
                        </div>
                        <table className="striped centered" style={{width: "900px"}}>
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
                            {list.map((data, index) => (
                                <tr>
                                    <td>{index+1}</td>
                                    <td>{data.side}</td>
                                    <td>{data.laneNumber}</td>
                                    <td>{data.count}</td>
                                    <td>{data.date}</td>
                                    <td>{data.time}</td>
                                </tr>
                            ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Table;