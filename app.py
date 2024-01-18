from flask import Flask, session
from api import app as api_app
from flask import Flask, render_template
import sqlite3
import os



template_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template/')
app = Flask(__name__, template_folder=template_folder_path)

app.secret_key = 'qwer'
# if 'cart' not in session:
#     session['cart'] = []


# if 'cart' not in session or not session['cart']:
#     print('initialize session')
#     session['cart'] = []

if __name__ == '__main__':
    
    api_app.run(port=5001)  # 启动 API 服务
   # app.run(port=5000)  # 启动主应用
