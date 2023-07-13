import React, { useContext, useEffect, useState } from "react";
import Context from '../Context.jsx'
import { Container, Row, Col, Card, Button } from "react-bootstrap";
import { Link, useNavigate } from "react-router-dom";
import { FaDatabase, FaClipboardList, FaHeart } from "react-icons/fa";


const Home = () => {
    const navigate = useNavigate();
    const handleShop = () => {
        navigate("/shop"); 
    };


    const { user } = useContext(Context);
    return (
        <div >
            <div className="jumbotron">
                <Container >
                    <h1 className="pacifico-bold"
                    >
                    Let's save the world together, United.
                    </h1>
                    <h4 className="pacifico-reg top-spacing">
                    Concious, Ethical shopping that helps you look good and helps the planet feel good.
                    </h4>
                </Container>
            </div>
            <Container>
            <div>
                <Container >
                    <div className="center onyx-reg">
                        <h1>
                            Made with sustainablitiy, <br/>
                            and Inclusion for all types of Men <br></br>
                             in Mind.<br/>
                            {/* Fix reload */}
                            <Button href='#' onClick={handleShop}> Shop</Button>
                        </h1>
                    </div>
                </Container>
            </div>
            </Container>
            <Container>
                <div>
                    
                </div>
            </Container>
        </div>

    );
};

export default Home;