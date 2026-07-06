# Car Rental System (Object-Oriented Python)

## Overview

This project is a console-based Car Rental System written in Python using Object-Oriented Programming (OOP). It demonstrates customer management, car management, and the complete car rental process while enforcing business rules.

The system allows users to create and manage customers, maintain a fleet of rental vehicles, rent cars, return cars, and prevent invalid operations such as deleting rented vehicles.

---

## Features

### Customer Management
- Create new customers
- Search customers by Customer ID
- Display all customers
- Update customer details
- Delete customers

### Car Management
- Create new cars
- Search cars by Car ID
- Display all cars
- Delete available cars

### Car Rental
- Rent available cars
- Return rented cars
- Automatically change vehicle availability
- Calculate rental cost based on daily rental rate and rental duration
- Create a new customer during the rental process if the customer does not already exist

---

## Business Rules

- Customer IDs are generated automatically.
- Car IDs are generated automatically.
- Every new car is initially marked as **Available**.
- Cars cannot be rented if already unavailable.
- Rented cars cannot be deleted.
- Daily rental prices are determined by the vehicle manufacturer.
- Registration numbers must contain exactly seven letters and/or numbers.

---

## Validation

The program validates:

- Customer names
- Vehicle make
- Vehicle model
- Vehicle colour
- Vehicle registration number
- Empty input fields

---

## Technologies Used

- Python 3
- Object-Oriented Programming
- Lists of Objects
- Functions
- Input Validation

---

## Future Improvements

- Store data using SQLite instead of in-memory lists.
- Improve input validation for numeric values.
- Prevent duplicate registration numbers.
- Record rental history.
- Calculate late return charges.
- Save data between program executions.

---

## Learning Outcomes

This project helped me practise:

- Classes and Objects
- Constructors (`__init__`)
- Object Methods
- Business Rule Implementation
- CRUD Operations
- Searching Lists of Objects
- Input Validation
- Program Design
- Menu Driven Applications

---

## Author

Yusuf Ali