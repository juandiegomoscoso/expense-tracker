import argparse
from database.db_manager import DatabaseManager
import sys

def main():
    args = parse_arguments()
    db_manager = DatabaseManager("expenses.db")

    if args.command == "add_expense":
        try:
            new_id = db_manager.add_expense(args.description, args.amount, args.category)
            print(f"New expense added with id {new_id}")
        except ValueError as ve:
            print(f"Error: {str(ve)}")
            sys.exit(1)

    elif args.command == "get_expenses":
        expenses = db_manager.get_expenses()
        for expense in expenses:
            print(expense)

    elif args.command == "update_expense":
        db_manager.update_expense(args.id, args.description, args.amount, args.category)

    elif args.command == "get_summary":
        summary = db_manager.get_summary_all_expenses()
        print(f"Total expenses: {summary[0]}")

    elif args.command == "get_summary_month":
        summary = db_manager.get_summary_expenses_of_month(args.month, args.year)
        print(f"Total expenses for {args.month}/{args.year}: {summary[0]}")

    elif args.command == "delete_expense":
        db_manager.delete_expense(args.id)

    elif args.command == "add_category":
        try:
            new_id = db_manager.add_category(args.name)
            print(f"New category added with id {new_id}")
        except ValueError as ve:
            print(f"Error: {str(ve)}")
            sys.exit(1)

    elif args.command == "get_categories":
        categories = db_manager.get_categories()
        for category in categories:
            print(category)

    elif args.command == "delete_category":
        db_manager.delete_category(args.id)

    elif args.command == "update_category":
        db_manager.update_category(args.id)

    elif args.command == "get_summary_category":
        summary = db_manager.get_summary_expenses_by_category()
        for category, amount in summary:
            print(f"{category}: {amount}")

    else:
        print("Invalid command")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Expenses tracker")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add expense
    add_exp_parser = subparsers.add_parser("add_expense", help="Add a new expense")
    add_exp_parser.add_argument("--description", "-d", required=True, help="Expense description")
    add_exp_parser.add_argument("--amount", "-a", required=True, type=float, help="Expense amount")
    add_exp_parser.add_argument("--category", "-c", help="Expense category")

    # Get expenses
    get_exp_parser = subparsers.add_parser("get_expenses", help="Get list of expenses")

    # Update expense
    update_exp_parser = subparsers.add_parser("update_expense", help="Update an expense")
    update_exp_parser.add_argument("--id", required=True, type=int, help="Expense ID")
    update_exp_parser.add_argument("--description", "-d", help="New description")
    update_exp_parser.add_argument("--amount", "-a", type=float, help="New amount")
    update_exp_parser.add_argument("--category", "-c", help="New category")

    # Get summary of expenses
    get_summary_parser = subparsers.add_parser("get_summary", help="Get summary of all expenses")

    # Get summary of expenses of a month
    get_summary_month_parser = subparsers.add_parser("get_summary_month", help="Get summary of expenses of a month")
    get_summary_month_parser.add_argument("--month", "-m", type=int, help="Month")
    get_summary_month_parser.add_argument("--year", "-y", type=int, help="Year")

    # Delete expense
    delete_exp_parser = subparsers.add_parser("delete_expense", help="Delete an expense")
    delete_exp_parser.add_argument("--id", required=True, type=int, help="Expense ID")

    # Add category
    add_cat_parser = subparsers.add_parser("add_category", help="Add a new category")
    add_cat_parser.add_argument("--name", required=True, help="Category name")

    # Get categories
    get_cat_parser = subparsers.add_parser("get_categories", help="Get list of categories")

    # Delete category
    delete_cat_parser = subparsers.add_parser("delete_category", help="Delete a category")
    delete_cat_parser.add_argument("--id", required=True, help="Category id")

    # Update category
    update_cat_parser = subparsers.add_parser("update_category", help="Update a category")
    update_cat_parser.add_argument("--id", required=True, help="Category id")

    # Get summary of all expenses by category
    get_summary_cat_parser = subparsers.add_parser("get_summary_category", help="Get summary of all expenses by category")
    
    return parser.parse_args()


if __name__ == "__main__":
    main()