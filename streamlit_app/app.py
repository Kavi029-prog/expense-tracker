import streamlit as st

import requests


API_URL = "https://expense-tracker-backend-1m1o.onrender.com"


st.set_page_config(

    page_title="Expense Tracker",

    layout="centered"
)


st.markdown(

    """
    <style>

    .main {

        padding-top: 50px;
    }

    .title {

        text-align: center;

        font-size: 50px;

        font-weight: bold;

        margin-bottom: 40px;
    }

    </style>
    """,

    unsafe_allow_html=True
)


st.markdown(

    '<p class="title">Login</p>',

    unsafe_allow_html=True
)


if "token" not in st.session_state:

    st.session_state.token = None


tab1, tab2 = st.tabs(

    ["Login", "Register"]
)


# LOGIN TAB

with tab1:

    username = st.text_input(

        "Username",

        key="login_user"
    )

    password = st.text_input(

        "Password",

        type="password",

        key="login_pass"
    )


    if st.button("Login"):

        response = requests.post(

            f"{API_URL}/login",

            json={
                "username": username,
                "password": password
            }
        )


        if response.status_code == 200:

            data = response.json()

            if "access_token" in data:

                token = data["access_token"]

                st.session_state.token = token

                st.success("Login successful")

                st.link_button(

                    "Open Expense Tracker Dashboard",

                    f"http://localhost:5173/dashboard?token={token}"
                )

            else:

                if data.get("error") == "User not found":

                    st.warning(

                        "User not registered. Please register first."
                    )

                elif data.get("error") == "Incorrect password":


                    st.error("Incorrect password")

        else:

            st.error("Login failed")

# REGISTER TAB

with tab2:

    username = st.text_input(

        "Create Username",

        key="register_user"
    )

    password = st.text_input(

        "Create Password",

        type="password",

        key="register_pass"
    )


    if st.button("Register"):

        response = requests.post(

            f"{API_URL}/register",

            json={
                "username": username,
                "password": password
            }
        )


        if response.status_code == 200:

            st.success("Registration successful")

        else:

            st.error("Registration failed")