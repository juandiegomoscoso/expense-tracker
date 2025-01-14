# Expense Tracker CLI

A command-line expense tracking application built with Python and SQLite.

## Features
- Track daily expenses with descriptions, amounts, and categories
- Manage expense categories
- View expense summaries (total, monthly, by category)
- SQLite database for persistent storage
- Default expense categories included

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/expense-tracker.git
    cd expense-tracker
    ```

2. Make sure you have Python 3.x installed
3. No additional dependencies required - uses standard library only

## Command Options

### Expense Commands
- `add_expense`: Add a new expense
    - `-d, --description`: Description of the expense (Required)
    - `-a, --amount`: Amount spent (Required)
    - `-c, --category`: Category name (Optional)

- `get_expenses`: List all expenses
    - No additional options required

- `update_expense`: Modify existing expense
    - `--id`: ID of the expense to update (Required)
    - `-d, --description`: New description (Optional)
    - `-a, --amount`: New amount (Optional)
    - `-c, --category`: New category (Optional)

- `delete_expense`: Remove an expense
    - `--id`: ID of the expense to delete (Required)

### Category Commands
- `add_category`: Create new category
    - `--name`: Name of the category (Required)

- `get_categories`: List all categories
    - No additional options required

- `delete_category`: Remove a category
    - `--id`: ID of the category to delete (Required)

- `update_category`: Modify category
    - `--id`: ID of the category (Required)
    - `--name`: New category name (Required)

### Summary Commands
- `get_summary`: View total expenses summary
    - No additional options required

- `get_summary_month`: View monthly expenses
    - `-m, --month`: Month number (1-12) (Required)
    - `-y, --year`: Year (Required)

- `get_summary_category`: View expenses by category
    - No additional options required

## Usage Examples

### Managing Expenses
```bash
# Add new expense
python main.py add_expense -d "Grocery shopping" -a 45.99 -c "Food"

# List all expenses
python main.py get_expenses

# Update expense with ID 1
python main.py update_expense --id 1 -d "Weekly groceries" -a 52.50 -c "Food"

# Delete expense with ID 1
python main.py delete_expense --id 1
```

### Managing Categories
```bash
# Add new category
python main.py add_category --name "Healthcare"

# List all categories
python main.py get_categories

# Update category with ID 1
python main.py update_category --id 1 --name "Medical"

# Delete category with ID 1
python main.py delete_category --id 1
```

### Viewing Summaries
```bash
# View total expenses
python main.py get_summary

# View expenses for June 2023
python main.py get_summary_month -m 6 -y 2023

# View expenses by category
python main.py get_summary_category
```

## Database Structure
- SQLite3 database file: `expenses.db`
- Tables:
    - Categories: `id`, `name`
    - Espenses: `id`, `description`, `amount`, `category_id`, `date`

## Default Categories
- Food
- Transport
- Rent
- Entertainment
- Others