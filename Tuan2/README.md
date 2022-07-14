|Ngày|Nhiệm vụ|
|----|----|
|Thứ 2| Tìm hiểu framework Flask|
|Thứ 3| Tìm hiểu framework Flask|
|Thứ 4| Viết API (sử dụng Flask) gửi email bằng Pyhon |
|Thứ 5| Kết hợp giữ Flask và SQLite (Tạo dự án quản lý nhân viên)|
|Thứ 6| Kết hợp giữ Flask và SQLite (Tạo dự án quản lý nhân viên)|

# 1. Framework Flask
- Flask là một Web Framework rất nhẹ của Python, dễ dàng giúp người mới bắt đầu học Python có thể tạo ra website nhỏ. Flask cũng dễ mở rộng để xây dựng các ứng dụng web phức tạp.
- Flask có nền tảng là Werkzeug và Jinja2 và nó đã trở thành một trong những Web Framework phổ biến nhất của Python

## Tính năng của Framework Flask 
- Phát triển máy chủ
- Phát triển trình gỡ lỗi
- Hỗ trợ sẵn sàng để kiểm thử đơn vị
- Jinja2 templates
- RESTful request dispatch
- Hỗ trợ bảo mật cookie
- Full WSGI compliant
- Tài liệu mở rộng
- Dựa trên Unicode
- Khả năng tương thích công cụ dựa trên ứng dụng Google
- Nhiều tiện ích mở rộng cho các tính năng mong muốn
- Tính modular và thiết kế gọn nhẹ
- ORM-agnostic
- Độ linh hoạt cao
- Cung cấp xử lý HTTP request
- API có độc đáo và mạch lạc
- Dễ dàng triển khai

## Cài đặt và chạy thử chương trình với Framework Flask
 - Sử dụng command và chạy câu lệnh: pip install Flask
 - Chương trình Hello World!
 

        from flask import Flask
        app = Flask(__name__)
        
        @app.route('/')
        def hello_world():
            return 'Hello, World!'
        
        if __name__ == '__main__':
            app.run()   

    Sau khi chạy, console của bạn sẽ có 1 dòng log giống như thế này.

    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

    Bạn có thể copy và dán đường dẫn này lên trình duyệt để xem kết quả. Bạn sẽ thấy dòng chữ Hello, World! được in ra trên trình duyệt.