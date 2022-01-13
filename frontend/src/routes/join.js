import React, { useEffect } from 'react';

function Join(){
    const [userEmail, setUserEmail] = React.useState();
    const [userPassword, setUserPassword] = React.useState();
    const [userName, setUserName] = React.useState();
    const [userPhoneNumber, setUserPhoneNumber] = React.useState();
    const [userBirthday, setUserBirthday] = React.useState();
    const [userGender, setUserGender] = React.useState();
    const [userNickname, setUserNickname] = React.useState();
    const [userProfileImage, setUserProfileImage] = React.useState();

    const handleUserEmail = (event) => {
        setUserEmail(event.target.value)
    }
    
    const handleUserPassword = (event) => {
        setUserPassword(event.target.value)
    }

    const handleUserName = (event) => {
        setUserName(event.target.value)
    }

    const handleUserPhoneNumber = (event) => {
        setUserPhoneNumber(event.target.value)
    }

    const handleUserBirthday = (event) => {
        setUserBirthday(event.target.value)
    }

    const handleUserGender = (event) => {
        setUserGender(event.target.value)
    }
    
    const handleUserNickname = (event) => {
        setUserNickname(event.target.value)
    }

    const handleUserProfileImage = (event) => {
        setUserProfileImage(event.target.value)
    }

    return(
        <div>
            <h2>Join</h2>
            <div>
                <label htmlFor="userEmail">Email : </label>
                <input type="email" id="userEmail" value={userEmail} onChange={handleUserEmail}/>
            </div>
            <div>
                <label htmlFor="userPassword">Password : </label>
                <input type="password" id="userPassword" value={userPassword} onChange={handleUserPassword} />
            </div>
            <div>
                <label htmlFor="userName">Name : </label>
                <input type="text" id="userName" value={userName} onChange={handleUserName} />
            </div>
            <div>
                <label htmlFor="userPhoneNumber">Phone Number : </label>
                <input type="text" id="userPhoneNumber" value={userPhoneNumber} onChange={handleUserPhoneNumber} />
            </div>
            <div>
                <label htmlFor="userBirthday">Birthday : </label>
                <input type="date" id="userBirthday" value={userBirthday} onChange={handleUserBirthday} />
            </div>
            <div>
                <label htmlFor="user">Gender : </label>
                <select value={userGender} onChange={handleUserGender}>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                </select>
            </div>
            <div>
                <label htmlFor="userNickname">Nickname : </label>
                <input type="text" id="userNickname" value={userNickname} onChange={handleUserNickname} />
            </div>
            <div>
                <label htmlFor="userProfileImage">Profile Image : </label>
                <input type="text" id="userProfileImage" value={userProfileImage} onChange={handleUserProfileImage} />
            </div>
        </div>
    );
}

export default Join;