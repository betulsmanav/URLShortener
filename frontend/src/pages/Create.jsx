import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import "../App.css";
import { useNavigate } from "react-router-dom";

const Create = () => {
  const [url, setUrl] = useState();

  const navigate = useNavigate();


  const handleProviderRegister = () => {};

  const style = {
    "& label.Mui-focused": {
      color: "#e84224",
    },
    "& .MuiOutlinedInput-root": {
      "&.Mui-focused fieldset": {
        borderColor: "#ef6f59",
      },
    },
  };


  var myHeaders = new Headers();
    myHeaders.append("Authorization", "Token 8a9a0aa76eec29e72aac42c8b9f48362e10aa93e");
  myHeaders.append("Cookie", "csrftoken=JXxZlDDGmQgOPWBkXdvRLeeWsW8DNNAucD30jRmNyoMejyGPW9mjDvww1JboVgx5; sessionid=f8il3qccfu3pghc5z8iexovkkaalikb8"
  );

  var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    redirect: 'follow'
  };

  const fetchFunc=()=>fetch("http://127.0.0.1:8000/urls/", requestOptions)
    .then(response => response.json())
    .then(result => {
      console.log(result)
      setUrl(result)
    })
    .catch(error => console.log('error', error));
    // fetchFunc()
  
  const handleSubmit = (e) => { 
    e.preventDefault()
    console.log(url)
  };
  




  return (
    <div className="registerMain">
      <div className="registerContainer">
        <h1>── Url Create ──</h1>

        <form action="" onSubmit={handleSubmit}>
          <TextField
            sx={style}
            name="url"
            required
            // id="outlined-password-input"
            label="Url"
            type="url"
            autoComplete=""
            // onChange={(e) => setPassword(e.target.value)}
          />

          <Button variant="contained" type="submit" className="registerButton">
            Conversion
          </Button>
        </form>
      </div>
    </div>
  );
};

export default Create;
