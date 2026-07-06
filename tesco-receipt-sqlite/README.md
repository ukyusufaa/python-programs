# Tesco Receipt System (Procedural Python with SQLite)

## Overview

This project is a console-based Tesco Receipt System developed in Python using procedural programming and SQLite.

The system allows users to create, search, update, delete, and display customer orders while storing all data permanently in a SQLite database.

The project was developed to practise Python programming, SQL, CRUD operations, input validation, and business rule implementation.

---

## Features

- Insert new orders
- Display all orders
- Search for an order
- Update an existing order
- Delete an order
- Calculate order totals
- Store data using SQLite

---

## Database

The project uses a SQLite database containing one table:

### expenses

| Column | Description |
|---------|-------------|
| t_id | Primary Key (Auto Increment) |
| t_order_id | Order Number |
| t_item | Item Name |
| t_category | Product Category |
| t_amount | Item Price |

---

## Product Categories

The system supports:

- Food
- Clothing
- Electrics

Each category has its own maximum permitted price validation.

---

## Validation

The program validates:

- Product category
- Product price
- Numeric input for prices
- Empty database searches
- Update and delete operations

---

## Technologies Used

- Python 3
- SQLite3
- SQL
- Procedural Programming
- Git
- GitHub

---

## SQL Operations

The project demonstrates:

- CREATE TABLE
- INSERT
- SELECT
- UPDATE
- DELETE

using parameterised SQL queries.

---

## Skills Demonstrated

- Procedural Programming
- SQLite Database Design
- CRUD Operations
- SQL
- Input Validation
- Business Logic
- Menu-Driven Applications
- Data Processing

---

## Future Improvements

- Prevent duplicate order numbers.
- Improve numeric input validation.
- Allow decimal prices for all products.
- Generate printable receipts.
- Add discount calculations.
- Produce sales reports.

---

## Author

Yusuf Ali