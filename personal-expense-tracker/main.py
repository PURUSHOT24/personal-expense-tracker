"""
Personal Expense Tracker
A simple menu-driven program to record and review daily expenses.
Expenses are saved in a CSV file so they are kept after closing the program.
"""

import csv
import os
from datetime import datetime

# The CSV file lives next to main.py, so it works from any folder
FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.csv")
HEADERS = ["id", "date", "amount", "category", "description"]
DATE_FORMAT = "%Y-%m-%d"


# ---------- File handling ----------

def setup_file():
    """Create the CSV file with a header row if it does not exist or is empty."""
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow(HEADERS)


def load_expenses():
    """Read all expenses from the CSV file and return them as a list of dictionaries."""
    expenses = []
    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                try:
                    row["id"] = int(row["id"])
                    row["amount"] = float(row["amount"])
                    expenses.append(row)
                except (ValueError, KeyError, TypeError):
                    continue  # skip damaged rows instead of crashing
    except FileNotFoundError:
        setup_file()
    except OSError as error:
        print(f"Could not read the file: {error}")
    return expenses


def save_expenses(expenses):
    """Write the full list of expenses back to the CSV file."""
    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(expenses)
        return True
    except OSError as error:
        print(f"Could not save the file: {error}")
        return False


# ---------- Input helpers (validation) ----------

def get_amount():
    """Keep asking until the user enters a valid positive number."""
    while True:
        text = input("Amount: ").strip()
        try:
            amount = float(text)
            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return round(amount, 2)
        except ValueError:
            print("Please enter a number, for example 250 or 99.50.")


def get_date(prompt="Date (YYYY-MM-DD, press Enter for today): ", allow_blank=True):
    """Keep asking until the user enters a valid date. Returns a string."""
    while True:
        text = input(prompt).strip()
        if text == "" and allow_blank:
            return datetime.now().strftime(DATE_FORMAT)
        try:
            return datetime.strptime(text, DATE_FORMAT).strftime(DATE_FORMAT)
        except ValueError:
            print("Invalid date. Use the format YYYY-MM-DD, for example 2026-10-11.")


def get_text(prompt, allow_blank=False):
    """Keep asking until the user types some text."""
    while True:
        text = input(prompt).strip()
        if text or allow_blank:
            return text
        print("This field cannot be empty.")


def get_next_id(expenses):
    """Return a new unique ID (highest existing ID + 1)."""
    if not expenses:
        return 1
    return max(expense["id"] for expense in expenses) + 1


# ---------- Display helper ----------

def print_table(expenses):
    """Print a list of expenses as a neat table."""
    if not expenses:
        print("No expenses found.")
        return
    print(f"\n{'ID':<5}{'Date':<12}{'Amount':>10}  {'Category':<14}{'Description'}")
    print("-" * 60)
    for e in expenses:
        print(f"{e['id']:<5}{e['date']:<12}{e['amount']:>10.2f}  "
              f"{e['category']:<14}{e['description']}")
    print("-" * 60)


# ---------- Main features ----------

def add_expense():
    """Ask for expense details and save them."""
    print("\n--- Add Expense ---")
    amount = get_amount()
    category = get_text("Category (e.g. Food, Travel, Bills): ").title()
    date = get_date()
    description = get_text("Description (optional): ", allow_blank=True)

    expenses = load_expenses()
    new_expense = {
        "id": get_next_id(expenses),
        "date": date,
        "amount": amount,
        "category": category,
        "description": description,
    }
    expenses.append(new_expense)
    if save_expenses(expenses):
        print("Expense added successfully!")


def view_expenses():
    """Show every recorded expense."""
    print("\n--- All Expenses ---")
    print_table(load_expenses())


def show_total():
    """Show the total of all expenses."""
    expenses = load_expenses()
    total = sum(e["amount"] for e in expenses)
    print(f"\nNumber of expenses: {len(expenses)}")
    print(f"Total spent: {total:.2f}")


def view_by_category():
    """Show a total for each category, then optionally list one category."""
    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses found.")
        return

    # Add up the amounts for each category
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]

    print("\n--- Totals by Category ---")
    for category, total in sorted(totals.items()):
        print(f"{category:<15}{total:>10.2f}")

    choice = input("\nType a category name to see its expenses (or press Enter to skip): ").strip().title()
    if choice:
        matches = [e for e in expenses if e["category"].title() == choice]
        print_table(matches)


def search_by_date():
    """Show expenses for one specific date."""
    print("\n--- Search by Date ---")
    date = get_date("Enter date (YYYY-MM-DD): ", allow_blank=False)
    matches = [e for e in load_expenses() if e["date"] == date]
    print_table(matches)
    if matches:
        print(f"Total for {date}: {sum(e['amount'] for e in matches):.2f}")


def delete_expense():
    """Delete an expense by its ID."""
    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses to delete.")
        return
    print_table(expenses)

    text = input("Enter the ID of the expense to delete: ").strip()
    try:
        expense_id = int(text)
    except ValueError:
        print("Please enter a valid whole number.")
        return

    for e in expenses:
        if e["id"] == expense_id:
            confirm = input(f"Delete '{e['description'] or e['category']}' ({e['amount']:.2f})? (y/n): ").strip().lower()
            if confirm == "y":
                expenses.remove(e)
                if save_expenses(expenses):
                    print("Expense deleted.")
            else:
                print("Delete cancelled.")
            return
    print("No expense found with that ID.")


# ---------- Menu ----------

def show_menu():
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Show total expenses")
    print("4. View expenses by category")
    print("5. Search expenses by date")
    print("6. Delete an expense")
    print("7. Exit")


def main():
    setup_file()
    actions = {
        "1": add_expense,
        "2": view_expenses,
        "3": show_total,
        "4": view_by_category,
        "5": search_by_date,
        "6": delete_expense,
    }
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()
        if choice == "7":
            print("Goodbye! Your expenses are saved.")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram closed. Your expenses are saved.")
