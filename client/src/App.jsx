import { useState, useEffect } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
// import './Components/Header.jsx'
import Home from './Components/pages/Home.jsx'
import Shop from './Components/pages/Shop.jsx'
// import ShopByCategory from './Components/pages/ShopByCategory'
import Cart from './Components/pages/Cart.jsx'
import Product from './Components/pages/Products.jsx'
import Header from './Components/Header.jsx'
import Footer from './Components/Footer.jsx'
import ProfileDetails from './Components/pages/Userprofile.jsx'
import ProcessUser from './Components/pages/Login-Signup.jsx'
import Context from './Components/Context.jsx'
import 'bootstrap/dist/css/bootstrap.css';
import './stylesheet/index.css'


function App() {
const [user, setUser] = useState(null)

useEffect(() => {
  if(user == null) {
    fetch('/api/check_session')
    .then(res => {
      if (res.ok) {
        res.json().then(user => {setUser(user)})
      }
    })
  }
},[])

  return (
    <Context.Provider value={{user, setUser}}>
    <div className="app-container ">
    <Router>
      <Header />
      <div className="content-container">
      <Routes>
        <Route path="/" index element={<Home />} />
        <Route path="/login" element={<ProcessUser />} />
        <Route path="/profile" element={<ProfileDetails />} />
        <Route path="/product/:id" element={<Product />}/>
        <Route path='/shop' element={<Shop />}/>
        {/* <Route path='/shop/:id' element={<ShopBycategory />}/> */}
        <Route path='/cart' element={<Cart />}/>
      </Routes>
      </div>
      <Footer />
    </Router>
    </div>
    </Context.Provider>
  )
}

export default App
