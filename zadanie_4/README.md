Т.к. размер датасета очень большой, то из-за проблем с вычислительными мощностями ноутбука для некоторых классификаторов пришлось
ограничиться изначальным заданием параметров, а не их подбором через gridsearch. Наилучшим образом повели себя решающее дерево и ЛГБМ. Полноценно их сравнить не могу,
т.к. подбор парамаетров для лгбм занимает около 10 а то и более минут

Тем не менее полученные результаты (сравнение решил проводить через macro avg для precision/recall):

GradientBoost: AUC=0.85

<img width="280" height="130" alt="image" src="https://github.com/user-attachments/assets/74cc72da-9a12-4a5d-a05c-68b3616f31b0" />

LightGBM: AUC=0.96

<img width="280" height="130" alt="image" src="https://github.com/user-attachments/assets/ca7257cf-debd-47cf-97c3-20c96df51f0e" />

XGBoost: AUC=0.81

<img width="280" height="130" alt="image" src="https://github.com/user-attachments/assets/db12f9a3-b74a-4f8f-bb96-1f5cdf6aca1c" />

DecisionTree: AUC=0.97

<img width="280" height="130" alt="image" src="https://github.com/user-attachments/assets/9c57a41b-6428-40b6-a2cd-799be977bbbf" />

Stack(Base:LGBM + XGB, Meta: DecisionTree): AUC=0.87

<img width="280" height="130" alt="image" src="https://github.com/user-attachments/assets/710e5bfe-2741-4fbf-8a4d-6f6afaea88e5" />
