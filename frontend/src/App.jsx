import { Routes, Route } from "react-router-dom"

import Login from "./pages/Login"

import Register from "./pages/Register"

import Dashboard from "./pages/Dashboard"

import AddExpense from "./pages/AddExpense"

import History from "./pages/History"

import AddIncome from "./pages/AddIncome"


function App() {

  return (

    

      <Routes>

        <Route
          path="/"
          element={<Login />}
        />

        <Route
          path="/register"
          element={<Register />}
        />

        <Route
          path="/dashboard"
          element={<Dashboard />}
        />

        <Route
          path="/add-expense"
          element={<AddExpense />}
        />

        <Route
          path="/history"
          element={<History />}
        />
        <Route
          path="/add-income"
          element={<AddIncome />}
        />

      </Routes>

    
  )
}


export default App