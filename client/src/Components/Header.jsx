import React, { useContext, useEffect, useState } from "react";
import { CgUser, CgProfile } from "react-icons/cg";
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
// import { CgUser } from "react-icons/cg";
import {FaJenkins, FaCcDiscover, FaFolderOpen, FaHandHoldingUsd, FaEdit} from "react-icons/fa";
import {FaOpencart} from "react-icons/fa6"
// , FaShoppingCart, FaCartShopping, FaRegUser
import {TfiUser} from "react-icons/tfi";
import { Link, useNavigate} from "react-router-dom";


function Header() {
  const navigate = useNavigate();
  const handleProfile = () => {
    navigate("/profile"); 
  };

  const handleCart = () => {
    navigate("/cart")
  }
  // const handleModal = () => {
  //   pass
  // }


    return (
      <Navbar expand="lg" className="sticky-nav">
        <Container fluid>
          <Navbar.Brand href="/">
          <img 
            className="brandLogo"
            alt="Bold Skin"
            src="https://raw.githubusercontent.com/TheeCryptoKing/Bold-Skin/main/assets/Products/BoldSkin/BoldSkinLogo.png"
            width= "175px"
            height="125px"
          />
          </Navbar.Brand>
          {/* <Navbar.Toggle aria-controls="navbarScroll" /> */}
          <Navbar.Collapse id="navbarScroll">
            <Nav
              className="me-auto my-2 my-lg-0"
              style={{ maxHeight: '100px' }}
              navbarScroll
            >
              {/* <Nav.Link href="#action1"></Nav.Link>
              <Nav.Link href="#action2">Link</Nav.Link>
              <Nav.Link href="#action1">Home</Nav.Link>
              <Nav.Link href="#action1">Hair Growth</Nav.Link> */}
              {/* <NavDropdown title="Link" id="navbarScrollingDropdown">
                <NavDropdown.Item href="#action3">Action</NavDropdown.Item>
                {/* <NavDropdown.Item href="#action4">
                  Another action
                </NavDropdown.Item>
                <NavDropdown.Divider />
                {/* <NavDropdown.Item href="#action5">
                  Something else here
                </NavDropdown.Item> */}
              {/* </NavDropdown>  */} 
              {/* <Nav.Link href="#" disabled>
                Profile
              </Nav.Link> */}
              {/* right side modal */}
            </Nav>
            {/* <Form className="d-flex">
              <Form.Control
                type="search"
                placeholder="Search"
                className="me-2"
                aria-label="Search"
              />
              <Button variant="outline-success">Search</Button>
            </Form> */}
            {/* <Nav.Link href="#action2"><CgProfile/></Nav.Link> */}
            <ul className="icon-center">
              <Nav.Link href="#" onClick={handleProfile}><TfiUser className="feature-icon" /></Nav.Link>
              <Nav.Link href="#" onClick={handleCart}><FaOpencart className="feature-icon"/></Nav.Link>
              <Nav.Link href="#action2"><FaFolderOpen className="feature-icon"/></Nav.Link>
            </ul>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    );
  }
  
  export default Header;