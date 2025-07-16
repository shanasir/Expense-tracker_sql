
from db_functions import add_transaction, get_transactions, get_totals_by_category
from data_entry import get_date, get_category, get_amount, get_description

import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime



def add():
    date = get_date("Enter a date of the transactions (dd-mm-yyyy) format or tap enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    descriptions = get_description()
    add_transaction(date, amount, category, descriptions)
    print("Entry added successfully")


def plot(df):
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)

    income_df = (
        df[df["category"] == "Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

    expense_df = (
        df[df["category"] != "Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="r")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="g")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expense Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()


def show_expense_pie_chart():
    data = get_totals_by_category()
    categories = [row[0] for row in data]
    totals = [row[1] for row in data]

    plt.figure(figsize=(10, 8))
    plt.pie(totals, labels=categories, autopct="%1.1f%%", startangle=140)
    plt.title("Expense Distribution by Category")
    plt.axis("equal")
    plt.grid(True)
    plt.show()


def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            add()

        elif choice == "2":
            start_raw = get_date("Enter the start date (dd-mm-yyyy): ")
            end_raw = get_date("Enter the end date (dd-mm-yyyy): ")


            start_date = datetime.strptime(start_raw, "%d-%m-%Y").strftime("%Y-%m-%d")
            end_date = datetime.strptime(end_raw, "%d-%m-%Y").strftime("%Y-%m-%d")

            rows = get_transactions(start_date, end_date)

            if not rows:
                print("No transactions found in the given date range.")
            else:
                print(f"\nTransactions from {start_date} to {end_date}")
                df = pd.DataFrame(rows, columns=["date", "amount", "category", "description"])
                print(df.to_string(index=False))

                total_income = df[df["category"] == "Income"]["amount"].sum()
                total_expense = df[df["category"] != "Income"]["amount"].sum()

                print("\nSummary:")
                print(f"Total Income   : ₹{total_income:.2f}")
                print(f"Total Expenses : ₹{total_expense:.2f}")
                print(f"Net Savings    : ₹{(total_income - total_expense):.2f}")

                if input("Do you want to see a plot? (y/n): ").lower() == "y":
                    plot(df)
                if input("Do you want to see a pie chart? (y/n): ").lower() == "y":
                    show_expense_pie_chart()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
