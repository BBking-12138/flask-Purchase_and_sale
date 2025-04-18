#-*- coding:utf-8 -*-
# author:Agam
# datetime:2018-11-05
from datetime import datetime

from .apps import db

# class client(db.Model):
#     __tablename__ = 'client'
#
#     client_id = db.Column(db.Integer, primary_key=True)
#     client_name = db.Column(db.String(100))
#     client_addre = db.Column(db.String(100))
#     client_phone = db.Column(db.String(100))
#     client_credit = db.Column(db.Integer)
#
#
# class duty(db.Model):
#     __tablename__ = 'duty'
#
#     duty_id = db.Column(db.Integer, primary_key=True)
#     duty_name = db.Column(db.String(100), unique=True)
#     duty_addtime = db.Column(db.DateTime, index=True)
#     duty_is_true = db.Column(db.Integer)
#
#
# class goods(db.Model):
#     __tablename__ = 'goods'
#
#     goods_id = db.Column(db.Integer, primary_key=True)
#     goods_name = db.Column(db.String(100), unique=True)
#     goods_price = db.Column(db.String(100))
#     goods_intro = db.Column(db.String(255))
#
#
# class inwarehouse(db.Model):
#     __tablename__ = 'inwarehouse'
#
#     inwarehouse_id = db.Column(db.Integer, primary_key=True)
#     inwarehouse_count = db.Column(db.Integer)
#     inwarehouse_price = db.Column(db.String(100))
#     inwarehouse_addtime = db.Column(db.DateTime, index=True)
#     inwarehouse_goods = db.Column(db.String(100))
#     inwarehouse_supplier = db.Column(db.String(100))
#     inwarehouse_user_name = db.Column(db.String(100))
#     inwarehouse_num = db.Column(db.ForeignKey('purchase.purchase_num'), index=True)
#
#     purchase = db.relationship('Purchase', primaryjoin='inwarehouse.inwarehouse_num == Purchase.purchase_num', backref='inwarehouses')
#
#
# class power(db.Model):
#     __tablename__ = 'power'
#
#     power_id = db.Column(db.Integer, primary_key=True, index=True)
#     power_name = db.Column(db.String(100), unique=True)
#     power_addtime = db.Column(db.DateTime, index=True)
#
#
# class Purchase(db.Model):
#     __tablename__ = 'purchase'
#
#     purchase_id = db.Column(db.Integer, primary_key=True)
#     purchase_num = db.Column(db.String(100), unique=True)
#     purchase_count = db.Column(db.Integer)
#     purchase_price = db.Column(db.String(100))
#     purchase_addtime = db.Column(db.DateTime, index=True)
#     purchase_goods = db.Column(db.ForeignKey('goods.goods_name'), index=True)
#     purchase_supplier = db.Column(db.ForeignKey('supplier.supplier_name'), index=True)
#     purchase_user_name = db.Column(db.ForeignKey('user.user_name'), index=True)
#
#     good = db.relationship('goods', primaryjoin='Purchase.purchase_goods == goods.goods_name', backref='purchases')
#     supplier = db.relationship('supplier', primaryjoin='Purchase.purchase_supplier == supplier.supplier_name', backref='purchases')
#     user = db.relationship('User', primaryjoin='Purchase.purchase_user_name == User.user_name', backref='purchases')
#
#
#
#
# class returngoods(db.Model):
#     __tablename__ = 'returngoods'
#
#     returngoods_id = db.Column(db.Integer, primary_key=True)
#     returngoods_count = db.Column(db.Integer)
#     returngoods_price = db.Column(db.String(100))
#     returngoods_addtime = db.Column(db.DateTime, index=True)
#     returngoods_goods = db.Column(db.String(100))
#     returngoods_supplier = db.Column(db.String(100))
#     returngoods_user_name = db.Column(db.String(100))
#     returngoods_num = db.Column(db.ForeignKey('purchase.purchase_num'), index=True)
#
#     purchase = db.relationship('Purchase', primaryjoin='returngoods.returngoods_num == Purchase.purchase_num', backref='returngoods')
#
#
# class Salary(db.Model):
#     __tablename__ = 'salary'
#
#     salary_id = db.Column(db.Integer, primary_key=True)
#     salary_base = db.Column(db.Integer)
#     salary_grade = db.Column(db.Integer)
#     salary_subsidy = db.Column(db.Integer)
#     salary_other = db.Column(db.Integer)
#
#
# class sales(db.Model):
#     __tablename__ = 'sales'
#
#     sales_id = db.Column(db.Integer, primary_key=True)
#     sales_num = db.Column(db.String(100), unique=True)
#     sales_count = db.Column(db.Integer)
#     sales_price = db.Column(db.String(100))
#     sales_addtime = db.Column(db.DateTime, index=True)
#     sales_user_name = db.Column(db.ForeignKey('user.user_name'), index=True)
#     sales_client_id = db.Column(db.ForeignKey('client.client_id'), index=True)
#     sales_goods_name = db.Column(db.ForeignKey('goods.goods_name'), index=True)
#
#     sales_client = db.relationship('client', primaryjoin='sales.sales_client_id == client.client_id', backref='sales')
#     good = db.relationship('goods', primaryjoin='sales.sales_goods_name == goods.goods_name', backref='sales')
#     user = db.relationship('User', primaryjoin='sales.sales_user_name == User.user_name', backref='sales')
#
#
# class sealreturngoods(db.Model):
#     __tablename__ = 'sealreturngoods'
#
#     sealreturngoods_id = db.Column(db.Integer, primary_key=True)
#     sealreturngoods_count = db.Column(db.Integer)
#     sealreturngoods_price = db.Column(db.String(100))
#     sealreturngoods_addtime = db.Column(db.DateTime, index=True)
#     sealreturngoods_goods = db.Column(db.String(100))
#     sealreturngoods_supplier = db.Column(db.String(100))
#     sealreturngoods_user_name = db.Column(db.String(100))
#     sealreturngoods_num = db.Column(db.ForeignKey('sales.sales_num'), index=True)
#
#     sale = db.relationship('sales', primaryjoin='sealreturngoods.sealreturngoods_num == sales.sales_num', backref='sealreturngoods')
#
#
# class section(db.Model):
#     __tablename__ = 'section'
#
#     section_id = db.Column(db.Integer, primary_key=True)
#     section_name = db.Column(db.String(100), unique=True)
#     section_addtime = db.Column(db.DateTime, index=True)
#     section_is_true = db.Column(db.Integer)
#
#
# class stock(db.Model):
#     __tablename__ = 'stock'
#
#     stock_id = db.Column(db.Integer, primary_key=True)
#     stock_count = db.Column(db.Integer)
#     stock_price = db.Column(db.String(100))
#     stock_addtime = db.Column(db.DateTime, index=True)
#     stock_goods = db.Column(db.String(100))
#     stock_supplier = db.Column(db.String(100))
#     stock_user_name = db.Column(db.String(100))
#     stock_num = db.Column(db.ForeignKey('sales.sales_num'), index=True)
#
#     sale = db.relationship('sales', primaryjoin='stock.stock_num == sales.sales_num', backref='stocks')
#
#
# class supplier(db.Model):
#     __tablename__ = 'supplier'
#
#     supplier_id = db.Column(db.Integer, primary_key=True)
#     supplier_name = db.Column(db.String(100), unique=True)
#     supplier_addre = db.Column(db.String(100))
#     supplier_credit = db.Column(db.Integer)
#

# class User(db.Model):
#     __tablename__ = 'user'
#
#     user_id = db.Column(db.Integer, primary_key=True)
#     user_count = db.Column(db.String(100), unique=True)账号
#     user_name = db.Column(db.String(100), unique=True)用户名
#     user_sex = db.Column(db.String(100))
#     user_pwd = db.Column(db.String(100))
#     user_mail = db.Column(db.String(100))
#     user_phone = db.Column(db.String(100))
#     user_addtime = db.Column(db.DateTime, index=True)
#     user_photo = db.Column(db.String(100))
#     user_ispass = db.Column(db.Integer)
#     user_section = db.Column(db.ForeignKey('section.section_name'), index=True)
#     user_duty = db.Column(db.ForeignKey('duty.duty_name'), index=True)
#     user_power = db.Column(db.ForeignKey('power.power_name'), index=True)
#     user_salary = db.Column(db.ForeignKey('salary.salary_id'), index=True)
#
#     duty = db.relationship('duty', primaryjoin='User.user_duty == duty.duty_name', backref='users')
#     power = db.relationship('power', primaryjoin='User.user_power == power.power_name', backref='users')
#     salary = db.relationship('Salary', primaryjoin='User.user_salary == Salary.salary_id', backref='users')
#     section = db.relationship('section', primaryjoin='User.user_section == section.section_name', backref='users')
#
#     def check_pwd(self,pwd):
#         from werkzeug.security import check_password_hash
#         return check_password_hash(self.user_pwd,pwd)

class User(db.Model):
    __tablename__ = 'user'

    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="自增ID，主键")
    count = db.Column(db.String(255), nullable=False, comment="登陆账号")
    password = db.Column(db.String(512), nullable=False, comment="登录密码")
    username = db.Column(db.String(50), nullable=False, comment="用户名")
    sex = db.Column(db.Enum('男', '女', '其他'), nullable=False, comment="用户性别")
    mobile = db.Column(db.String(20), default=None, comment="电话号码")
    email = db.Column(db.String(100), default=None, comment="电子邮箱")
    # count = db.Column(db.String(255), nullable=False, comment="登陆账号")
    # password = db.Column(db.String(512), nullable=False, comment="登录密码")
    identity = db.Column(db.String(100), default=None, comment="用户身份：管理员 招标单位 投标单位 评标员")
    create_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    is_deleted = db.Column(db.Boolean, default=False, comment="是否删除")

    def check_pwd(self,pwd):
            from werkzeug.security import check_password_hash
            return check_password_hash(self.password,pwd)


class Status(db.Model):
    __tablename__ = 'status'

    id = db.Column(db.SmallInteger, primary_key=True, autoincrement=True, comment='状态ID')
    type = db.Column(db.String(30), nullable=False, comment='状态类型')
    code = db.Column(db.String(30), nullable=False, comment='状态代码')
    name = db.Column(db.String(50), nullable=False, comment='状态名称')

class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='主键ID')
    project_number = db.Column(db.SmallInteger, default=0, comment='项目编号')
    project_name = db.Column(db.Integer, default=0, comment='招标名称')  # 注意：实际应为字符串类型
    project_introduction = db.Column(db.Integer, default=0, comment='项目简介')  # 注意：实际应为文本类型
    notes = db.Column(db.SmallInteger, default=0, comment='备注')
    tender_unit = db.Column(db.String(100), comment='招标单位（创建人）')
    tender_status = db.Column(db.SmallInteger, default=0, comment='招标状态 0：招标中 1：已招标')
    bid_unit = db.Column(db.String(100), comment='投标单位')
    bid_status = db.Column(db.SmallInteger, default=0, comment='投标状态 0：投标中 1：已投标')
    status_id = db.Column(db.SmallInteger, db.ForeignKey('status.id'), nullable=False, comment='项目整体状态ID')
    is_deleted = db.Column(db.SmallInteger, default=0, comment='是否已删除,0:未删除;1:已删除')
    create_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    update_time = db.Column(db.DateTime, default=datetime.now, comment='更新时间')

    status = db.relationship('Status', backref='projects')

    def __init__(self, project_number, project_name, project_introduction, notes, tender_unit, status_id):
        self.project_number = project_number
        self.project_name = project_name
        self.project_introduction = project_introduction
        self.notes = notes
        self.tender_unit = tender_unit
        self.status_id = status_id


class ProjectEvaluator(db.Model):
    __tablename__ = 'project_evaluator'

    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), primary_key=True, comment='主键ID')
    evaluator_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, comment='评标员ID')
    evaluation_status = db.Column(db.SmallInteger, nullable=False, comment='评标状态ID')
    score = db.Column(db.Numeric(5, 2), comment='评分')
    evaluation_notes = db.Column(db.Text, comment='评标意见')
    evaluation_time = db.Column(db.DateTime, comment='评标时间')

# class warehouse(db.Model):
#     __tablename__ = 'warehouse'
#
#     warehouse_id = db.Column(db.Integer, primary_key=True)
#     warehouse_goods_num = db.Column(db.Integer)
#     warehouse_goods_name = db.Column(db.ForeignKey('goods.goods_name'), index=True)
#     warehouse_supplier_name = db.Column(db.ForeignKey('supplier.supplier_name'), index=True)
#
#     good = db.relationship('goods', primaryjoin='warehouse.warehouse_goods_name == goods.goods_name', backref='warehouses')
#     supplier = db.relationship('supplier', primaryjoin='warehouse.warehouse_supplier_name == supplier.supplier_name', backref='warehouses')
