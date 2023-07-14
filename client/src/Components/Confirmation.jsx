import React, { useContext } from "react";
import { useNavigate } from "react-router-dom";
import { Button, Container, Row, Col } from "react-bootstrap";
import Context from "./Context";

function Confirmation() {
  const { user } = useContext(Context);
  const navigate = useNavigate();

  const handleYes = () => {
    fetch(`/api/checkout`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        if (response.ok) {
          navigate("/profile");
        } else {
          throw new Error("Error confirming the order");
        }
      })
      .catch((error) => {
        console.error(error);
      });
  };

  const handleNo = () => {
    navigate("/cart");
  };

  return (
    <Container>
      <Row>
        <Col>
          <h2>Confirm Order?</h2>
          <Button variant="success" onClick={handleYes}>
            Yes
          </Button>{" "}
          <Button variant="danger" onClick={handleNo}>
            No
          </Button>
        </Col>
      </Row>
    </Container>
  );
}

export default Confirmation;