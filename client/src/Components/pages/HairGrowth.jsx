import React, { useContext, useEffect, useState } from "react";


function HairGrowth() {
    const[hairGrowth, setHairGrowth] = useState()

    useEffect(() => {
        fetch("/api/products")
          .then((response) => response.json())
          .then((data) => {
            setHairGrowth(data);
          })
          .catch((error) => {
            console.error("Error fetching Hair growth oil:", error);
          });
      }, []);
  return (
    <div>HairGrowth</div>
  )
}

export default HairGrowth