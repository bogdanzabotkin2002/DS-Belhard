import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
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
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        return None

def explore_data(df):
    """Исследование данных."""
    print("Информация о данных:")
    print(f"Размер: {df.shape}")
    print(f"Колонки: {list(df.columns)}")
    print("\nПропущенные значения:")
    print(df.isnull().sum())

def diagram(df, col_x: str, col_y: str):
  """col_x: название столбца из датафрэйма по оси х
     col_y: название столбца из датафрэйма по оси у
     heatmap: тепловая матрица корреляции по дефолту False
  """
  return sns.scatterplot(x = df[col_x], y = df[col_y])

def heatmap(df: pd.DataFrame):
    return sns.heatmap(df.corr())

def boost_preprocessing(df: pd.DataFrame, target: str):
    df = df.dropna()
    X = df.drop(target, axis=1)
    y = df[target]
    return train_test_split(X, y, test_size=0.5,random_state=42, stratify=y )

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




