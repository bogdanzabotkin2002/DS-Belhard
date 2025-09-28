Т.к. размер датасета очень большой, то из-за проблем с вычислительными мощностями ноутбука для некоторых классификаторов пришлось
ограничиться изначальным заданием параметров, а не их подбором через gridsearch.

Тем не менее полученные результаты (сравнение решил проводить через macro avg для precision/recall):
GradientBoost:
<img width="260" height="110" alt="image" src="https://github.com/user-attachments/assets/74cc72da-9a12-4a5d-a05c-68b3616f31b0" />
LightGBM:
XGBoost
DecisionTree
Stack(Base:LGBM + XGB, Meta: DecisionTree):
