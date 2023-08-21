import random
import psycopg2
import csv

conn = psycopg2.connect(
    host="HOST",
    database="DB_NAME",
    user="USERNAME",
    port="PORT",
    password="PASSWORD"
)

cursor = conn.cursor()

with open('outp5-02.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)

    for row in reader:
        cursor.execute(
            "INSERT INTO incident (longitude, latitude, address, category, is_predictive, is_active, created_at) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], random.choice(['Преступление', 'ДТП', 'Пожар']), 'false',
             random.choice(['true', 'false']), row[3])
        )
        print(row)

conn.commit()
conn.close()
