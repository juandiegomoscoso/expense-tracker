import argparse
from database.db_manager import DatabaseManager


def parse_arguments():
    parser = argparse.ArgumentParser(description="Expenses tracker")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add expense
    add_exp_parser = subparsers.add_parser("add_expense", help="Add a new expense")
    add_exp_parser.add_argument("--description", required=True, help="Expense description")
    add_exp_parser.add_argument("--amount", required=True, type=float, help="Expense amount")
    add_exp_parser.add_argument("--category", help="Expense category")

    # Get expenses
    get_exp_parser = subparsers.add_parser("get_expenses", help="Get list of expenses")

    
    # Update expense
    update_exp_parser = subparsers.add_parser("update_expense", help="Update an expense")
    update_exp_parser.add_argument("id", type=int, help="Expense ID")
    update_exp_parser.add_argument("--description", help="New description")
    update_exp_parser.add_argument("--amount", type=float, help="New amount")
    update_exp_parser.add_argument("--category", help="New category")


    # Get summary of expenses
    get_summary_parser = subparsers.add_parser("get_summary", help="Get summary of all expenses")
    

    # Get summary of expenses of a month
    get_summary_month_parser = subparsers.add_parser("get_summary_month", help="Get summary of expenses of a month")
    get_summary_month_parser.add_argument("--month", type=int, help="Month")
    get_summary_month_parser.add_argument("--year", type=int, help="Year")

    
    # Delete expense
    delete_exp_parser = subparsers.add_parser("delete_expense", help="Delete an expense")
    delete_exp_parser.add_argument("id", type=int, help="Expense ID")


    # Add category
    add_cat_parser = subparsers.add_parser("add_category", help="Add a new category")
    add_cat_parser.add_argument("name", help="Category name")


    # Get categories
    get_cat_parser = subparsers.add_parser("get_categories", help="Get list of categories")


    # Delete category
    delete_cat_parser = subparsers.add_parser("delete_category", help="Delete a category")
    delete_cat_parser.add_argument("nid", help="Category id")


    # Update category
    update_cat_parser = subparsers.add_parser("update_category", help="Update a category") 
    update_cat_parser.add_argument("id", help="Category id")