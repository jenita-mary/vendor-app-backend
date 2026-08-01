import { useState } from "react";

function Login({onLoginSuccess}) {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");


    async function handleLogin() {

        const response = await fetch(
            "http://127.0.0.1:8000/api/token/",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json",
                },

                body: JSON.stringify({
                    username: username,
                    password: password,
                }),
            }
        );

        const data = await response.json();

        if (response.ok) {
            onLoginSuccess(data.access,data.refresh);
        } else {
            alert("Invalid username or password");
        }
     
    }

    return (
        <>
            <h2>Vendor Login</h2>

            <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(event) => {
                    setUsername(event.target.value);
                }}
            />

            <br /><br />

            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(event) => {
                    setPassword(event.target.value);
                }}
            />

            <br /><br />

            <button onClick = {handleLogin}>
                Login
            </button>

            <p>{username}</p>
            <p>{password}</p>

        </>
    );
}

export default Login;