import React, { useState } from "react";
import { Container } from "react-bootstrap";
import PaymentDetails from "../PaymentAtCheckout";
import AddressForm from "../addressForm";
import Confirmation from "../Confirmation";

function Checkout() {
  const [currentStep, setCurrentStep] = useState("payment");
  console.log(currentStep)
  const handlePaymentNext = () => {
    setCurrentStep("address");
  };
// Passed down as props from onNext() post 
  const handleAddressNext = () => {
    setCurrentStep("confirm");
  };

  return (
    <Container>
      {currentStep === "payment" && (
        <PaymentDetails onNext={handlePaymentNext} />
      )}
      {/* {currentStep === "address" && (
        <AddressForm onNext={handleAddressNext} />
      )}
      {currentStep === "confirm" && <Confirmation />} */}
    </Container>
  );
}

export default Checkout;