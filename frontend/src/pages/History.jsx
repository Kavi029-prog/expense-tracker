import API_URL from "../config";

import { useEffect, useState } from "react"

import axios from "axios"

import Navbar from "../components/Navbar"


function History() {

  const [expenses, setExpenses] = useState([])


  useEffect(() => {

    getExpenses()

  }, [])


  const getExpenses = async () => {

    try {

      const token = localStorage.getItem("token")

      const response = await axios.get(

        "https://expense-tracker-backend-1m1o.onrender.com/expenses",

        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      )

      setExpenses(response.data)

    } catch (error) {

      console.log(error)
    }
  }


  const deleteExpense = async (id) => {

    try {

      const token = localStorage.getItem("token")

      await axios.delete(

        `${API_URL}/expenses/${id}`,

        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      )

      alert("Expense deleted!")

      getExpenses()

    } catch (error) {

      console.log(error)

      alert("Failed to delete expense")
    }
  }


  return (

    <div>

      <Navbar />

      <div className="container">

        <h1>Expense History</h1>

        <table className="expense-table">

          <thead>

            <tr>

              <th>Title</th>

              <th>Category</th>

              <th>Amount</th>

              <th>Note</th>

              <th>Date</th>

              <th>Action</th>

            </tr>

          </thead>

          <tbody>

            {expenses.map((expense) => (

              <tr key={expense.id}>

                <td>{expense.title}</td>

                <td>{expense.category}</td>

                <td>₹ {expense.amount}</td>

                <td>{expense.note}</td>

                <td>{expense.expense_date}</td>

                <td>

                  <button
                    onClick={() =>
                      deleteExpense(expense.id)
                    }
                  >
                    Delete
                  </button>

                </td>

              </tr>
            ))}

          </tbody>

        </table>

      </div>

    </div>
  )
}


export default History