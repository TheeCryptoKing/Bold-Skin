import React, { useState, useEffect, useContext } from "react";
import Context from "../Context.jsx";
import { Container, Table, Row, Col, Button } from "react-bootstrap";
import { Link, useNavigate} from "react-router-dom";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";
import AddressForm from "../addressForm.jsx";
import UserPaymentFrom from "../paymentForm.jsx";

function ProfileDetails() {
  const { user, setUser } = useContext(Context);
  const navigate = useNavigate();
  const [orders, setOrders] = useState([]);
  const [showConfirmation, setShowConfirmation] = useState(false);
  const [showAccountEdit, setAccountEdit] = useState(false);

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

// const handleLogout = () => {
//   if (user) {
//   fetch('/api/logout', {
//     method: 'POST',
//     credentials: 'include',
//   })
//     .then(response => response.json())
//     .then(data => {
//       setUser(null);
//       navigate("/");
//     })
//     navigate("/login")
// };
// }

  const handleDeleteConfirmation = () => {
    setShowConfirmation(true);
  };

  const handleAccountEdit = () => {
    setAccountEdit((prev) => !prev);
  };

  const handleNo = () => {
    setShowConfirmation(false);
  };

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
          <Link to={`/order/${order.order_id}`}>View Details</Link>
        </td>
      </tr>
    );
  });

  return (
    <Container >
    {/* <Button className="text-align" onClick={handleLogout}>Logout</Button> */}
      <Row className="center">
          <h3>Welcome</h3>
          <h3>Hello,{user.name}</h3>
          <h3>{user.username}</h3>
          <h3>{user.email}</h3>
        <p>
            View your order history and update personal Your details.
            Let us know any way we can assist you!
        </p>
        {showAccountEdit ? (
          <>
            <Formik
              initialValues={{ email: user.email, password: "" }}
              validationSchema={validationSchema}
              onSubmit={(values) => {
                fetch("/api/users", {
                  method: "PATCH",
                  headers: {
                    "Content-Type": "application/json",
                  },
                  body: JSON.stringify({
                    email: values.email,
                    password: values.password,
                  }),
                })
                  .then((response) => {
                    if (response.ok) {
                    } else {
                      throw new Error("Error updating email and password");
                    }
                  })
                  .catch((error) => {
                    console.error(error);
                  });
              }}
            >
              <Form>
                <h4>Edit Email and Password</h4>
                <hr />
                <div className="form-group">
                  <label htmlFor="email" className="form-label">
                    Email:
                  </label>
                  <Field
                    type="email"
                    id="email"
                    name="email"
                    className="edit-form"
                  />
                  <ErrorMessage
                    name="email"
                    component="div"
                    className="error-message"
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="password" className="form-label">
                    Password:
                  </label>
                  <Field
                    type="password"
                    id="password"
                    name="password"
                    className="edit-form"
                  />
                  <ErrorMessage
                    name="password"
                    component="div"
                    className="error-message"
                  />
                </div>
                <Button type="submit" className="custom-btn-primary">
                  Update
                </Button>
                <Button variant="danger" onClick={handleAccountEdit}>
                  Cancel
                </Button>
              </Form>
            </Formik>
          </>
        ) : (
          <p>
            Need to Provide or edit your account details?{" "}
            <span onClick={handleAccountEdit} className="edit-click">
              Click Here
            </span>
          </p>
        )}
      </Row>
      <Row>
        <h4>Payment Details</h4>
        <hr />
        <UserPaymentFrom />
      </Row>
      <Row>
        <h4>Addresses</h4>
        <hr />
        <AddressForm />
      </Row>
      <Row>
        <h3>Order History</h3>
        <hr />
        <Table>
          <thead>
            <tr>
              <th>Order #</th>
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
      </Row>
      {/* <Row className="center ">
        <h3>Now longer a Fan of BoldSKin?</h3>
        <hr />
        {showConfirmation ? (
          <>
            <p>Are you sure you want to delete your account?</p>
            <Button
              className=""
              variant="success"
              onClick={handleYes}
            >
              Yes
            </Button>
            <Button className="" variant="danger" onClick={handleNo}>
              No
            </Button>
          </>
        ) : (
          <Button
            className=""
            onClick={handleDeleteConfirmation}
          >
            Delete Account
          </Button>
        )}
      </Row> */}
    </Container>
  );
}

export default ProfileDetails;