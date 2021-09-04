import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import reportWebVitals from './reportWebVitals';
import M from 'materialize-css/dist/js/materialize.min'

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

document.addEventListener('DOMContentLoaded', function() {
    const elements = document.querySelectorAll('.collapsible');
    M.Collapsible.init(elements);
});

reportWebVitals();
