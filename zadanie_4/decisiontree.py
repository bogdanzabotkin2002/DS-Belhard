from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, accuracy_score, roc_curve, auc, roc_auc_score
import matplotlib as plt

def dt_classify(X_train, y_train):
  param_grid = {
    'max_depth': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'max_features': [int, float, 'sqrt', 'log2']
    }

  dt_classifier = DecisionTreeClassifier(random_state=42)

  grid_search = GridSearchCV(
      estimator=dt_classifier,
      param_grid=param_grid,
      cv=5,
      scoring='accuracy')

  grid_search.fit(X_train, y_train)
  best_clf = grid_search.best_estimator_
  return best_clf

def evaluate(X_test, y_test, best_clf):
    # Использование лучшей модели для прогнозирования
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