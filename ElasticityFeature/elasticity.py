import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def elasticity_df(df: pd.DataFrame) -> pd.DataFrame:
    # Создаем DataFrame для хранения результатов
    elasticity_results = []

    # Перебираем каждый SKU по отдельности
    for sku, group in df.groupby("sku"):
        # Достаем значения цены и логарифм количества продаж (qty)
        X = group["price"].values.reshape(-1, 1)
        y = np.log(group["qty"] + 1)

        # Создаем и обучаем модель линейной регрессии
        model = LinearRegression()
        model.fit(X, y)

        # Предсказываем значения и вычисляем R^2
        y_pred = model.predict(X)
        r2 = r2_score(y, y_pred)

        # Добавляем SKU и R^2 в список результатов
        elasticity_results.append({"sku": sku, "elasticity": r2})

    # Преобразуем список результатов в DataFrame и возвращаем
    result_df = pd.DataFrame(elasticity_results)
    return result_df
