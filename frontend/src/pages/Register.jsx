import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import "../App.css";
import { useNavigate } from "react-router-dom";

const Register = () => {
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();
  const [fullName, setFullName] = useState();
  const navigate = useNavigate();

  const handleSubmit = (e) => {};

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
myHeaders.append("Cookie", "csrftoken=fxnbwEZG2lycC2WzF1QTfDFOvRvd80pp3IQaV6lUG31jfzi342LdfaNSc41ZLxRw");

var raw = "";

// var requestOptions = {
//   method: 'POST',
//   headers: myHeaders,
//   body: raw,
//   redirect: 'follow'
// };

// const fetcFunc=()=>fetch("http://127.0.0.1:8000/register/", requestOptions)
//   .then(response => response.text())
//   .then(result => console.log(result))
//   .catch(error => console.log('error', error));
//   fetcFunc()
  return (
    <div className="registerMain">
      <div className="registerContainer">
        <h1>── Register ──</h1>

        <form action="" onSubmit={handleSubmit}>
          <TextField
            sx={style}
            name="first_name"
            required
            id="outlined-required"
            label="First Name"
            defaultValue=""
            onChange={(e) => setFullName(e.target.value)}
          />
          <TextField
            sx={style}
            name="last_name"
            required
            id="outlined-required"
            label="Last Name"
            defaultValue=""
            onChange={(e) => setFullName(e.target.value)}
          />

          <TextField
            sx={style}
            name="email"
            required
            id="outlined-required"
            label="Email"
            defaultValue=""
            onChange={(e) => setEmail(e.target.value)}
          />
          <TextField
            sx={style}
            name="password"
            required
            id="outlined-password-input"
            label="Password"
            type="password"
            autoComplete="current-password"
            onChange={(e) => setPassword(e.target.value)}
          />

          <Button variant="contained" type="submit" className="registerButton">
            Register
          </Button>
        </form>
      </div>
    </div>
  );
};

export default Register;
