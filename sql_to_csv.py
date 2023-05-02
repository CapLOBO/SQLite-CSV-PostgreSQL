import sqlite3
import csv


# Подключаемся к базе данных
conn = sqlite3.connect('db.sqlite3')

# Создаем курсор для выполнения запросов
cursor = conn.cursor()

cursor.execute('''
    UPDATE crime_crimescene
SET created_at = datetime(strftime('%s', '2023-05-02 00:00:00') + abs(random()) % 
(strftime('%s', '2023-05-02 23:59:59') - strftime('%s', '2023-05-02 00:00:00')), 'unixepoch');
    ''')
# Выполняем SQL-запрос для объединения колонок и выборки данных
cursor.execute('''
    SELECT longitude,latitude,city||','||street||','||house AS address, created_at
    FROM crime_crimescene
    ''')

rows = cursor.fetchall()

for row in rows:
    print(row)

with open('outp5-02.csv', 'w', newline='') as file:
    # Создание объекта writer с delimiter=','
    writer = csv.writer(file, delimiter=',')

    # Запись значений в CSV-файл
    for row in rows:
        writer.writerow(row)

# Закрываем соединение с базой данных
conn.close()
