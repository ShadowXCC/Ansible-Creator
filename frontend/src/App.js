import React, { Component } from 'react';
import './index.css';
import './App.css';
import MessageView from './components/message-view';
import MessageView2 from './components/message-view-2';
import MessageList from './components/message-list';

var test = <p>THIS IS A TEST</p>
const toRender = 
  <div>
    <h1 className="header-red">Heading</h1>
    {test}
    <h3>a</h3>
    <MessageView/>
    <MessageView2/>
    <MessageList/>
  </div>

class App extends Component {

  render(){
    return (
      toRender
    )
  }
}

export default App;

// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
