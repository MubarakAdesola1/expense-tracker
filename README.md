# Expense Tracker

A simple command-line Expense Tracker built with Python.

This project was created as part of my Python project-based learning journey. It helped me practice working with lists, dictionaries, functions, loops, file handling, JSON, input validation, and program structure.

## Features

* Add an expense
* View all expenses
* Calculate total spending
* Calculate spending by category
* Delete an expense using its ID
* Save expenses to a JSON file
* Load saved expenses when the program starts
* Validate user input
* Automatically assign unique expense IDs

## Technologies Used

* Python 3
* JSON
* File handling
* Lists and dictionaries
* Functions
* Loops
* Exception handling

## Example Expense

Each expense is stored as a dictionary:

```python
{
    "id": 1,
    "amount": 5000,
    "category": "food",
    "description": "Lunch"
}
```

Multiple expenses are stored inside a list.

## Project Structure

```text
expense-tracker/
│
├── expense_tracker.py
├── expenses.json
└── README.md
```

## How to Run

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Navigate into the project:

```bash
cd expense-tracker
```

3. Run the program:

```bash
python3 expense_tracker.py
```

## What I Learned

Through this project, I practiced:

* Creating and using functions
* Working with lists and dictionaries
* Using loops and conditional statements
* Handling invalid user input with `try` and `except`
* Reading and writing files
* Working with JSON using Python's `json` module
* Breaking a program into smaller functions
* Managing data using IDs
* Understanding how different functions work together in a larger program

## Future Improvements

Possible improvements include:

* Add expense dates
* Edit existing expenses
* Search expenses
* Filter expenses by date or category
* Add monthly spending reports
* Export expenses to CSV
* Improve the command-line interface

## Status

Completed ✅

This project is part of my Python learning journey.
