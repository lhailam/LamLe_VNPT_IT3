
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import json
import sqlite3

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'lehailam222@gmail.com'
app.config['MAIL_PASSWORD'] = '*******'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


def db_connection():
    conn = None
    conn = sqlite3.connect("db_nhanvien.sqlite")
    return conn
#hiển thị danh sách nhân viên
@app.route("/nhanvien", methods=["GET"])
def show():
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM nhanvien")
    nhanvien = [
                dict(id=row[0], name=row[1], cccd=row[2], email=row[3], phone = row[4])
                for row in cursor.fetchall()
                ]
    return jsonify(nhanvien)   
#thêm tài khoản nhân viên
@app.route("/nhanvien", methods=["POST"])
def insert():
    conn = db_connection()
    cursor = conn.cursor()
    id = request.form['id']
    name = request.form['name']
    cccd = request.form['cccd']
    email = request.form['email']
    phone = request.form['phone']
    sql = """INSERT INTO nhanvien (id_nhanvien, ten_nhanvien, cccd, email, phone)
                VALUES (?, ?, ?, ?, ?)"""
    cursor = cursor.execute(sql, (id, name, cccd, email, phone))
    conn.commit()

    msg = Message("Thêm nhân viên", sender='lehailam222@g,ail.com', recipients=[email])
    msg.body = "Gửi từ python (Lê Hải Đăng Lâm)"
    mail.send(msg)  

    return f"Đã thêm dữ liệu nhân viên và gửi email"


@app.route("/nhanvien/<id>", methods=["GET", "PUT", "DELETE"])
def def_nhanvien(id):
    conn = db_connection()
    cursor = conn.cursor()
    nhanvien = None

    #Cập nhật thông tin
    if request.method == "PUT":
        sql = """UPDATE nhanvien
                SET ten_nhanvien=?,
                    cccd=?,
                    email=?,
                    phone=?
                WHERE id_nhanvien=? """

        name = request.form['name']
        cccd = request.form['cccd']
        email = request.form['email']
        phone = request.form['phone']
        updated_nhanvien = {
            "id_nhanvien": id,
            "ten_nhanvien": name,
            "cccd": cccd,
            "email": email,
            "phone": phone
        }
        conn.execute(sql, (id, name, cccd, email, phone))
        conn.commit()
        return jsonify(updated_nhanvien)

    #hiển thị thông tin nhân viên theo ID
    if request.method == "GET":
        cursor.execute("SELECT * FROM nhanvien WHERE id_nhanvien=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            nhanvien = r
        return jsonify(nhanvien)

    #Xóa tài khoản 
    if request.method == "DELETE":
        sql = """ DELETE FROM nhanvien WHERE id_nhanvien=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "Đã xóa nhân viên có id: {} !!!".format(id)


if __name__ == "__main__":
    app.run(debug=True)