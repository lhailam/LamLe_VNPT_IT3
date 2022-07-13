|Nga`y|Nhi�?m vu?|
|----|-----|
|Thu� 2| Python co ba?n|
|Thu� 3|M�i tru?ng ?o pipenv|
|Thu� 4|Ti`m hi�?u v�` SQL (SQLite, NoSQL vs SQL)|
|Thu� 5|T�m hi?u v? Git |
|Thu� 6|T�m hi?u v? Git |
***
# 1. Python co ba?n
Ti`m hi�?u theo suo`n : https://unica.vn/lap-trinh-python-tu-zero-hero
# 2. M�i tru?ng ?o pipenv
## C�c v?n d? m� Pipenv gia?i quy�t:
* B?n kh�ng c�n c?n ph?i s? d?ng pip v� virtualenv ri�ng bi?t. Ch�ng l�m vi?c c�ng nhau.
* Vi?c qu?n l� t?p requirements.txt c� th? c� v?n d?, v� v?y Pipenv s? d?ng Pipfile v� Pipfile.lock d? t�ch c�c khai b�o ph? thu?c tr?u tu?ng kh?i k?t h?p du?c th? nghi?m cu?i c�ng.
* Hash du?c s? d?ng ? m?i noi, m?i l�c. An to�n
* Khuy?n kh�ch m?nh m? vi?c s? d?ng c�c phi�n b?n ph? thu?c m?i nh?t d? gi?m thi?u r?i ro b?o m?t ph�t sinh t? c�c th�nh ph?n l?i th?i.
* Cung c?p cho b?n c�i nh�n s�u s?c v? bi?u d? ph? thu?c c?a b?n
* H?p l� h�a quy tr�nh ph�t tri?n b?ng c�ch t?i c�c t?p .env.

## Thao ta�c ca`i thu vi�?n va` su? du?ng pipenv:
- C�i d?t m�i tru?ng ?o Pipenv: pip install pipenv
- T?o m�i tru?ng ?o cho t?ng project: pipenv install
- C�i d?t c�c thu vi?n: pipenv install name_library
- K�ch ho?t m�i tru?ng d? s? d?ng: pipenv shell
- T?o file requirement: $pipenv lock -r > requirements.txt

# 3. Ti`m hi�?u v�` Database
## SQLite la` gi`?

    SQLite l� h? qu? tr? co s? d? li?u (DBMS) quan h? tuong t? nhu Mysql, ... �?c di?m n?i b?t c?a SQLite so v?i c�c DBMS kh�c l� g?n, nh?, don gi?n, d?t bi?t kh�ng c?n m� h�nh server-client, kh�ng c?n c�i d?t, c?u h�nh hay kh?i d?ng n�n kh�ng c� kh�i ni?m user, password hay quy?n h?n trong SQLite Database. D? li?u cung du?c luu ? m?t file duy nh?t.
## Cu� pha�p trong SQLite
|STT|C� ph�p|� nghia|
|---|-------------------|------------|
|1	|sqlite3 <name.db>	|T?o database|
|||
|2	|ATTACH DATABASE �<databasename>� As �<alias-name>�;|	S? d?ng database, c� th? d?t alias cho database v� s? d?ng nhu t�n c?a database, m?i m?t l?n g?i l?nh s? d?ng th� ta c� th? s? d?ng t�n alias kh�c nhau|
|3	|DETACH DATABASE �<name-name>�;	|X�a co s? d? li?u s? d?ng v?i t�n alias|
|4	|CREATE TABLE <databasename.tablename>();	|T?o b?ng|
|5	|DROP TABLE database_name.table_name;|	X�a b?ng|
|6	| INSERT INTO  table_name [(column1, column2,..)] VALUES (value1, value2,..); |	Th�m d? li?u v�o b?ng|
|7	|INSERT INTO table1 [(column�)] SELECT column FROM table2 [WHERE];|	Ch�n d? li?u v�o b?ng t? m?t b?ng kh�c
|8	|SELECT sql FROM table;|	Hi?n th? th�ng tin b?ng|
|9	|SELECT ( 12+8) AS ADDITION; #20|	Th?c hi?n bi?u th?c s? h?c|
|10	|SELECT COUNT(*) AS �RECORDS� FROM table;|	d?m b?ng ghi trong b?ng|
|11	|SELECT CURRENT_TIMESTAMP;|	Hi?n th? th?i gian h? th?ng|
|12	|UPDATE table_name SET column1 = value,... WHERE ..;	|Update d? li?u b?ng|
|13	|DELETE FROM table_name WHERE �;	|X�a b?n ghi|
|14	|PRAGMA pragma_name;|	�i?u khi?n c�c bi?n m�i tru?ng v� c�c flag tr?ng th�i da d?ng|
|15	|PRAGMA pragma_name = value;	|Thi?t l?p gi� tr?|
|16	|SELECT ... FROM table1 CROSS JOIN table2 ...	CROSS JOIN:| k?t n?i m?i h�ng c?a b?ng d?u ti�n v?i m?i h�ng c?a b?ng th? hai|
|17	|SELECT ... FROM table1 [INNER] JOIN table2 ON conditional_expression ...|	INNER JOIN|
|18	|SELECT ... FROM table1 LEFT OUTER JOIN table2 ON conditional_expression ...	|OUTER JOIN: ch? h? tr? LEFT JOIN|

## So s�nh co b?n gi?a SQL v� NoSQL:
||SQL|NoSQL|
|--------|------|-----|
|Ng�n ng?|	S? d?ng ng�n ng? truy v?n c� c?u tr�c.	|S? d?ng ng�n ng? truy v?n kh�g c?u tr�c. D? li?u du?c luu tr? du?i d?ng bi?u d?, m� h�nh, vector, etc�|
|C?u tr�c|	Bi?u th? d? li?u du?i d?ng b?ng, h�ng v� c?t.	|Bi?u th? d? li?u du?i d?ng bi?u d?, c�c c?p kh�a-gi� tr? v� nhi?u hon th?.
|Kh? nang m? r?ng	|CSDL SQL c� th? du?c thu nh? theo chi?u d?c, du?c m? r?ng b?ng c�ch tang luu lu?ng ph?n c?ng.|	�u?c t�y bi?n theo chi?u ngang, m? r?ng b?ng c�ch tang s? lu?ng m�y ch? CSDL.
|Ng�n ng?| Query	S? d?ng ng�n ng? Query|	Kh�ng c� ng�n ng? Query
|Ph?n m?m|	MySql, Oracle, Ms-SQL.	| MongoDB, Cassandra, HBase, CouchDB.

# 4. Ti`m hi�?u v�` GIT


    -C?u h�nh t�n t�i kho?n tr�n local: git config �global user.name [username].
    -C?u h�nh email tr�n local: git config -global user.email [youremail].
    -T?i source v? local dang g?i : git clone [url].
    -T?o k?t n?i tr�n local: git init.
    -Th�m c�c file c?n t?i l�n v�o index: git add [namefile].
    -T?o commit t? local v?i sever: git commit -m "message".
    -T?o nh�nh m?i: git branch [namebranch].
    -Truy c?p v�o nh�nh: git checkout [namebranch].
    -G?p nh�nh: git merge -T?i soure: git pull -T?o k?t n?i v?i server: git remote add origin [url].
    -T?i source t? local l�n server: git push -u origin [namebranch].