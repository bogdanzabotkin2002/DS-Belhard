import sqlite3 as sql


def create_base(name_base: str):
  database = sql.connect(name_base + '.db')
  cursor = database.cursor()
  return cursor

def create_table(cursor, table_name: str, columns_sql: dict):
    try:
        columns_sql_str = ",\n    ".join([f"{name} {data_type}" for name, data_type in columns_sql.items()])
        query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                      {columns_sql_str})"""
        cursor.execute(query)
        print(f'Таблица {table_name} успешно создана')
    except Exception as e:
        print(f'Ошибка: {e}')

def insert_in_table(df, cursor, table_name, columns_df: dict):
    try:
        columns_list = list(columns_df.keys())
        placeholders = '(' + ','.join(['?' for _ in range(len(columns_list))]) + ')'
        bd = df[columns_list]
        data_tuples = [tuple(row[col] for col in columns_list) for _, row in bd.iterrows()]
        query = f"INSERT INTO {table_name} VALUES {placeholders}"
        cursor.executemany(query, data_tuples)        
    except Exception as e:
        print(f"Ошибка: {e}")


