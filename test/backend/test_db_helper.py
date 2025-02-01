# test_db_helper.py

from backend import db_helper


def test_fetch_expenses_for_date_aug_15():
    # Test case for fetching expenses on 2024-08-15
    expenses = db_helper.fetch_expenses_for_date("2024-08-15")

    # Check if expenses is a valid list (not None)
    assert expenses is not None  # Should now always return a list

    assert len(expenses) == 1  # Expect 1 expense

    # Check if the expense has the expected details
    assert expenses[0]['amount'] == 10.0
    assert expenses[0]['category'] == "Shopping"
    assert expenses[0]["notes"] == "Bought potatoes"


def test_fetch_expenses_for_date_invalid_date():
    # Test case for fetching expenses on an invalid date (9999-08-15)
    expenses = db_helper.fetch_expenses_for_date("9999-08-15")

    # Ensure expenses is a list (not None)
    assert expenses is not None

    assert len(expenses) == 0  # Expect no expenses for an invalid date


def test_fetch_expense_summary_invalid_range():
    """
    Tests the `fetch_expense_summary` function with an invalid date range.

    This test case checks if the function returns an empty list when the provided date range is invalid.
    """
    summary = db_helper.fetch_expense_summary("2099-01-01", "2099-12-31")

    # Ensure the summary is an empty list
    assert summary is not None
    assert len(summary) == 0
