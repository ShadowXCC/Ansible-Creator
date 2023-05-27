import React, { Component } from 'react'
import CodeMirror from '@uiw/react-codemirror'
import { StreamLanguage } from '@codemirror/language'
import { yaml } from '@codemirror/legacy-modes/mode/yaml'
import { markdown } from '@codemirror/lang-markdown'

import './index.css'
import './App.css'
import logo from './logo.png'

const header = 
  <header id="header">
    <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
    <nav>
      <a href="/"><img id="menu-icon" src={ logo } alt="Company's Logo"/></a>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/Products">Products</a></li>
        <li><a href="/Pricing">Pricing</a></li>
        <li><a href="/Voting">Voting</a></li>
        <li><a href="/Account"><ion-icon name="person-outline"></ion-icon></a></li>
      </ul>
    </nav>
  </header>

const ansibleButtons =
  <div>
    <></>
  </div>

var defaultYAML = "---\n- name: Example ansible play\n\thosts: You decide!\n\tremote_user: toor"
const codeMirror = 
  <div class="cm-container">
    <CodeMirror
      value={ defaultYAML }
      height="900px"
      width="100%"
      extensions={[StreamLanguage.define(yaml), markdown(yaml)]}
    />
  </div>

//This was used to allow for dynamic switching of the language, this is not needed as it should always be YAML
//import { languages } from "@codemirror/language-data"
//markdown({codeLanguages: languages})

const homePage =
  <div class="">
    {}
  </div>

const votingPage =
  <div class="">
    {}
  </div>

const paidAnsiblePage =
  <div class="container">
    {header}
    {ansibleButtons}
    {codeMirror}
  </div>

const freeAnsiblePage =
  <div class="container">
    {header}
    {ansibleButtons}
    {codeMirror}
  </div>

var toRender
var choice = 1

if (choice === 1) {
  toRender = paidAnsiblePage
} else if (choice === 2) {
  toRender = freeAnsiblePage
} else if (choice === 3) {
  toRender = homePage
} else if (choice === 4) {
  toRender = votingPage
}

class App extends Component {

  render(){
    return (
      toRender
    )
  }
}

export default App

// import logo from './logo.svg'
// import './App.css'

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
//   )
// }

// export default App
