Размеры датасета
Строк: 852
Столбцов: 4
============================================================
Кол-во пропущенных значений: 0
============================================================
Колонки и их типы:
---  ------                       --------------  -----  
 0   Учетный день                 852 non-null    object 
 1   Количество гостей            852 non-null    int64  
 2   Сумма без скидки, р.         852 non-null    float64
 3   Средняя выручка с гостя, р.  852 non-null    float64
============================================================
Пропусков нет
==================================================
АНАЛИЗ РАСПРЕДЕЛЕНИЯ ДАННЫХ
==================================================
Общее количество наблюдений: 852
Минимум: 167.01
Максимум: 2075.50
Среднее: 1040.98
Медиана: 1070.78
Стандартное отклонение: 351.61
Асимметрия: -0.409
Эксцесс: -0.362
Тест на нормальность: p-value = 0.000001
Данные НЕ нормальные
====================================================
АНАЛИЗ ВЫБРОСОВ:
Q1 (25-й перцентиль): 843.04
Q3 (75-й перцентиль): 1298.75
IQR: 455.71
Нижняя граница: 159.48
Верхняя граница: 1982.31
Количество выбросов: 1
Процент выбросов: 0.12%
====================================================Графики распределений и корреляции====================================================
ADF Statistic: -2.939796
p-value: 0.040912
	1%: -3.438
	5%: -2.865
	10%: -2.569
==================================================
После дифференциации
ADF Statistic: -2.939796
p-value: 0.040912
	1%: -3.438
	5%: -2.865
	10%: -2.569

ARIMA for not diff
Лучшие параметры: {'p': 11, 'd': 0, 'q': 12}
Mean Absolute Error (MAE): 241.550
R^2: 0.109
Root Mean Squared Error (RMSE): 321.817
Mean Absolute Percentage Error (MAPE): 0.403%

SARIMA for not diff
Лучшие параметры: {'p': 2, 'd': 1, 'q': 4, 'P': 2, 'D': 0, 'Q': 1, 'm': 7}
Mean Absolute Error (MAE): 471.308
R^2: -1.928
Root Mean Squared Error (RMSE): 583.272
Mean Absolute Percentage Error (MAPE): 77.226%

ARIMA for diff
Лучшие параметры: {'p': 9, 'd': 0, 'q': 9}
Mean Absolute Error (MAE): 294.495
R^2: 0.096
Root Mean Squared Error (RMSE): 391.341
Mean Absolute Percentage Error (MAPE): 1.457%

SARIMA for diff
Лучшие параметры: {'p': 4, 'd': 0, 'q': 2, 'P': 0, 'D': 1, 'Q': 4, 'm': 7}
Mean Absolute Error (MAE): 295.134
R^2: 0.111
Root Mean Squared Error (RMSE): 388.054
Mean Absolute Percentage Error (MAPE): 43.840%

GRU
Mean Absolute Error (MAE): 131.448
R^2: 0.659
Root Mean Squared Error (RMSE): 188.851
Mean Absolute Percentage Error (MAPE): 0.155%

AUTOENCODER
Mean Absolute Error (MAE): 0.067
R^2: 0.992
Root Mean Squared Error (RMSE): 0.087
Mean Absolute Percentage Error (MAPE): 0.267%

STACKING(base: random_forest+LGBM+RIDGE,  meta: XGBR)
tree_based: MAE = 23.55
 R^2 = 0.99
boosting: MAE = 15.44
 R^2 = 0.99
linear: MAE = 43.20
 R^2 = 0.96
Stacking MAE = 47.67
Stacking R^2 = 0.95









