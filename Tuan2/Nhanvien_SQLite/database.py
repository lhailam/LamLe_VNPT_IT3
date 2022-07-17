import sqlite3

conn = sqlite3.connect("db_nhanvien.sqlite")

cursor = conn.cursor()
sql_query = """ CREATE TABLE nhanvien (
    id_nhanvien text PRIMARY KEY,
    ten_nhanvien text NOT NULL,
    cccd text UNIQUE,
    email text UNIQUE,
    phone text UNIQUE
)"""

cursor.execute(sql_query)