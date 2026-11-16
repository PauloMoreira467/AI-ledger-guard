import pandas as pd


def precision_recall(alerts: pd.Series, labels: pd.Series) -> tuple[float, float]:
    """
    Compare alerts with labels (both True/False, one value per posting).

    Precision: of the alerts, the share that are anomalies.
    Recall: of the anomalies, the share that got an alert.
    """
    true_positives = (alerts & labels).sum()
    precision = true_positives / alerts.sum()
    recall = true_positives / labels.sum()
    return precision, recall
