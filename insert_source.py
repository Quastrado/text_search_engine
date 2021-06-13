import csv

import psycopg2

from app.config import settings


connection_string = f"host=db port=5432 dbname={settings.POSTGRES_DB} user={settings.POSTGRES_USER} password={settings.POSTGRES_PASSWORD}"
conn = psycopg2.connect(connection_string)
cur = conn.cursor()

with open("app/resources/posts.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cur.execute(
            "INSERT INTO posts(text, created_date, rubrics) VALUES (%s, %s, %s)",
            row
        )
conn.commit()
