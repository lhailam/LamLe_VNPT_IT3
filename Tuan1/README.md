|Ngày|Nhiệm vụ|
|----|-----|
|Thứ 2| Python cơ bản|
|Thứ 3|Môi trường ảo pipenv|
|Thứ 4|Tìm hiểu về SQL (SQLite, NoSQL vs SQL)|
|Thứ 5|Tìm hiểu về Git |
|Thứ 6|Tìm hiểu về Git |
***
# 1. Python cơ bản
Tìm hiểu theo sườn : https://unica.vn/lap-trinh-python-tu-zero-hero
# 2. Môi trường ảo pipenv
## Các vấn đề mà Pipenv giải quyết:
* Bạn không còn cần phải sử dụng pip và virtualenv riêng biệt. Chúng làm việc cùng nhau.
* Việc quản lý tệp requirements.txt có thể có vấn đề, vì vậy Pipenv sử dụng Pipfile và Pipfile.lock để tách các khai báo phụ thuộc trừu tượng khỏi kết hợp được thử nghiệm cuối cùng.
* Hash được sử dụng ở mọi nơi, mọi lúc. An toàn
* Khuyến khích mạnh mẽ việc sử dụng các phiên bản phụ thuộc mới nhất để giảm thiểu rủi ro bảo mật phát sinh từ các thành phần lỗi thời.
* Cung cấp cho bạn cái nhìn sâu sắc về biểu đồ phụ thuộc của bạn
* Hợp lý hóa quy trình phát triển bằng cách tải các tệp .env.

## Thao tác cài thư viện và sử dụng pipenv:
- Cài đặt môi trường ảo Pipenv: pip install pipenv
- Tạo môi trường ảo cho từng project: pipenv install
- Cài đặt các thư viện: pipenv install name_library
- Kích hoạt môi trường để sử dụng: pipenv shell
- Tạo file requirement: pipenv lock -r > requirements.txt

# 3. Tìm hiểu về Database
## SQLite là gì?
### SQLite là hệ quả trị cơ sở dữ liệu (DBMS) quan hệ tương tự như Mysql, ... Đặc điểm nổi bật của SQLite so với các DBMS khác là gọn, nhẹ, đơn giản, đặt biệt không cần mô hình server-client, không cần cài đặt, cấu hình hay khởi động nên không có khái niệm user, password hay quyền hạn trong SQLite Database. Dữ liệu cũng được lưu ở một file duy nhất.
    
## Cú pháp trong SQLite
|STT|Cú pháp|Ý nghĩa|
|---|-------------------|------------|
|1	|sqlite3 <name.db>	|Tạo database|
|||
|2	|ATTACH DATABASE ‘<databasename>’ As ‘<alias-name>’;|	Sử dụng database, có thể đặt alias cho database và sử dụng như tên của database, mỗi một lần gọi lệnh sử dụng thì ta có thể sử dụng tên alias khác nhau|
|3	|DETACH DATABASE ‘<name-name>’;	|Xóa cơ sở dữ liệu sử dụng với tên alias|
|4	|CREATE TABLE <databasename.tablename>();	|Tạo bảng|
|5	|DROP TABLE database_name.table_name;|	Xóa bảng|
|6	| INSERT INTO  table_name [(column1, column2,..)] VALUES (value1, value2,..); |	Thêm dữ liệu vào bảng|
|7	|INSERT INTO table1 [(column…)] SELECT column FROM table2 [WHERE];|	Chèn dữ liệu vào bảng từ một bảng khác
|8	|SELECT sql FROM table;|	Hiển thị thông tin bảng|
|9	|SELECT ( 12+8) AS ADDITION; #20|	Thực hiện biểu thức số học|
|10	|SELECT COUNT(*) AS “RECORDS” FROM table;|	đếm bảng ghi trong bảng|
|11	|SELECT CURRENT_TIMESTAMP;|	Hiển thị thời gian hệ thống|
|12	|UPDATE table_name SET column1 = value,... WHERE ..;	|Update dữ liệu bảng|
|13	|DELETE FROM table_name WHERE …;	|Xóa bản ghi|
|14	|PRAGMA pragma_name;|	Điều khiển các biến môi trường và các flag trạng thái đa dạng|
|15	|PRAGMA pragma_name = value;	|Thiết lập giá trị|
|16	|SELECT ... FROM table1 CROSS JOIN table2 ...	CROSS JOIN:| kết nối mọi hàng của bảng đầu tiên với mỗi hàng của bảng thứ hai|
|17	|SELECT ... FROM table1 [INNER] JOIN table2 ON conditional_expression ...|	INNER JOIN|
|18	|SELECT ... FROM table1 LEFT OUTER JOIN table2 ON conditional_expression ...	|OUTER JOIN: chỉ hỗ trợ LEFT JOIN|

## So sánh cơ bản giữa SQL và NoSQL:
||SQL|NoSQL|
|--------|------|-----|
|Ngôn ngữ|	Sử dụng ngôn ngữ truy vấn có cấu trúc.	|Sử dụng ngôn ngữ truy vấn khôg cấu trúc. Dữ liệu được lưu trữ dưới dạng biểu đồ, mô hình, vector, etc…|
|Cấu trúc|	Biểu thị dữ liệu dưới dạng bảng, hàng và cột.	|Biểu thị dữ liệu dưới dạng biểu đồ, các cặp khóa-giá trị và nhiều hơn thế.
|Khả năng mở rộng	|CSDL SQL có thể được thu nhỏ theo chiều dọc, được mở rộng bằng cách tăng lưu lượng phần cứng.|	Được tùy biến theo chiều ngang, mở rộng bằng cách tăng số lượng máy chủ CSDL.
|Ngôn ngữ| Query	Sử dụng ngôn ngữ Query|	Không có ngôn ngữ Query
|Phần mềm|	MySql, Oracle, Ms-SQL.	| MongoDB, Cassandra, HBase, CouchDB.

# 4. Tìm hiểu về GIT


    -Cấu hình tên tài khoản trên local: git config –global user.name [username].
    -Cấu hình email trên local: git config -global user.email [youremail].
    -Tải source về local đang gọi : git clone [url].
    -Tạo kết nối trên local: git init.
    -Thêm các file cần tải lên vào index: git add [namefile].
    -Tạo commit từ local với sever: git commit -m "message".
    -Tạo nhánh mới: git branch [namebranch].
    -Truy cập vào nhánh: git checkout [namebranch].
    -Gộp nhánh: git merge -Tải soure: git pull -Tạo kết nối với server: git remote add origin [url].
    -Tải source từ local lên server: git push -u origin [namebranch].