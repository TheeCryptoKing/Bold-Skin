// import React, { useState, useEffect, useContext } from "react";
// import { Card, Pagination, Button} from "react-bootstrap";
// import Accordion from 'react-bootstrap/Accordion';
// import Context from "./Context";

// function ReviewContainer({ reviews }) {
// const { user } = useContext(Context);
//   const [currentPage, setCurrentPage] = useState(1);
//   const reviewsPerPage = 9;
// //   const [reviewDetails, setReviewDetails] = useState([])
// //   const [selectedReviewId, setSelectedReviewID] = useState(null)

//   // Calculate the index of the first and last review on the current page
//   const indexOfLastReview = currentPage * reviewsPerPage;
//   const indexOfFirstReview = indexOfLastReview - reviewsPerPage;
//   const currentReviews = reviews.slice(indexOfFirstReview, indexOfLastReview);

//   const paginate = (pageNumber) => {
//     setCurrentPage(pageNumber);
//   };

//   const reviewsList = currentReviews.map((review) => {
//     console.log(review);
//     const date = new Date(review.created_at);
//     const formattedDate = date.toLocaleDateString("en-US", {
//       year: "numeric",
//       month: "long",
//       day: "numeric",
//     });
//     // NOt sure if route will work unsure how to grab reviewid, might have to mak route
//     // either grabbing user or review id
//     // useEffect(() => {
//     //     fetch(`/api/reviews/${review.id}`)
//     //     .then((r) => {
//     //         if(r.ok) {
//     //             return r.json();
//     //         }   else if (r.status === 404) {
//     //             return [];
//     //         }   else {
//     //             throw new Error("Eror fetching review data")
//     //         }
//     //     })
//     //     .then((reviews) => {
//     //         setReviewDetails(reviews);
//     //         console.log(reviews)
//     //     })
//     //     .catch((error) => {
//     //         console.error(error);
//     //     });
//     // }, [review]);



// //     const handleDelete = () => {
// //     useEffect(() => {
// //         fetch(`/api/reviews/review/${selectedReviewId}`)
// //         method: "DELETE",
// //         })
// //         .then((r) => {
// //             if(r.ok) {

// //             }
// //         })
    
// //     }), [id]
// // }

//     return (
//       <Card className="row review-card " key={review.review_id}>
//         <Card.Body>

//           <Card.Title>{review.users_name.toUpperCase()}</Card.Title>
//           <Card.Text><b>Created:</b><br/>  {formattedDate}</Card.Text>
//           {/* <Card.Subtitle>Rating: {review.rating}</Card.Subtitle> */}
//           <Card.Text><b>User Review:</b><br/> {review.review_text} </Card.Text>

//         </Card.Body>
//       </Card>
//     );
//   });



//   // Calculate the total number of pages
//   const totalPages = Math.ceil(reviews.length / reviewsPerPage);

//   return (
//     <div>
//       <div className="row ">{reviewsList}</div>
//       {totalPages > 1 && (
//         <Pagination>
//           {Array.from({ length: totalPages }).map((_, index) => (
//             <Pagination.Item
//               key={index + 1}
//               active={index + 1 === currentPage}
//               onClick={() => paginate(index + 1)}
//             >
//               {index + 1}
//             </Pagination.Item>
//           ))}

//         </Pagination>
//       )}
//     </div>
//   );
// }

// export default ReviewContainer;