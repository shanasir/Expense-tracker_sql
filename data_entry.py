import datetime

from pandas import value_counts
from unicodedata import category

date_format="%d-%m-%Y"
categorys = {"I":"Income","E":"Expense"}

def get_date(prompt,allow_default=False):
     date_str=input(prompt)
     if allow_default and not date_str:
         return datetime.datetime.today().strftime(date_format)
     try:
         valid_date=datetime.datetime.strptime(date_str, date_format)
         return valid_date.strftime(date_format)
     except ValueError:
         print("Invalid format,Please enter in dd-mm-yyyy format!Thank you ")
         return get_date(prompt,allow_default)


def get_amount():
    try:
        amount=float(input("Enter th amount: "))
        if amount<=0:
            raise ValueError("Amount should not be in non-zero numbers")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category ('I' for income and 'E' for expense): ").upper()
    if category in categorys:
        return categorys[category]

    print("Invalid category type accordingly")
    return get_category()

def get_description():
    return input("Enter a descriptions u want too...(optional):")

    

