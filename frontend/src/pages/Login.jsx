import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import "../App.css";
import { useNavigate } from "react-router-dom";

const Login = () => {
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

  return (
    <div className="registerMain">
      <div className="registerContainer">
        <h1>── Login ──</h1>

        <form action="" onSubmit={handleSubmit}>
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
            Login
          </Button>
        </form>
      </div>
    </div>
  );
};

export default Login;
