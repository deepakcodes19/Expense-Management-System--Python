import mysql.connector
from contextlib import contextmanager
import logging

# Logger setup
logger = logging.getLogger("db_helper")
logging.basicConfig(level=logging.INFO)


@contextmanager
def get_db_cursor(commit=False):
    """Context manager to handle database connection."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )
    cursor = connection.cursor(dictionary=True)

    try:
        yield cursor
        if commit:
            connection.commit()
    finally:
        cursor.close()
        connection.close()


def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        logger.info(f"Fetched expenses: {expenses}")  # Log raw data to see what’s returned
        return expenses


def delete_expenses_for_date(expense_date):
    """Delete all expenses for a specific date."""
    logger.info(f"Deleting expenses for date: {expense_date}")

    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


def insert_expense(expense_date, amount, category, notes):
    """Insert a new expense into the database."""
    logger.info(f"Inserting expense: {expense_date}, {amount}, {category}, {notes}")

    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )


def fetch_expense_summary(start_date, end_date):
    """Fetch summarized expenses within a date range."""
    logger.info(f"Fetching expense summary from {start_date} to {end_date}")

    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category, SUM(amount) as total 
               FROM expenses WHERE expense_date BETWEEN %s and %s  
               GROUP BY category''',
            (start_date, end_date)
        )
        return cursor.fetchall()


if __name__ == "__main__":
    # Test the database functions
    expenses = fetch_expenses_for_date("2024-09-30")
    print(expenses)

    summary = fetch_expense_summary("2024-08-01", "2024-08-05")
    print(summary)
