import pandas as pd

from ai_ledger_guard.rules import *


def test_rule_weekend_flags_saturday_and_sunday():
    df = pd.DataFrame({
        "entered_date": [
            "2023-06-02 10:00:00", # Friday
            "2023-06-03 10:00:00", # Saturday
            "2023-06-04 10:00:00", # Sunday
            "2023-06-05 10:00:00", # Monday
        ]
    })
    
    result = rule_weekend(df)
    
    assert result.tolist() == [False, True, True, False]
    
    
def test_rule_weekend_around_midnight_flags_saturday_and_sunday():
    df = pd.DataFrame({
        "entered_date": [
            "2023-06-02 23:59:59", # Friday
            "2023-06-03 00:00:00", # Saturday
            "2023-06-04 23:59:59", # Sunday
            "2023-06-05 00:00:00", # Monday
        ]
    })
    
    result = rule_weekend(df)
    
    assert result.tolist() == [False, True, True, False]
    
    
def test_rule_round_amount_flags_multiples_of_100():
    df = pd.DataFrame({
        "amount": [500.0, 1200.0, 112.42, 150.0],
    })

    result = rule_round_amount(df)

    assert result.tolist() == [True, True, False, False]


def test_rule_rare_account_flags_accounts_below_min_lines():
    df = pd.DataFrame({
        "gl_account": [1600, 1600, 1600, 1000, 1000, 1200],
    })

    result = rule_rare_account(df, min_lines=2)

    assert result.tolist() == [False, False, False, False, False, True]
