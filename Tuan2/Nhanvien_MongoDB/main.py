
from flask import Flask, render_template, request
from flask_mail import Mail, Message
import pymongo



app = Flask(__name__)

nosql_conn = pymongo.MongoClient('mongodb://127.0.0.1:27017/')  # 1. Kết nối DB
mydb = nosql_conn['Nhanvien']                                   # 2. Khởi tạo hoặc gọi một Database
mycol = mydb["nhanvien"]                                        # 3. Khởi tạo hoặc gọi một Collection


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'lehailam222@gmail.com'
app.config['MAIL_PASSWORD'] = '*******' 
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/show")
def show():
    users = []
    for x in mycol.find():
        users.append(x)

    return render_template("base.html", users = users)

@app.route("/insert",methods=['POST'])
def insert():
    id = request.form['id']
    name = request.form['name']
    cccd = request.form['cccd']
    email = request.form['email']
    phone = request.form['phone']
    mydict = { "id_nhanvien": id, "ten_nhanvien": name, "cccd": cccd, "email": email,"phone": phone }
    x = mycol.insert_one(mydict)

    # msg = Message("Thêm nhân viên", sender='lehailam222@g,ail.com', recipients=[email])
    # msg.body = "Gửi từ python (Lê Hải Đăng Lâm)"
    # mail.send(msg)

    return 'Đã thêm tài khoản và gửi email tới nhân viên'
@app.route("/update",methods=['POST'])
def update():
    id = request.form['id']
    name = request.form['name']
    cccd = request.form['cccd']
    email = request.form['email']
    phone = request.form['phone']

    if name != "":
        myquery = { "id_nhanvien": id }
        newvalues = { "$set": { "ten_nhanvien": name } }
        mycol.update_one(myquery, newvalues)  
    if cccd != "":
        myquery = { "id_nhanvien": id }
        newvalues = { "$set": { "cccd": cccd } }
        mycol.update_one(myquery, newvalues)  
    if email != "":
        myquery = { "id_nhanvien": id }
        newvalues = { "$set": { "email": email } }
        mycol.update_one(myquery, newvalues)  
    if phone != "":
        myquery = { "id_nhanvien": id }
        newvalues = { "$set": { "phone": phone } }
        mycol.update_one(myquery, newvalues)  

    return 'Đã cập nhật thông tin nhân viên'

@app.route("/find", methods=['GET'])
def find():

    id = request.args.get('id')
    if id:
        kq= []
        for x in mycol.find():
            if x['id_nhanvien'].find(id)>=0:
                kq.append(x)
        users = kq
    return render_template("thongtin.html", users = users)


@app.route("/delete", methods=['GET'])
def delete():
    id = request.args.get('id')    
    myquery = { "id_nhanvien": id }
    mycol.delete_one(myquery)

    return 'Đã xóa nhân viên'

if __name__ == "__main__":
    app.run(debug=True)
