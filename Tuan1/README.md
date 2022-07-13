|Nga`y|Nhiê?m vu?|
|----|-----|
|Thu´ 2| Python co ba?n|
|Thu´ 3|Môi tru?ng ?o pipenv|
|Thu´ 4|Ti`m hiê?u vê` SQL (SQLite, NoSQL vs SQL)|
|Thu´ 5|Tìm hi?u v? Git |
|Thu´ 6|Tìm hi?u v? Git |
***
# 1. Python co ba?n
Ti`m hiê?u theo suo`n : https://unica.vn/lap-trinh-python-tu-zero-hero
# 2. Môi tru?ng ?o pipenv
## Các v?n d? mà Pipenv gia?i quyê´t:
* B?n không còn c?n ph?i s? d?ng pip và virtualenv riêng bi?t. Chúng làm vi?c cùng nhau.
* Vi?c qu?n lý t?p requirements.txt có th? có v?n d?, vì v?y Pipenv s? d?ng Pipfile và Pipfile.lock d? tách các khai báo ph? thu?c tr?u tu?ng kh?i k?t h?p du?c th? nghi?m cu?i cùng.
* Hash du?c s? d?ng ? m?i noi, m?i lúc. An toàn
* Khuy?n khích m?nh m? vi?c s? d?ng các phiên b?n ph? thu?c m?i nh?t d? gi?m thi?u r?i ro b?o m?t phát sinh t? các thành ph?n l?i th?i.
* Cung c?p cho b?n cái nhìn sâu s?c v? bi?u d? ph? thu?c c?a b?n
* H?p lý hóa quy trình phát tri?n b?ng cách t?i các t?p .env.

## Thao ta´c ca`i thu viê?n va` su? du?ng pipenv:
- Cài d?t môi tru?ng ?o Pipenv: pip install pipenv
- T?o môi tru?ng ?o cho t?ng project: pipenv install
- Cài d?t các thu vi?n: pipenv install name_library
- Kích ho?t môi tru?ng d? s? d?ng: pipenv shell
- T?o file requirement: $pipenv lock -r > requirements.txt

# 3. Ti`m hiê?u vê` Database
## SQLite la` gi`?

    SQLite là h? qu? tr? co s? d? li?u (DBMS) quan h? tuong t? nhu Mysql, ... Ð?c di?m n?i b?t c?a SQLite so v?i các DBMS khác là g?n, nh?, don gi?n, d?t bi?t không c?n mô hình server-client, không c?n cài d?t, c?u hình hay kh?i d?ng nên không có khái ni?m user, password hay quy?n h?n trong SQLite Database. D? li?u cung du?c luu ? m?t file duy nh?t.
## Cu´ pha´p trong SQLite
|STT|Cú pháp|Ý nghia|
|---|-------------------|------------|
|1	|sqlite3 <name.db>	|T?o database|
|||
|2	|ATTACH DATABASE ‘<databasename>’ As ‘<alias-name>’;|	S? d?ng database, có th? d?t alias cho database và s? d?ng nhu tên c?a database, m?i m?t l?n g?i l?nh s? d?ng thì ta có th? s? d?ng tên alias khác nhau|
|3	|DETACH DATABASE ‘<name-name>’;	|Xóa co s? d? li?u s? d?ng v?i tên alias|
|4	|CREATE TABLE <databasename.tablename>();	|T?o b?ng|
|5	|DROP TABLE database_name.table_name;|	Xóa b?ng|
|6	| INSERT INTO  table_name [(column1, column2,..)] VALUES (value1, value2,..); |	Thêm d? li?u vào b?ng|
|7	|INSERT INTO table1 [(column…)] SELECT column FROM table2 [WHERE];|	Chèn d? li?u vào b?ng t? m?t b?ng khác
|8	|SELECT sql FROM table;|	Hi?n th? thông tin b?ng|
|9	|SELECT ( 12+8) AS ADDITION; #20|	Th?c hi?n bi?u th?c s? h?c|
|10	|SELECT COUNT(*) AS “RECORDS” FROM table;|	d?m b?ng ghi trong b?ng|
|11	|SELECT CURRENT_TIMESTAMP;|	Hi?n th? th?i gian h? th?ng|
|12	|UPDATE table_name SET column1 = value,... WHERE ..;	|Update d? li?u b?ng|
|13	|DELETE FROM table_name WHERE …;	|Xóa b?n ghi|
|14	|PRAGMA pragma_name;|	Ði?u khi?n các bi?n môi tru?ng và các flag tr?ng thái da d?ng|
|15	|PRAGMA pragma_name = value;	|Thi?t l?p giá tr?|
|16	|SELECT ... FROM table1 CROSS JOIN table2 ...	CROSS JOIN:| k?t n?i m?i hàng c?a b?ng d?u tiên v?i m?i hàng c?a b?ng th? hai|
|17	|SELECT ... FROM table1 [INNER] JOIN table2 ON conditional_expression ...|	INNER JOIN|
|18	|SELECT ... FROM table1 LEFT OUTER JOIN table2 ON conditional_expression ...	|OUTER JOIN: ch? h? tr? LEFT JOIN|

## So sánh co b?n gi?a SQL và NoSQL:
||SQL|NoSQL|
|--------|------|-----|
|Ngôn ng?|	S? d?ng ngôn ng? truy v?n có c?u trúc.	|S? d?ng ngôn ng? truy v?n khôg c?u trúc. D? li?u du?c luu tr? du?i d?ng bi?u d?, mô hình, vector, etc…|
|C?u trúc|	Bi?u th? d? li?u du?i d?ng b?ng, hàng và c?t.	|Bi?u th? d? li?u du?i d?ng bi?u d?, các c?p khóa-giá tr? và nhi?u hon th?.
|Kh? nang m? r?ng	|CSDL SQL có th? du?c thu nh? theo chi?u d?c, du?c m? r?ng b?ng cách tang luu lu?ng ph?n c?ng.|	Ðu?c tùy bi?n theo chi?u ngang, m? r?ng b?ng cách tang s? lu?ng máy ch? CSDL.
|Ngôn ng?| Query	S? d?ng ngôn ng? Query|	Không có ngôn ng? Query
|Ph?n m?m|	MySql, Oracle, Ms-SQL.	| MongoDB, Cassandra, HBase, CouchDB.

# 4. Ti`m hiê?u vê` GIT


    -C?u hình tên tài kho?n trên local: git config –global user.name [username].
    -C?u hình email trên local: git config -global user.email [youremail].
    -T?i source v? local dang g?i : git clone [url].
    -T?o k?t n?i trên local: git init.
    -Thêm các file c?n t?i lên vào index: git add [namefile].
    -T?o commit t? local v?i sever: git commit -m "message".
    -T?o nhánh m?i: git branch [namebranch].
    -Truy c?p vào nhánh: git checkout [namebranch].
    -G?p nhánh: git merge -T?i soure: git pull -T?o k?t n?i v?i server: git remote add origin [url].
    -T?i source t? local lên server: git push -u origin [namebranch].