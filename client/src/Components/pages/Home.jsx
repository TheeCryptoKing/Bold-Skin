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
    const [isLoading, setLoading] = useState(true);
    useEffect(() => {
        setTimeout(() => {
            setLoading(false);
        }, 2000);
        }, []);



    return (
        <div>
        {/* {isLoading ? (
        <div className="center full-height">
            <h1 className="loading">
            <span class="let1">l</span>  
            <span class="let2">o</span>  
            <span class="let3">a</span>  
            <span class="let4">d</span>  
            <span class="let5">i</span>  
            <span class="let6">n</span>  
            <span class="let7">g</span>  
            </h1>
        </div>
        ) : ( */}
          <>
            <div className="jumbotron">
              <Container>
                <h1 className="pacifico-bold">Let's save the world together, United.</h1>
                <h3 className="pacifico-reg top-spacing">
                  Conscious, Ethical shopping that helps you look good and helps the planet feel good.
                </h3>
              </Container>
            </div>
            <Container>
              <div>
                <Container>
                  <div className="center onyx-reg">
                    <h1>
                      Made with sustainability,
                      <br />
                      and Inclusion for all types of Men <br />
                      in Mind.
                      <br />
                      <Button className="shop-button" onClick={handleShop}>
                        Shop
                      </Button>
                    </h1>
                  </div>
                </Container>
              </div>
            </Container>
          </>
        {/* )} */}
      </div>
    );
  };

export default Home;