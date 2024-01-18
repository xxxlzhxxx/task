from flask import Flask

app = Flask(__name__)

# 导入 API 路由
from api.admin import *
from api.cart import *
from api.catalog import *
from api.checkout import *

if __name__ == '__main__':
    app.run(debug=True)
