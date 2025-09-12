import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, root_mean_squared_error
import seaborn as sns


def load_data(file_path, csv=True, parquet=False, json=False, excel=False):
    """file_path: путь к файлу с датафрэймом
       csv, parquet, json, excel: указываем True для расширения файла
    """
    try:
      if csv == True:
        return pd.read_csv(file_path)
      elif parquet == True:
        return pd.read_parquet(file_path)
      elif json == True:
        return pd.read_json(file_path)
      elif excel == True:
        return pd.read_excel(file_path)
    except FileNotFoundError:
      print("Файл не найден или неправильный формат расширения")

def diagram(df, col_x: str, col_y: str, heatmap=False):
  """col_x: название столбца из датафрэйма по оси х
     col_y: название столбца из датафрэйма по оси у
     heatmap: тепловая матрица корреляции по дефолту False
  """
  sns.scatterplot(x = df[col_x], y = df[col_y])
  if heatmap == True:
    return sns.heatmap(df.corr()), sns.scatterplot(x = df[col_x], y = df[col_y])
  else:
    return sns.scatterplot(x = df[col_x], y = df[col_y])

def preprocessing(df, target_column):
  """target_column: целевой столбец
  """
  try:
    X = df.drop(columns=[target_column])
    y = df[target_column]

    numeric_features = ['Yearly % Change', 'Yearly % Change', 'Migrants (net)', 'Median Age',
                          'Fertility Rate', 'Density (P/Km²)', 'Urban Pop %',	'Urban Population',	"Country's Share of World Pop",
                          'World Population',	'U.S. Global Rank'
                        ]
      
    numeric_transformer = StandardScaler()
      
    preprocessor = ColumnTransformer(
                  transformers=[('num', numeric_transformer, numeric_features)]
                  )

    X_processed = preprocessor.fit_transform(X)

    return X_processed, y, preprocessor
  except KeyError:
      print("Перепроверьте имя целевого столбца")

def train_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict(model, X):
    return model.predict(X)

def evaluate_model(y_true, y_pred):
  """rmse: корень из средней квадратичной ошибки, 
           использую т.к. mse порядка 10^12
     r2: коэффициент детерминации, для хорошей модели (0.5, 1)
  """
  try:
      rmse = root_mean_squared_error(y_true, y_pred)
      r2 = r2_score(y_true, y_pred)
      return print(f"Среднеквадратичная ошибка: {rmse:.2f}", 
            f"Коэффициент детерминации R^2: {r2:.2f}", sep='\n')
  except r2 <=0.5:
      print(f'Коэффициент детерминации  {r2:.2f}<0.5')

def visualization(y_test, y_pred):
    plt.scatter(range(6), y_pred, color='blue')
    plt.scatter(range(6), y_test, color='red')
    return plt.show()
    
