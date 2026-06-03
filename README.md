# Expense Tracker App

A full-stack Expense Tracker application built using:

* React.js frontend
* FastAPI backend
* PostgreSQL database
* Streamlit login portal
* JWT authentication

## Features

* User registration & login
* Add expenses and income
* Dashboard analytics
* Pie chart and bar graph
* Expense history
* Protected routes
* PostgreSQL integration

## Tech Stack

### Frontend

* React.js
* Vite
* Axios
* Chart.js

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* JWT Authentication

### Additional

* Streamlit
* GitHub workflow

## Run Backend

```bash id="w3q8ka"
cd backend
uvicorn app.main:app --reload
```

## Run Frontend

```bash id="v6m2pw"
cd frontend
npm install
npm run dev
```

## Run Streamlit

```bash id="q5t1vl"
streamlit run streamlit_app/app.py
```
