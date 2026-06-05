import API_URL from "../config";

import { useState } from "react"

import axios from "axios"

import { Link, useNavigate } from "react-router-dom"

function Login() {

  const navigate = useNavigate()

  const [username, setUsername] = useState("")

  const [password, setPassword] = useState("")

  const loginUser = async () => {

    if (!username || !password) {

      alert("Username and password required")

      return
    }

    try {

      const response = await axios.post(
        `${API_URL}/login`,

        {
          username,
          password
        }
      )

      if (response.data.error) {

        alert(response.data.error)

        return
     }
      localStorage.setItem(
        "token",
        response.data.access_token
      )

      alert("Login successful!")

      navigate("/dashboard")

    } catch (error) {

      console.log(error)

      alert("Login failed")
    }
  }

  return (

    <div className="container">

      <h1>Login</h1>

      <input
        type="text"
        placeholder="Username"
        onChange={(e) =>
          setUsername(e.target.value)
        }
      />

      <input
        type="password"
        placeholder="Password"
        onChange={(e) =>
          setPassword(e.target.value)
        }
      />

      <button onClick={loginUser}>
        Login
      </button>

      <p>

        No account?

        <Link to="/register">
          Register
        </Link>

      </p>

    </div>
  )
}

export default Login