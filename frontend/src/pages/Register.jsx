import API_URL from "../config";

import { useState } from "react"

import axios from "axios"

import { Link, useNavigate } from "react-router-dom"

function Register() {

  const navigate = useNavigate()

  const [username, setUsername] = useState("")

  const [password, setPassword] = useState("")

  const registerUser = async () => {

    if (!username || !password) {

      alert("Username and password required")

      return
    }

    try {

      await axios.post(
        `${API_URL}/register`,

        {
          username,
          password
        }
      )

      alert("Registration successful!")

      navigate("/")

    } catch (error) {

      console.log(error)

      alert("Registration failed")
    }
  }

  return (

    <div className="container">

      <h1>Register</h1>

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

      <button onClick={registerUser}>
        Register
      </button>

      <p>

        Already have account?

        <Link to="/">
          Login
        </Link>

      </p>

    </div>
  )
}

export default Register
