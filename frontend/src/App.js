import React, { Component } from 'react';
import CodeMirror from '@uiw/react-codemirror';
import { StreamLanguage } from '@codemirror/language';
import { yaml } from '@codemirror/legacy-modes/mode/yaml';
import { markdown } from '@codemirror/lang-markdown'

import './index.css';
import './App.css';
import logo from './logo.png'

const header = 
  <header id="header">
    <nav>
      <a href="clepore.com"><img id="menu-icon" src={ logo } alt="Company's Logo"/></a>
      <ul>
        <li><a href="/Home">Home</a></li>
        <li><a href="/Pricing">Pricing</a></li>
        <li><a href="/Voting">Voting</a></li>
        <li><a href="/Account">Account</a></li>
      </ul>
    </nav>
  </header>

var defaultYAML = "---\n- name: Update web servers\n\thosts: webservers\n\tremote_user: root"

const codeMirror = 
<CodeMirror
      value={ defaultYAML }
      height="200px"
      width="50%"
      extensions={[StreamLanguage.define(yaml), markdown(yaml)]}
    />

//This was used to allow for dynamic switching of the language, this is not needed as it should always be YAML
//import { languages } from "@codemirror/language-data"
//markdown({codeLanguages: languages})





const toRender = 
  <div>
    {header}

    {codeMirror}
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
