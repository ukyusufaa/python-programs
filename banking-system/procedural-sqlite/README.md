# Banking System (Procedural SQLite)

## Overview

This project is a command-line Banking System developed in Python using SQLite for permanent data storage.

The application allows users to create bank accounts, search for accounts, deposit money, withdraw money and delete accounts while storing customer information in an SQLite database.

## Features

- Create new bank accounts
- Automatic account number generation
- Search for customer accounts
- Deposit money
- Withdraw money
- Delete bank accounts
- Customer name validation
- Deposit and withdrawal validation
- SQLite database storage

## Business Rules

- Minimum opening deposit is **£50.00**
- Customer names may only contain letters and spaces
- Deposits must be greater than **£0.00**
- Withdrawals cannot exceed the available account balance
- Accounts can only be deleted when the account balance is **£0.00**
- Account numbers are generated automatically

## Technologies Used

- Python 3
- SQLite3

## Skills Demonstrated

- Procedural Programming
- Python Functions
- SQLite Database Programming
- SQL CRUD Operations
  - CREATE
  - INSERT
  - SELECT
  - UPDATE
  - DELETE
- Input Validation
- Exception Handling
- Business Rule Implementation

## Database

The project uses an SQLite database to store customer account information, including:

- Account Number
- Customer Name
- Account Balance

## How to Run

1. Ensure Python 3 is installed.
2. Open the project folder.
3. Run:

```bash
python main.py
```

## Future Improvements

- Display all customer accounts
- Account statements
- Transaction history
- Savings and Current account types
- Interest calculations
- Graphical User Interface (GUI)

## Author

Created by Yusuf Ali as part of a Python software development portfolio.