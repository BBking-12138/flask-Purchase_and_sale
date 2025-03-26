#-*- coding:utf-8 -*-
# author:Agam
# datetime:2018-11-05

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
import os

app = Flask(__name__)

# 数据库配置
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/bishe?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # 关闭SQLAlchemy的修改追踪,提高性能
app.config["SQLALCHEMY_ECHO"] = False  # 关闭SQL语句打印

# 密钥配置
app.config['SECRET_KEY'] = os.urandom(24)  # 使用系统生成的随机密钥

# 调试开关
app.debug = True

# 注册数据模型
db = SQLAlchemy(app)

# 邮件配置
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', '')  # 从环境变量获取
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', '')  # 从环境变量获取
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', '')  # 从环境变量获取

mail = Mail(app)

# 注册蓝图
from app.admin import admin as admin_blueprint
from app.home import home as home_blueprint
app.register_blueprint(admin_blueprint, url_prefix='/admin/')
app.register_blueprint(home_blueprint, url_prefix='/')

@app.errorhandler(404)
def page_not_found(error):
    return render_template("admin/404.html"), 404






