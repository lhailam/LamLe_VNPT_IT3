import sqlalchemy
import psycopg2

dbms_name = 'postgresql'
driver = 'psycopg2'
user = 'postgres'
password = '******'
host = '127.0.0.1'
port = 5432
db_name = 'Nhanvien'
conn_str = f'{dbms_name}+{driver}://{user}:{password}@{host}:{port}/{db_name}'
db_conn = sqlalchemy.create_engine(url =conn_str).connect()

print(conn_str)
print(db_conn)

#chèn
# sql = "INSERT INTO nhanvien (id_nhanvien, ten_nhanvien, cccd, email, phone) VALUES (%s, %s, %s, %s, %s)"
# val = ("2", "Lâm Lê",152225,"lehailam444@gmail.com", 9844110)
# db_conn.execute(sql, val)

#xóa
# sql = "DELETE FROM nhanvien WHERE id_nhanvien = '123'"
# sql_result = db_conn.execute(sql)

#update
# update =  "UPDATE nhanvien SET phone = '11111111' WHERE phone = '9844110'"
# db_conn.execute(update)


#Hiển thị
sql_command= "SELECT * FROM public.nhanvien "
result = db_conn.execute(sql_command)

print(result)

for row in result:
    print(row)