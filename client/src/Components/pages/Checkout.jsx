import React, { useState } from "react";
import { Container } from "react-bootstrap";
import PaymentCheckout from "../PaymentAtCheckout";
import AddressCheckout from "../AddressAtCheckout";
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
                <PaymentCheckout onNext={handlePaymentNext} />
            )}
            {currentStep === "address" && (
                <AddressCheckout onNext={handleAddressNext} />
            )}
            {currentStep === "confirm" && <Confirmation />} 
        </Container>
    );
}

export default Checkout;