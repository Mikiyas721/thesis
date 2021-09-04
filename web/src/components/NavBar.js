import React from 'react';

const NavBar = ({title}) => {
    return (
        <nav className="light-blue">
            <h4 style={{margin:"0 0 0 50px", padding:"8px 0 0 0"}}>{title}</h4>
        </nav>
    );
};

NavBar.defaultProps = {
    title: 'Nav Bar',
}

export default NavBar;