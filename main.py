import argparse
from database.db_manager import DatabaseManager


def parse_arguments():
    parser = argparse.ArgumentParser(description="Expenses tracker")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    