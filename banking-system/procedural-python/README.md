# Banking System (Procedural Python)

## Overview

This project is a command-line Banking System written in Python using procedural programming.

The application allows users to create bank accounts, search for accounts, deposit money, withdraw money, delete accounts and display all customer accounts while enforcing business rules and input validation.

## Features

- Create new bank accounts
- Automatic account number generation
- Search for customer accounts
- Deposit money
- Withdraw money
- Delete accounts (only when balance is £0.00)
- Display all customer accounts
- Customer name validation
- Deposit and withdrawal validation
- Formatted account receipts

## Business Rules

- Minimum opening deposit is **£50.00**
- Customer names may contain letters and spaces only
- Deposits must be greater than £0.00
- Withdrawals cannot exceed the current balance
- Bank accounts can only be deleted when the balance is **£0.00**
- Account numbers are generated automatically

## Technologies Used

- Python 3

## Programming Concepts Demonstrated

- Procedural Programming
- Functions
- Lists
- Dictionaries
- Loops
- Input Validation
- Exception Handling (`try` / `except`)
- Business Rules
- CRUD Operations

## Future Improvements

- Store customer data using SQLite
- Convert the application to Object-Oriented Programming (OOP)
- Add account types (Current and Savings)
- Add transaction history
- Add interest calculations

## Author

Created by Yusuf Ali as part of a Python learning portfolio.