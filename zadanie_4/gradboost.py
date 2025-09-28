import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, accuracy_score, roc_auc_score, roc_curve, auc



def GBoost(X_train, X_test, y_train, y_test, target):
    clf = GradientBoostingClassifier(n_estimators=100,learning_rate=0.5)
    clf.fit(X_train,y_train)
    return clf

def evaluate(clf, X_test, y_test):      
    y_pred = clf.predict(X_test)

    # Генерация отчета о классификации
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    # Вывод отчета
    print(f'Accuracy: {accuracy:.2f}')
    print("Classification Report:")
    print(report)

def roc_auc(clf, X_test, y_test):
    y_proba = clf.predict_proba(X_test)[:, 1]
    fpr, tpr, thresholds = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)
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