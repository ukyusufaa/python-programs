# Car Rental System (Object-Oriented Python with SQLite)

## Overview

This project is a console-based Car Rental System developed in Python using Object-Oriented Programming (OOP) and SQLite.

The application allows staff to manage customers, manage rental vehicles, rent and return cars, and store all information permanently in a SQLite database.

The project was built to practise object-oriented programming, database design, CRUD operations, business rules, and SQL integration.

---

## Features

### Customer Management
- Create customer
- Search customer
- Display all customers
- Update customer details
- Delete customer

### Car Management
- Create car
- Search car
- Display all cars
- Delete available cars

### Rental Management
- Rent available cars
- Return rented cars
- Calculate rental cost
- Link rented cars to customers
- Automatically update vehicle availability

---

## Technologies Used

- Python 3
- SQLite3
- Object-Oriented Programming (OOP)
- SQL
- VS Code
- Git
- GitHub

---

## Database

The project uses SQLite with two tables:

### Client Table

Stores customer information including:

- Customer ID
- Name
- Address
- Phone Number
- Email Address

### Car Rental Table

Stores vehicle information including:

- Car ID
- Make
- Model
- Colour
- Registration Number
- Daily Rental Price
- Availability
- Customer ID (when rented)

---

## Business Rules

- Customer IDs are generated automatically by SQLite.
- Car IDs are generated automatically by SQLite.
- Cars are initially marked as Available.
- Only available cars can be rented.
- Rented cars cannot be deleted.
- Daily rental prices are automatically assigned based on vehicle make.
- Registration numbers must contain exactly seven alphanumeric characters.
- Customer details are stored permanently in the database.
- Car details are stored permanently in the database.

---

## Validation

The program validates:

- Empty input
- Customer names
- Vehicle make
- Vehicle model
- Vehicle colour
- Vehicle registration format

---

## Skills Demonstrated

This project demonstrates:

- Object-Oriented Programming
- Classes and Objects
- Constructors
- Methods
- CRUD Operations
- SQLite Database Design
- SQL Queries
- INSERT
- SELECT
- UPDATE
- DELETE
- Input Validation
- Business Logic
- Menu Driven Applications

---

## Future Improvements

- Prevent duplicate registration numbers.
- Improve numeric input validation.
- Record complete rental history.
- Calculate overdue rental charges.
- Add customer search by name.
- Add reporting features.

---

## Author

Yusuf Ali