import React, { useContext, useEffect, useState } from "react";
import Context from '../Context.jsx'
import Login from '../login.jsx'
import Signup from '../signup.jsx'
import { Link } from "react-router-dom";
import { Row, Col, Container, Button, Image } from "react-bootstrap";


// Header, Footer, 2 buttons open forms and when pressed, open Login form or Signup form

function ProcessUser(){
    const[showLoginForm, setShowLoginForm] = useState(false)
    const[showSignupForm, setShowSignupForm] = useState(false)

    const handleLoginClick = () => {
        // setShowLoginForm(true);
        // setShowSignupForm(false);
        setShowLoginForm(!showLoginForm)
    };
    
    const handleSignupClick = () => {
        // setShowLoginForm(false);
        // setShowSignupForm(true);
        setShowSignupForm(!showSignupForm)
    };
    
// WIll use when cancel button functional
// return (
//     <Container>
//         <Row className="justify-content-center mt-4">
//         <Col md={6}>
//             {!showLoginForm && !showSignupForm && (
//                 <div>
//                 <h3 onClick={handleLoginClick} style={{ cursor: "pointer" }}>
//                     Login
//                 </h3>
//                 <h3 onClick={handleSignupClick} style={{ cursor: "pointer" }}>
//                     Signup
//                 </h3>
//                 </div>
//             )}
//             {showLoginForm && <Login />}
//             {showSignupForm && <Signup />}
//         </Col>
//         </Row>
//     </Container>
//     )
// }
return (
    <Container>
      <Col className="justify-content-center mt-4">
        <Row md={6}>
          <h3 onClick={handleLoginClick} style={{ cursor: "pointer" }}>
            Login
          </h3>
          {showLoginForm && <Login />}
          <h3 onClick={handleSignupClick} style={{ cursor: "pointer" }}>
            Signup
          </h3>
          {showSignupForm && <Signup />}
        </Row>
      </Col>
    </Container>
  );
}

export default ProcessUser
