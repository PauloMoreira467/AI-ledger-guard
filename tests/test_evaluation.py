import pandas as pd

from ai_ledger_guard.evaluation import *


def test_precision_recall_with_different_values():
    df = pd.DataFrame({
        "alert": [True, True, True, True, False],
        "label": [True, False, False, False, True],
    })

    precision, recall = precision_recall(df["alert"], df["label"])

    assert precision == 0.25  # 1 hit out of 4 alerts
    assert recall == 0.5  # 1 hit out of 2 anomalies
