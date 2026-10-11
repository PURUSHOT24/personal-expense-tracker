# Personal Expense Tracker

A simple, menu-driven expense tracker for the terminal, written in beginner-friendly Python. It saves your expenses in a CSV file, so your data is still there after you close the program.

## Features

- Add an expense with amount, category, date, and description
- View all recorded expenses in a neat table
- Calculate the total of all expenses
- View totals for each category, and list the expenses of one category
- Search expenses by date (with a total for that day)
- Delete an expense by its ID (with a confirmation step)
- Permanent storage in `expenses.csv`
- Input validation: invalid amounts, dates, menu choices, and IDs are handled without crashing

## Technologies Used

- Python 3
- Built-in `csv` module (file handling)
- Built-in `datetime` and `os` modules

No paid services, API keys, or extra packages are needed.

## Python Installation Requirements

- Python 3.6 or newer (download from https://www.python.org/downloads/)
- Check your version by running `python --version` (or `python3 --version` on Mac/Linux)
- No `pip install` is required. `requirements.txt` is included only to show there are no dependencies.

## How to Run

1. Download or clone this project and open a terminal inside the `personal-expense-tracker` folder.
2. Run:

   ```bash
   python main.py
   ```

   On Mac/Linux you may need `python3 main.py`.
3. Type a number from the menu and press Enter.

## Project Structure

```
personal-expense-tracker/
├── main.py            # the program
├── expenses.csv       # where expenses are saved (starts with only a header row)
├── README.md          # this file
├── requirements.txt   # no dependencies
└── .gitignore         # files Git should ignore
```

## Example Output

The following is an example of how the program looks when run (the values are sample data):

```
===== PERSONAL EXPENSE TRACKER =====
1. Add expense
2. View all expenses
3. Show total expenses
4. View expenses by category
5. Search expenses by date
6. Delete an expense
7. Exit
Choose an option (1-7): 2

--- All Expenses ---

ID   Date            Amount  Category      Description
------------------------------------------------------------
1    2026-10-11      250.50  Food          Lunch at cafe
2    2026-10-11       99.00  Travel        Bus ticket
3    2026-10-10      500.00  Bills         Electricity bill
------------------------------------------------------------
```

## Future Improvements

- Edit an existing expense
- Filter by month or date range
- Monthly summary reports
- Set a budget and show a warning when it is exceeded
- Export reports to Excel or PDF
- Charts using `matplotlib`
- A graphical interface (Tkinter) or a web version (Flask)
- Automated tests with `unittest` or `pytest`

## How to Upload This Project to GitHub

1. Create a free account at https://github.com.
2. Click **New repository**, name it `personal-expense-tracker`, and do not tick "Add a README" (you already have one). Click **Create repository**.
3. Install Git from https://git-scm.com/downloads if you do not have it.
4. In a terminal inside the project folder, run:

   ```bash
   git init
   git add .
   git commit -m "Add personal expense tracker project"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/personal-expense-tracker.git
   git push -u origin main
   ```

   Replace `YOUR-USERNAME` with your GitHub username.
5. Refresh the repository page to see your files.

## Author

Your Name - add your GitHub and LinkedIn links here.
