
import "./App.css";
import { useState, useEffect } from "react";
import Navbar from "./components/Navbar";
import Login from "./components/Login";
import Dashboard from "./components/Dashboard";

function App() {

   useEffect(() => {const savedToken = localStorage.getItem("token")
        if (savedToken) {
        setToken(savedToken);
        setIsLoggedIn(true);
    }

    }, []);  
  const [isLoggedIn, setIsLoggedIn] = useState(false);    
  const [token, setToken] = useState("");

function handleLoginSuccess(accessToken, refreshToken) {
    localStorage.setItem("accessToken", accessToken);
    localStorage.setItem("refreshToken", refreshToken);
    setToken(accessToken);
    setIsLoggedIn(true);
  }

  function handleLogOut() {
    localStorage.removeItem("token")
    setToken("");
    setIsLoggedIn(false);

  }
  

  return (
        <>
            <Navbar
                isLoggedIn={isLoggedIn}
                onLogout={handleLogOut}
            />

            {isLoggedIn ? (
                <Dashboard />
            ) : (
                <Login
                    onLoginSuccess={handleLoginSuccess}
                />
            )}
        </>
  )
}

export default App
