import { useState, useEffect } from "react"

import axios from "axios"

import Navbar from "../components/Navbar"

import API_URL from "../config";


function AddExpense() {

  const [title, setTitle] = useState("")

  const [amount, setAmount] = useState("")

  const [category, setCategory] = useState("")

  const [note, setNote] = useState("")

  const [expenseDate, setExpenseDate] = useState("")

  const [categories, setCategories] = useState([])


  useEffect(() => {

    fetchCategories()

  }, [])


  const fetchCategories = async () => {

    try {

      const token = localStorage.getItem("token")

      const response = await axios.get(

        `${API_URL}/categories`,

        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      )

      setCategories([

        ...response.data.default_categories,

        ...response.data.custom_categories
      ])

    } catch (error) {

      console.log(error)
    }
  }


  const addExpense = async () => {

    try {

      const token = localStorage.getItem("token")

      await axios.post(

        `${API_URL}/expenses`,

        {
          title,

          amount: Number(amount),

          category,

          note,

          expense_date: expenseDate || null
        },

        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      )

      alert("Expense added!")

      setTitle("")

      setAmount("")

      setCategory("")

      setNote("")

      setExpenseDate("")

    } catch (error) {

      console.log(error.response.data)

      alert("Failed to add expense")
    }
  }


  return (

    <div>

      <Navbar />

      <div className="container">

        <h1>Add Expense</h1>

        <div className="expense-form">

          <input
            type="text"
            placeholder="Title"
            value={title}
            onChange={(e) =>
              setTitle(e.target.value)
            }
            className="input"
          />

          <input
            type="text"
            placeholder="Amount"
            value={amount}
            onChange={(e) =>
              setAmount(e.target.value)
            }
            className="input"
          />

          <select
            className="expense-select"
            value={category}
            onChange={(e) =>
              setCategory(e.target.value)
            }
            className="input"
          >

            <option value="">
              Select Category
            </option>

            {categories.map((cat, index) => (

              <option
                key={index}
                value={cat}
              >
                {cat}
              </option>
            ))}

          </select>

          <input
            type="text"
            placeholder="Note"
            value={note}
            onChange={(e) =>
              setNote(e.target.value)
            }
            className="input"
          />

          <input
            type="date"
            value={expenseDate}
            onChange={(e) =>
                setExpenseDate(e.target.value)
            }
            className="input"
            />

          <button onClick={addExpense}>
            Add Expense
          </button>

        </div>

      </div>

    </div>
  )
}


export default AddExpense