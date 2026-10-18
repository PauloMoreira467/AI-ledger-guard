import pandas as pd


def rule_weekend(df: pd.DataFrame) -> pd.Series:
    """
    Flag lines entered on a Saturday or Sunday.
    
    Uses entered_date (when someone actually did the work), not posting_date (the accounting date).
    Returns true or false per line of df
    """
    
    entered = pd.to_datetime(df["entered_date"])
    return entered.dt.dayofweek >= 5
