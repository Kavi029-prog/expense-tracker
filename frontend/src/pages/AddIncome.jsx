import { useState } from "react"

import Navbar from "../components/Navbar"

import axios from "axios"


function AddIncome() {

  const [amount, setAmount] = useState("")

  const [source, setSource] = useState("")

  const [date, setDate] = useState("")


  const addIncome = async () => {

    try {

      const token = localStorage.getItem("token")

      await axios.post(

        "http://127.0.0.1:8000/income",

        {
          amount: Number(amount),

          source,

          date
        },

        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      )

      alert("Income added!")

      setAmount("")

      setSource("")

      setDate("")

    } catch (error) {

      console.log(error)

      alert("Failed to add income")
    }
  }


  return (

    <div>

        <Navbar />
        <div className="container">

        <h1>Add Income</h1>

        <div className="expense-form">

            <input
            type="number"
            placeholder="Amount"
            value={amount}
            onChange={(e) =>
                setAmount(e.target.value)
            }
            className="input"
            />

            <input
            type="text"
            placeholder="Source"
            value={source}
            onChange={(e) =>
                setSource(e.target.value)
            }
            className="input"
            />

            <input
            type="date"
            value={date}
            onChange={(e) =>
                setDate(e.target.value)
            }
            className="input"
            />

            <button onClick={addIncome}>
            Add Income
            </button>

        </div>

        </div>
    </div>    
  )
}


export default AddIncome