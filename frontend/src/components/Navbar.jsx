import { useState } from "react";
import Button from "@mui/material/Button";
import Menu from "@mui/material/Menu";
import MenuItem from "@mui/material/MenuItem";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import "../App.css";
import { Link } from "react-router-dom";

export default function Navbar() {
  const [anchorEl, setAnchorEl] = useState(null);
  const open = Boolean(anchorEl);
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <header className="navbar">
      <Link to={"/"}>
        <img
          src="https://github.com/Sule-Ss/firebase-blog-app/blob/master/src/assests/home.png?raw=true"
          alt="home-icon"
        />
      </Link>
      <h1>
        ──── <span> {"<Betül/>"}</span> Create Url ────
      </h1>

      <Button
        id="basic-button"
        aria-controls={open ? "basic-menu" : undefined}
        aria-haspopup="true"
        aria-expanded={open ? "true" : undefined}
        onClick={handleClick}
      >
        <h3>user name</h3>
        <AccountCircleIcon className="navbarButton" />
      </Button>

      <Menu
        id="basic-menu"
        anchorEl={anchorEl}
        open={open}
        onClose={handleClose}
        MenuListProps={{
          "aria-labelledby": "basic-button",
        }}
      >
        <div>
          <Link to={"/"} className="link">
            <MenuItem onClick={handleClose && "logout"}>Logout</MenuItem>
          </Link>
        </div>

        <div>
          <Link to={"/login"} className="link">
            <MenuItem onClick={handleClose}>Login</MenuItem>
          </Link>
          <Link to={"/register"} className="link">
            <MenuItem onClick={handleClose}>Register</MenuItem>
          </Link>
        </div>
      </Menu>
    </header>
  );
}
