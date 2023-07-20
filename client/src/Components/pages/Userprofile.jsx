import React, { useState, useEffect, useContext } from "react";
import Context from "../Context.jsx";
import { Container, Table, Row, Col, Button, Modal } from "react-bootstrap";
import { Link, useNavigate, useParams } from "react-router-dom";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";
// import OrderById from "./OrderbyId"


function ProfileDetails() {
  const { user, setUser } = useContext(Context);
  const navigate = useNavigate();
  const [orders, setOrders] = useState([]);
  const [showModal, setModalShow] = useState([])
  const [selectedOrder, setSelectedOrder] = useState(null); 

  const validationSchema = Yup.object().shape({
    email: Yup.string().email("Invalid email").required("Email is required"),
    password: Yup.string().required("Password is required"),
  });

  useEffect(() => {
    fetch("/api/user/orders")
      .then((r) => r.json())
      .then((orders) => {
        setOrders(orders);
      })
      .catch((error) => {
        console.error(error);
      });
  }, [user]);

  if (!user) {
    return navigate("/login");
  }
  
  const handleEditProfile = () => {
    navigate("/editprofile");
  };


const handleYes = () => {
  fetch(`/api/users`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      if (response.ok) {
        setUser(null);
        navigate("/");
      } else {
        throw new Error("Error confirming the order");
      }
    })
    .catch((error) => {
      console.error(error);
    });
};

const handleLogout = () => {
  if (user) {
  fetch('/api/logout', {
    method: 'POST',
    credentials: 'include',
  })
    .then(response => response.json())
    .then(data => {
      setUser(null);
      navigate("/");
    })
    navigate("/login")
};
}

// const handleModalShow = () => {
//   setModalShow(true);
// };

// const handleModalClose = () => {
//   setModalShow(false);
// };

// const handleOrderClick = (order) => {
//   setSelectedOrder(order); 
//   handleModalShow();
// }

  const orderData = orders.map((order) => {
    const date = new Date(order.created);
    const formattedDate = date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });

    return (
      <tr key={order.order_id}>
        <td>{order.order_id}</td>
        <td>{formattedDate}</td>
        <td>${order.order_total}</td>
        <td>{order.status}</td>
        <td>
          <Button className="edit-profile-button"><Link to={`/order/${order.order_id}`}>View Details</Link></Button>
        </td>
      </tr>
    );
  });
// row = 12 col | col md={2} takes up 2 rows

  return (
    <div>
      <Container >
        <Row className="user-info">
        <Col>
          <h1>Welcome,</h1>
            <h3>Username: {user.username}</h3>
            <h4>Email: {user.email}</h4>
            <h3>Name: {user.name}</h3>
            
          <p className="title-text">
              View your order history and update personal details.
              Let us know any way we can assist you!
          </p>
          <Button className="edit-profile-button" onClick={handleLogout}>Logout</Button>
          </Col>
          <Col>
          <Button className="profile-button" onClick={handleEditProfile}>
          Edit Profile Details
          </Button>
          </Col>
        <div className="order-history">
        <hr />
          <h3>Order History</h3>
          <hr />
          <Table>
            <thead>
              <tr>
                <th>Confirmation Num.</th>
                <th>Order Date</th>
                <th>Total</th>
                <th>Order Status</th>
                <th></th>
              </tr>
            </thead>
            {orders && orders.length > 0 ? (
              <tbody>{orderData}</tbody>
            ) : (
              <tbody>
                <tr>
                  <td colSpan="5">No orders found</td>
                </tr>
              </tbody>
            )}
          </Table>
          </div>
        </Row>
      {/* {orders.map((order) => (
        <div key={order.order_id}>
          <p>Order ID: {order.order_id}</p>
          <Button onClick={() => handleOrderClick(order)}>View Order</Button>
        </div>
      ))}

      <Modal show={showModal} onHide={handleModalClose}>
        <Modal.Header closeButton>
          <Modal.Title>Order Details</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {selectedOrder && <OrderById order={selectedOrder} />}
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleModalClose}>
            Close
          </Button>
        </Modal.Footer>
      </Modal> */}
      </Container>
    <div className="review-section">
      <h3>Reviews</h3>
      <hr />
      <Table>
            <tr >
              <th> No current Reviews </th>
            </tr>
        </Table>
        <hr />
      </div>

    </div>
  );
}

export default ProfileDetails;