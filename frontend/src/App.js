import React from 'react';
import logo from './dancing.gif';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo"/>
        <h1>
          Welcome to TG-ASS
        </h1>
        <a
          className="App-link"
          href="https://tgrex.com"
          target="_blank"
          rel="noopener noreferrer"
        >
          Login
        </a>
      </header>
    </div>
  );
}

export default App;
