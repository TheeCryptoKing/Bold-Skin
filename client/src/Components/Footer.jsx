import React from 'react';
import {
    MDBFooter,
    MDBContainer,
    MDBIcon,
    MDBInput,
    MDBCol,
    MDBRow,
    MDBBtn
} from 'mdb-react-ui-kit';
import {
    FaTwitter,
    FaInstagram,
    FaLinkedin,
    FaGithub,
    FaGoogle,
    FaDiscord,
    } from "react-icons/fa";
import { BsFacebook } from "react-icons/bs";

export default function App() {
    return (
        <MDBFooter className='text-center' color='white' style={{ backgroundColor: '#caced1' }}>
        <MDBContainer className='p-4'>
            <section className='mb-4'>
            <MDBBtn outline color="light" floating className='m-1' href='#!' role='button'>
                <BsFacebook fab icon='facebook-f' />
            </MDBBtn>

            <MDBBtn outline color="light" floating className='m-1' href='#!' role='button'>
                <FaTwitter fab icon='twitter' />
            </MDBBtn>

            <MDBBtn outline color="light" floating className='m-1' href='#!' role='button'>
                <FaGoogle fab icon='google' />
            </MDBBtn>

            <MDBBtn outline color="light" floating className='m-1' href='#!' role='button'>
                <FaInstagram fab icon='instagram' />
            </MDBBtn>

            <MDBBtn outline color="light" floating className='m-1' href='#!' role='button'>
                <FaLinkedin fab icon='linkedin-in' />
            </MDBBtn>

            <MDBBtn outline color="light" floating className='m-1' href='#!' role='button'>
                <FaGithub fab icon='github' />
            </MDBBtn>
            </section>

            <section className=''>
            <form action=''>
                <MDBRow className='d-flex justify-content-center'>
                </MDBRow>
            </form>
            </section>

            <section className='mb-4'>
            <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt distinctio earum repellat quaerat
                voluptatibus placeat nam, commodi optio pariatur est quia magnam eum harum corrupti dicta, aliquam
                sequi voluptate quas.
            </p>
            </section>

            {/* <section className=''>
            <MDBRow>
                <MDBCol lg='3' md='6' className='mb-4 mb-md-0'>
                <h5 className='text-uppercase'>Links</h5>

                <ul className='list-unstyled mb-0'>
                    <li>
                    <a href='#!' className='text-white'>
                        Link 1
                    </a>
                    </li>
                </ul>
                </MDBCol>

                <MDBCol lg='3' md='6' className='mb-4 mb-md-0'>
                <h5 className='text-uppercase'>Links</h5>

                <ul className='list-unstyled mb-0'>
                    <li>
                    <a href='#!' className='text-white'>
                        Link 1
                    </a>
                    </li>
                </ul>
                </MDBCol>

                <MDBCol lg='3' md='6' className='mb-4 mb-md-0'>
                <h5 className='text-uppercase'>Links</h5>

                <ul className='list-unstyled mb-0'>
                    <li>
                    <a href='#!' className='text-white'>
                        Link 1
                    </a>
                    </li>
                </ul>
                </MDBCol>

                <MDBCol lg='3' md='6' className='mb-4 mb-md-0'>
                <h5 className='text-uppercase'>Links</h5>

                <ul className='list-unstyled mb-0'>
                    <li>
                    <a href='#!' className='text-white'>
                        Link 1
                    </a>
                    </li>
                </ul>
                </MDBCol>
            </MDBRow>
            </section> */}
        </MDBContainer>

        <div className='text-center p-3' style={{ backgroundColor: 'rgba(0, 0, 0, 0.2)' }}>
            <p> © 2020 Copyright &nbsp; : &ensp;
            <a className='text-white' href='https://BoldSkinInc.com/'>
            BoldSkinInc.com
            </a>
            </p>
        </div>
        </MDBFooter>
        // <MDBFooter className='text-center text-white' style={{ backgroundColor: '#21081a' }}>
        //     <MDBContainer className='p-4'></MDBContainer>
    
        //     <div className='text-center p-3' style={{ backgroundColor: 'rgba(0, 0, 0, 0.2)' }}>
        //     © 2020 Copyright:
        //     <a className='text-white' href='https://mdbootstrap.com/'>
        //         MDBootstrap.com
        //     </a>
        //     </div>
        // </MDBFooter>
    );
}