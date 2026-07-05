# Mini Banking System (Object-Oriented Python)

## Overview

This project is a console-based banking system written in Python using Object-Oriented Programming (OOP).

It allows users to create and manage bank accounts while enforcing real banking business rules instead of simple CRUD operations.

## Features

- Create Account
- Search Account
- Display All Accounts
- Deposit Money
- Withdraw Money
- Transfer Money
- Delete Account

## Business Rules

### Account Creation
- Account numbers are generated automatically.
- Customer names are validated.
- Opening balance must meet the minimum requirement.
- Supports Current and Savings accounts.

### Deposit
- Deposits must be positive.
- Balance is updated after a successful deposit.

### Withdrawal
Current Account
- Overdraft limit: **-£100**

Savings Account
- Minimum balance: **£100**

Invalid withdrawals are rejected.

### Transfer
Transfers:
- Search for the sender account.
- Search for the receiver account.
- Withdraw money from the sender.
- Deposit money into the receiver only if the withdrawal succeeds.
- Display the updated details of both accounts after a successful transfer.

### Delete Account
Accounts can be deleted after confirmation.

## Object-Oriented Concepts Used

- Classes
- Objects
- Constructors (`__init__`)
- Attributes
- Methods
- Encapsulation
- Lists of objects
- Object references

## Skills Demonstrated

- Python
- Object-Oriented Programming
- Business Rule Validation
- Menu-driven Programs
- Input Validation
- Searching Objects
- Banking Logic
- Method Design

## Future Improvements

- SQLite database integration
- Transaction history
- PIN authentication
- Interest calculations
- File persistence
- Exception handling
- Unit testing

## Author

Yusuf Ali

Built as part of my Python and Object-Oriented Programming learning journey.