import React, { useEffect } from 'react';
import axios from 'axios';

function Login(){
    const [userEmail, setUserEmail] = React.useState();
    const [userPassword, setUserPassword] = React.useState();
    

    const handleUserEmail = (event) => {
        setUserEmail(event.target.value)
    }
    
    const handleUserPassword = (event) => {
        setUserPassword(event.target.value)
    }
    
    return(
        <div>
            <h2>Login</h2>
            <div>
                <label htmlFor="userEmail">Email : </label>
                <input type="text" id="userEmail" value={userEmail} onChange={handleUserEmail}/>
            </div>
            <div>
                <label htmlFor="userPassword">Password : </label>
                <input type="password" id="userPassword" value={userPassword} onChange={handleUserPassword} />
            </div>
        </div>
    );
}

export default Login;