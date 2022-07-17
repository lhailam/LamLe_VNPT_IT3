# Báo cáo công việc đã làm

## 1. Tìm hiểu về SQLite
### 1.1 SQLite là gì?
SQLite là hệ quả trị cơ sở dữ liệu (DBMS) quan hệ tương tự như Mysql, ... Đặc điểm nổi bật của SQLite so với các DBMS khác là gọn, nhẹ, đơn giản, đặt biệt không cần mô hình server-client, không cần cài đặt, cấu hình hay khởi động nên không có khái niệm user, password hay quyền hạn trong SQLite Database. Dữ liệu cũng được lưu ở một file duy nhất.
### 1.2 Ứng dụng chủ yếu của SQLite
* Cơ sở dữ liệu cho Internet Of Things.
* Định dạng tệp ứng dụng.
* Cơ sở dữ liệu cho web

### 1.3 Cú pháp cơ bản
|Cú pháp| Ý nghĩa|
|----|----|
|sqlite3 <name.db>|Tạo database|
CREATE TABLE <databasename.tablename>();|Tạo bảng|
|	INSERT INTO table_name [(column1, column2,..)] VALUES (value1, value2,..);|Thêm dữ liệu vào bảng|
|INSERT INTO table1 [(column…)] SELECT column FROM table2 [WHERE];|Chèn dữ liệu vào bảng từ một bảng khác|
|SELECT sql FROM table;|Hiển thị thông tin bảng|
|	UPDATE table_name SET column1 = value,... WHERE ..;|Update dữ liệu bảng|
|DELETE FROM table_name WHERE …;|	Xóa bản ghi|
### 1.4 Các ràng buộc khi tạo cơ sở dữ liệu:
 Các ràng buộc sau thường được sử dụng trong SQL:

* NOT NULL- Đảm bảo rằng một cột không thể có giá trị NULL
* UNIQUE- Đảm bảo rằng tất cả các giá trị trong một cột là khác nhau
* PRIMARY KEY- Sự kết hợp của a NOT NULLvà UNIQUE. Xác định duy nhất từng hàng trong bảng
* FOREIGN KEY - Ngăn chặn các hành động phá hủy liên kết giữa các bảng
* CHECK- Đảm bảo rằng các giá trị trong một cột thỏa mãn một điều kiện cụ thể
* DEFAULT- Đặt giá trị mặc định cho một cột nếu không có giá trị nào được chỉ định
* CREATE INDEX- Dùng để tạo và lấy dữ liệu từ cơ sở dữ liệu rất nhanh chóng
# 2. Tìm hiểu về HTTP METHODS, POST, GET, PUT, DELETE


|Method	| Description|
|---|---|
|delete(url, args)|	Sends a DELETE request to the specified url|
|get(url, params, args) |	Sends a GET request to the specified url|
|post(url, data, json, args) |	Sends a POST request to the specified url|
|put(url, data, args) |	Sends a PUT request to the specified url|
|request(method, url, args) |	Sends a request of the specified method to the specified url |

# 3. Yêu cầu thực hiện
```
Tạo 1 bảng dữ liệu bao gồm:
NHANVIEN
idNhanVien (string) suggest sử dụng uuidv4
tenNhanVien (string) 
CCCD (string) <- unique (duy nhất)
email (string) <- unique (duy nhất)
phone (string) <- unique (duy nhất)
Đầu ra: 5 APIs, sử dụng Postman để kiểm tra API nha
1. API danh sách nhân viên Method: GET
2. API tạo nhân viên: POST -> tạo thành công thì gửi email thông báo đến nhân viên đó
3. API cập nhật nhân viên Method: POST / PUT
4. API thông tin nhân viên Method: GET
5. API xóa nhân viên Method: DELETE
```
# 4 Kết quả đạt được
## Sử dụng Postman để kiểm tra API:
### 1. API danh sách nhân viên Method: GET
<img src="https://github.com/lhailam/LamLe_VNPT_IT3/blob/main/Tuan2/Nhanvien_SQLite/image/show.PNG">

### 2. API tạo nhân viên: POST
<img src="https://github.com/lhailam/LamLe_VNPT_IT3/blob/main/Tuan2/Nhanvien_SQLite/image/insert.PNG">

### 3. API cập nhật nhân viên Method: PUT
<img src="https://github.com/lhailam/LamLe_VNPT_IT3/blob/main/Tuan2/Nhanvien_SQLite/image/update.PNG">

### 4. API thông tin nhân viên Method: GET
<img src="https://github.com/lhailam/LamLe_VNPT_IT3/blob/main/Tuan2/Nhanvien_SQLite/image/infor.PNG">

### 5. API xóa nhân viên Method: DELETE
<img src="https://github.com/lhailam/LamLe_VNPT_IT3/blob/main/Tuan2/Nhanvien_SQLite/image/delete.PNG">
