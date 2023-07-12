import { useState, useEffect } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
// import './Components/Header.jsx'
import Home from './Components/pages/Home.jsx'
import Login from './Components/login.jsx'
import Signup from './Components/signup.jsx'
import Header from './Components/Header.jsx'
import ProcessUser from './Components/pages/Login-Signup.jsx'
import Context from './Components/Context.jsx'
import 'bootstrap/dist/css/bootstrap.css';
// import './stylesheet/index.css'


function App() {
const [curr_user, setCurr_User] = useState(null)

useEffect(() => {
  if(curr_user == null) {
    fetch('/api/check_session')
    .then(res => {
      if (res.ok) {
        res.json().then(curr_user => {setCurr_User(curr_user)})
      }
    })
  }
},[])

  return (
    <Context.Provider value={{curr_user, setCurr_User}}>
    <div className="app-container">
    <Router>
      <Header />
      <div className="content-container">
      <Routes>
        <Route path="/" index element={<Home />} />
        <Route path="/login" element={<ProcessUser />} />
      </Routes>
      </div>
    </Router>
    </div>
    </Context.Provider>
  )
}

export default App
