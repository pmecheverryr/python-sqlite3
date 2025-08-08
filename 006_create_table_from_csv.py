import sqlite3
import csv

file_csv = 'data/iris.csv'
table_name = 'iris'

with sqlite3.connect("test_from_csv.db") as conn:
    cursor = conn.cursor()

    # CSV obtenido desde Kaggle
    # https://www.kaggle.com/datasets/saurabh00007/iriscsv?resource=download
    with open(file_csv, 'r') as f:
        reader = csv.reader(f)
        column_names = next(reader)

        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_names)});")

        for row in reader:
            cursor.execute(f"INSERT INTO {table_name} VALUES ({', '.join('?' for _ in range(len(row)))})", row)

    conn.commit()

    cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
    result = cursor.fetchall()
    print(result)