import { Link, useNavigate } from "react-router-dom"

import "./Navbar.css"


function Navbar() {

  const navigate = useNavigate()


  const logout = () => {

    localStorage.removeItem("token")

    navigate("/")
  }


  return (

    <nav className="navbar">

      <h2 className="logo">
        Expense Tracker
      </h2>

      <div className="nav-links">

        <Link to="/dashboard">
          Dashboard
        </Link>

        <Link to="/add-expense">
          Add Expense
        </Link>

        <Link to="/history">
          History
        </Link>

        <Link to="/add-income">
          Add Income
        </Link>

        <button onClick={logout}>
          Logout
        </button>

      </div>

    </nav>
  )
}


export default Navbar