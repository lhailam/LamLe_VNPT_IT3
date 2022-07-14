from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os
import re

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'lehailam222@gmail.com'
app.config['MAIL_PASSWORD'] = '********' 
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
#'vutruong5438@gmail.com', 'thopn95@gmail.com'
email_from = 'lehailam222@gmail.com'
email_to = 'thopn95@gmail.com' 

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
if(re.search(regex,email_to)):   
        print("Valid Email")
        @app.route('/home', methods= ['GET', 'POST'])
        @app.route('/', methods= ['GET', 'POST'])
        def home():
            if request.method == 'POST':
                msg = Message("Framework Flask: Sử dụng Method: POST, validate email để gửi email", sender=email_from, recipients=[email_to])
                msg.body = "Gửi từ python (Lê Hải Đăng Lâm)"
                mail.send(msg)
                return "Send email"
            return render_template('index.html')   
else:   
        print("Invalid Email")
        @app.route('/home', methods= ['GET', 'POST'])
        @app.route('/', methods= ['GET', 'POST'])
        def home():
            if request.method == 'POST':
                return "Invalid Email!!!"
            return render_template('index.html')
         


if __name__ == "__main__":
    app.run(debug=True)
