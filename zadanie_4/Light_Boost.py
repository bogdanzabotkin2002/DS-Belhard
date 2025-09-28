import pandas as pd
import lightgbm as lgb
import matplotlib as plt
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import classification_report, accuracy_score, roc_curve, auc, roc_auc_score


def LGBoost(X_train, X_test, y_train, y_test):
    param_grid = {
      'learning_rate': [0.02, 0.05, 0.1],
      'num_leaves': [30, 40, 50]}

    clf = lgb.LGBMClassifier(class_weight='balanced')

    grid_search = GridSearchCV(
    estimator=clf,
    param_grid=param_grid,
    cv=5,
    scoring='accuracy')

    grid_search.fit(X_train, y_train)

    # Вывод лучших параметров и точности
    print("Лучшие параметры:", grid_search.best_params_)
    print("Лучшая точность (CV):", grid_search.best_score_)

    # Использование лучшей модели для прогнозирования
    best_clf = grid_search.best_estimator_
    return best_clf

def evaluate(best_clf, X_test, y_test):    
    y_pred = best_clf.predict(X_test)

    # Оценка модели
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f'Accuracy на тестовых данных: {accuracy:.2f}')
    print('Classification Report:')
    print(report)


def roc_auc(clf, X_test, y_test):
    y_proba = clf.predict_proba(X_test)[:, 1]

    fpr, tpr, thresholds = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(6,6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, 
              label=f'ROC curve (AUC = {roc_auc:.3f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
    plt.show()

    # Можно также напрямую вычислить AUC
    print(f"ROC AUC score: {roc_auc_score(y_test, y_proba):.3f}") 