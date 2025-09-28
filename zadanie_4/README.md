Т.к. размер датасета очень большой, то из-за проблем с вычислительными мощностями ноутбука для некоторых классификаторов пришлось
ограничиться изначальным заданием параметров, а не их подбором через gridsearch.

Тем не менее полученные результаты:
GradientBoost:<img width="532" height="231" alt="image" src="https://github.com/user-attachments/assets/0af3a520-de3a-4a18-8432-4be7bfa4122e" />

LightGBM:
XGBoost
DecisionTree
Stack(Base:LGBM + XGB, Meta: DecisionTree):
