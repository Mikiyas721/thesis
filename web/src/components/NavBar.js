import React from 'react';

const NavBar = ({title, onRefresh}) => {
    return (
        <nav className="light-blue"
             style={{
                 display: "flex",
                 flexDirection: "row"
             }}>
            <h4
                style={{
                    margin: "0 0 0 50px",
                    padding: "8px 0 0 0"
                }}>{title}</h4>
            <a className="waves-effect waves-teal btn-flat"
               style={{
                   margin: "0 0 0 74%",
                   alignContent: "center",
                   borderRadius: "50%"
               }}>
                <i className="material-icons"
                   style={{
                       color: "white"
                   }} onClick={{onRefresh}}>refresh</i></a>
        </nav>
    );
};

NavBar.defaultProps = {
    title: 'Nav Bar',
}

export default NavBar;