import React, {Fragment} from 'react';
import spinner from './spinner.gif';

const Spinner = () =>
    <Fragment>
        <div style={{padding:"0 0 0 25%"}}>
            <div style={{height:"120px", width:"100%"}}/>
            <img src={spinner} alt="Loading..." style={{width: '200px', margin: 'auto', display: 'block'}}/>
        </div>
    </Fragment>

export default Spinner;