import streamlit as st
import pandas as pd
from datetime import datetime
from db_functions import add_transaction, get_transactions, get_totals_by_category

st.set_page_config(page_title="Expense Tracker", layout="wide")
st.title("💸 Expense Tracker")

menu = ["Add Transaction", "View Transactions", "View Charts"]
choice = st.sidebar.radio("Choose an action:", menu)

if choice == "Add Transactions":
    st.subheader("➕ Add a New Transaction")
    date = st.date_input("Transaction Date", datetime.today())
    amount = st.number_input("Amount", min_value=0.0)
    category = st.selectbox("Category", ["Income", "Food", "Bills", "Transport", "Shopping", "Other"])
    description = st.text_input("Description")

    if st.button("Add Transaction"):
        formatted_date = date.strftime("%Y-%m-%d")
        add_transaction(formatted_date, amount, category, description)
        st.success("✅ Transaction added successfully!")

elif choice == "View Transactions":
    st.subheader("📋 View Transactions Within a Date Range")
    start_date = st.date_input("Start Date", datetime(2024, 1, 1))
    end_date = st.date_input("End Date", datetime.today())

    if st.button("Show Transactions"):
        start_str = start_date.strftime("%Y-%m-%d")
        end_str = end_date.strftime("%Y-%m-%d")
        rows = get_transactions(start_str, end_str)

        if rows:
            df = pd.DataFrame(rows, columns=["Date", "Amount", "Category", "Description"])
            st.dataframe(df)

            total_income = df[df["Category"] == "Income"]["Amount"].sum()
            total_expense = df[df["Category"] != "Income"]["Amount"].sum()

            st.markdown(f"""
            ### 💰 Summary
            - **Total Income**: ₹{total_income:.2f}
            - **Total Expenses**: ₹{total_expense:.2f}
            - **Net Savings**: ₹{(total_income - total_expense):.2f}
            """)
        else:
            st.warning("No transactions found.")

elif choice == "View Charts":
    st.subheader("📊 Expense Distribution by Category")
    data = get_totals_by_category()

    if data:
        categories = [row[0] for row in data]
        totals = [row[1] for row in data]
        chart_df = pd.DataFrame({"Category": categories, "Total": totals})
        st.bar_chart(chart_df.set_index("Category"))
    else:
        st.warning("No data to plot.")
