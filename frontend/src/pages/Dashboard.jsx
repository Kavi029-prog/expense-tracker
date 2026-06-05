import API_URL from "../config";

import { useEffect, useState } from "react"

import axios from "axios"

import Navbar from "../components/Navbar"

import {
  Pie,
  Line
} from "react-chartjs-2"

import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement
} from "chart.js"


ChartJS.register(
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement
)


function Dashboard() {

  const [summary, setSummary] = useState({

    total_income: 0,

    total_expenses: 0,

    net_balance: 0
  })

  const [expenses, setExpenses] = useState([])

  const [income, setIncome] = useState([])

  const [month, setMonth] = useState("2026-06")

  const params = new URLSearchParams(window.location.search)

  const token = params.get("token")

  if (token) {
      localStorage.setItem("token", token)
  }


  useEffect(() => {

    getSummary()

    getExpenses()

    getIncome()

  }, [month])


  const getSummary = async () => {

    try {

      const token = localStorage.getItem("token")

      const response = await axios.get(

        `${API_URL}/summary?month=${month}`,

        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      )

      setSummary(response.data)

    } catch (error) {

      console.log(error)
    }
  }


  const getExpenses = async () => {

    try {

      const token = localStorage.getItem("token")

      const response = await axios.get(

        `${API_URL}/expenses`,

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


  const getIncome = async () => {

    try {

      const token = localStorage.getItem("token")

      const response = await axios.get(

        `${API_URL}/income`,

        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      )

      setIncome(response.data)

    } catch (error) {

      console.log(error)
    }
  }


  const categoryTotals = {}

  expenses.forEach((expense) => {

    if (categoryTotals[expense.category]) {

      categoryTotals[expense.category] += expense.amount

    } else {

      categoryTotals[expense.category] = expense.amount
    }
  })


  const pieData = {

    labels: Object.keys(categoryTotals),

    datasets: [

      {
        label: "Expenses",

        data: Object.values(categoryTotals),

        backgroundColor: [

          "#ef4444",
          "#3b82f6",
          "#22c55e",
          "#f59e0b",
          "#8b5cf6",
          "#ec4899"
        ],
        borderWidth: 1
      }
    ]
  }


  const lineData = {

    labels: ["Income", "Expenses"],

    datasets: [

      {
        label: "Amount",

        data: [

          summary.total_income,

          summary.total_expenses
        ],

        tension: 0.4
      }
    ]
  }


  return (

    <div>

      <Navbar />

      <div className="container">

        <h1>Dashboard</h1>


        <div className="month-selector">

          <label>Select Month: </label>

          <input
            type="month"
            value={month}
            onChange={(e) =>
              setMonth(e.target.value)
            }
          />

        </div>


        <div className="summary-cards">

          <div className="summary-card income">

            <h3>Total Income</h3>

            <p>₹ {summary.total_income}</p>

          </div>


          <div className="summary-card expense">

            <h3>Total Expenses</h3>

            <p>₹ {summary.total_expenses}</p>

          </div>


          <div className="summary-card balance">

            <h3>Net Savings</h3>

            <p>₹ {summary.net_balance}</p>

          </div>

        </div>


        <div className="charts-grid">

          <div className="chart-box">

            <h2>Expense By Category</h2>

            <Pie data={pieData} />

          </div>


          <div className="chart-box">

            <h2>Income vs Expenses</h2>

            <Line data={lineData} />

          </div>

        </div>

      </div>

    </div>
  )
}


export default Dashboard