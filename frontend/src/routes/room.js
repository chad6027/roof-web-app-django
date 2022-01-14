import axios from 'axios';
import React, { useState, useEffect } from 'react';

function Room(){

    useEffect(() => {
        axios.get('http://localhost:8000/users/')
            .then(res => {
                console.log("success");
            }).catch(error => {
                console.log(error);
            })
    });

    return(
        <>

        </>
    )
}

export default Room;