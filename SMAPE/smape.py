import numpy as np


def smape(y_true: np.array, y_pred: np.array) -> float:
    """Return fixed sMAPE"""

    denominator = np.abs(y_true) + np.abs(y_pred)
    smape_values = np.where(
        denominator == 0, 0, 2 * np.abs(y_true - y_pred) / denominator
    )

    return np.mean(smape_values)
