import React, { useContext, useEffect, useState } from "react";
import ProductCard from "../ProductCard.jsx";
import { Row, Col, Container, Button } from "react-bootstrap";


function Shop() {
    const [products, setProducts] = useState([]);
    const [searchQuery, setSearchQuery] = useState("");
    const [filteredProducts, setFilteredProducts] = useState([]);
    const [selectedCategory, setSelectedCategory] = useState("");
    const [selectedPriceRange, setSelectedPriceRange] = useState("");

  // Fetch general product data
    useEffect(() => {
      fetch("/api/products")
        .then((response) => response.json())
        .then((data) => {
          setProducts(data);
          setFilteredProducts(data);
        })
        .catch((error) => {
          console.error("Error fetching products:", error);
        });
    }, []);
  
    // Filter products based on name search update of searchquery
    const filterProducts = () => {
      let filtered = [...products];
  
      if (searchQuery) {
        filtered = filtered.filter((product) =>
          product.name.toLowerCase().includes(searchQuery.toLowerCase())
        );
      }
  
      // filter products by category
      if (selectedCategory) {
        filtered = filtered.filter(
          (product) => product.category.name === selectedCategory
        );
      }
  
  // Seperating products by price 
      // if (selectedPriceRange) {
      //   const [minPrice, maxPrice] = selectedPriceRange.split("-");
      //   filtered = filtered.filter(
      //     (product) =>
      //       product.price >= Number(minPrice) && product.price <= Number(maxPrice)
      //   );
      // }
  // setting state to updated product
      setFilteredProducts(filtered);
    };
  
    // Useeffect when retrieving data on render 
    useEffect(() => {
      filterProducts();
    }, [
      searchQuery,
      selectedCategory,
      selectedPriceRange,
    ]);
  
    const handleCategoryChange = (category) => {
      setSelectedCategory(selectedCategory === category ? "" : category);
    };
  
    const handlePriceRangeChange = (priceRange) => {
      setSelectedPriceRange(selectedPriceRange === priceRange ? "" : priceRange);
    };
  
    return (
      <>
      <Container>
          <Col md={5}>
            <input
              type="text"
              placeholder="Search..."
              onChange={(e) => setSearchQuery(e.target.value)}
              className="form-control mr-2"
            />
            <hr />
            <h5 className="filter-heading">Categories</h5>
            <div className="filter-options">
              <label className="filter-option">
                <input
                  type="checkbox"
                  className="filter-checkbox"
                  checked={selectedCategory === "Hair"}
                  onChange={() => handleCategoryChange("Hair")}
                />
                Hair
              </label>
              {/* <label className="filter-option">
                <input
                  type="checkbox"
                  className="filter-checkbox"
                  checked={selectedCategory === "Beard"}
                  onChange={() => handleCategoryChange("Beard")}
                />
                Beard
              </label>  */}
              <label className="filter-option">
                <input
                  type="checkbox"
                  className="filter-checkbox"
                  checked={selectedCategory === "Body"}
                  onChange={() => handleCategoryChange("Body")}
                />
                Body
              </label> 
              {/* <label className="filter-option">
                <input
                  type="checkbox"
                  className="filter-checkbox"
                  checked={selectedCategory === "Face"}
                  onChange={() => handleCategoryChange("Face")}
                />
                Face
              </label>  */}
              <label className="filter-option">
                <input
                  type="checkbox"
                  className="filter-checkbox"
                  checked={selectedCategory === "Merch"}
                  onChange={() => handleCategoryChange("Merch")}
                />
                Merch 
              </label>
              {/* <label className="filter-option">
                <input
                  type="checkbox"
                  className="filter-checkbox"
                  checked={selectedCategory === "Hair Growth"}
                  onChange={() => handleCategoryChange("Hair Growth")}
                />
                Hair Growth
              </label> */}
            </div>
            <hr />
          </Col>
          <Col md={8}>
            <ProductCard products={filteredProducts}  searchQuery={searchQuery} />
          </Col>
      </Container>
      </>
    );
}
  
export default Shop;