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

    
