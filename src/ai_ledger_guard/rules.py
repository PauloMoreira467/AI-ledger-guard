import pandas as pd


def rule_weekend(df: pd.DataFrame) -> pd.Series:
    """
    Flag lines entered on a Saturday or Sunday.
    Uses entered_date (when someone actually did the work), not posting_date (the accounting date).
    Returns True or False per line of df
    """
    
    entered = pd.to_datetime(df["entered_date"])
    return entered.dt.dayofweek >= 5


def rule_round_amount(df: pd.DataFrame) -> pd.Series:
    """
    Flag lines whose amount is a multiple of 100 (e.g. 500.00, 1200.00).

    Real invoices usually have cents; round amounts can point to estimates or made-up entries.
    Returns True or False per line of df.
    """
    return df["amount"] % 100 == 0


def rule_rare_account(df: pd.DataFrame, min_lines: int = 100) -> pd.Series:
    """
    Flag lines posted to an account that has fewer than min_lines lines in the whole ledger.

    Rarely used accounts can point to postings to a wrong or unusual account.
    Returns True or False per line of df.
    """
    lines_per_account = df["gl_account"].value_counts()
    account_lines = df["gl_account"].map(lines_per_account)
    return account_lines < min_lines

