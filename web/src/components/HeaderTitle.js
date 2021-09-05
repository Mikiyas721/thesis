import React from 'react';

const HeaderTitle = ({title, content}) => {
    return (
        <div style={{margin: "0 50px 0 0"}}>
            <p style={{}}>{title}</p>
            <p style={{color: "grey", textAlign:"center", fontSize:"18px"}}>{content}</p>
        </div>
    );
};

export default HeaderTitle;