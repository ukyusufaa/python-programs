# OOP Banking System (Python + SQLite)

## Overview

This project is a console-based Banking System developed in Python using Object-Oriented Programming (OOP) and SQLite.

The application allows users to create and manage bank accounts while storing all data permanently in an SQLite database.

This project was built to practise OOP concepts, CRUD operations, business rules, validation and database programming.

---

## Features

- Create new bank accounts
- Search for an account
- Display all accounts
- Delete an account
- Deposit money
- Withdraw money
- Transfer money between accounts
- Auto-generated account numbers
- SQLite database storage

---

## Business Rules

### Opening Account
- Customer name cannot be blank.
- Customer name must contain letters only.
- Minimum opening deposit is **£50.00**.
- Account numbers are generated automatically.

### Account Types

#### Current Account
- Overdraft limit of **-£100**.

#### Savings Account
- Balance cannot fall below **£100**.

### Delete Account
- Accounts can only be deleted when the balance is **£0.00**.

---

## Technologies Used

- Python 3
- SQLite3
- Object-Oriented Programming (Classes and Objects)

---

## Database

Table: **barclays**

Fields:

- ID (Auto Increment)
- Customer Name
- Account Number
- Balance
- Account Type

---

## OOP Concepts Used

- Classes
- Objects
- Constructors
- Instance Attributes
- Methods
- Encapsulation

---

## CRUD Operations

| Operation | Status |
|----------|--------|
| Create | ✅ |
| Read | ✅ |
| Update | ✅ |
| Delete | ✅ |

---

## Future Improvements

- Input validation using try/except throughout the program
- Interest calculation for Savings Accounts
- Transaction history
- Login system
- PIN authentication
- Account statements
- Money transfer validation improvements

---

## Author

Yusuf Ali

Created as part of my Python, Object-Oriented Programming and SQLite learning journey.