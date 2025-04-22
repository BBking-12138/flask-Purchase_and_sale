# -*- coding:utf-8 -*-
# author:Agam
# datetime:2018-11-05

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, FloatField, IntegerField
from wtforms.validators import DataRequired

from app.apps import app
# from app.models import goods, supplier, User, power, client, duty, section, warehouse
from app.models import User, Project


# 登陆表单
class LoginForm(FlaskForm):
    count = StringField(
        label="登陆账号",
        validators=[
            DataRequired()
        ],
        description="登陆账号",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入登陆账号！",
        }

    )
    password = PasswordField(
        label="密码",
        validators=[
            DataRequired()
        ],
        description="密码",
        render_kw={
            "type": "password",
            "class": "layui-input",
            "placeholder": "请输入密码！",
            "lay-verify": "required",
        }
    )
    verify_code = StringField(
        label='验证码',
        validators=[
            DataRequired()
        ],
        description="验证码",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input-inline",
            "placeholder": "请输入验证码！",
        }
    )
    submit = SubmitField(
        "登陆",
        render_kw={
            "type": "submit",
            "lay-filter": "login",
            "style": "width:100%;",
            "onclick": "mesg()"
        }
    )


# 注册表单
class RegisterForm(FlaskForm):
    count = StringField(
        label='请输入登陆账号',
        validators=[
            DataRequired()
        ],
        description="输入登陆账号的输入框",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入登陆账号！",
        }
    )
    password = PasswordField(
        label='请输入密码',
        validators=[
            DataRequired()
        ],
        description="输入密码的输入框",
        render_kw={
            "type": "password",
            "class": "layui-input",
            "placeholder": "请输入密码！",
            "lay-verify": "required",
        }
    )
    re_password = PasswordField(
        label='请确认密码',
        validators=[
            DataRequired()
        ],
        description="确认密码的输入框",
        render_kw={
            "type": "password",
            "class": "layui-input",
            "placeholder": "请确认密码！",
            "lay-verify": "required",
        }
    )
    username = StringField(
        label='请输入真实姓名或单位名',
        validators=[
            DataRequired()
        ],
        description="请输入真实姓名或单位名输入框",
        render_kw={
            "type": "text",
            "class": "layui-input",
            "placeholder": "请输入真实姓名或单位名！",
            "lay-verify": "required",
        }
    )
    # sex = SelectField(
    #     label="请选择性别",
    #     validators=[
    #         DataRequired()
    #     ],
    #     coerce=int,
    #     choices=[(0, "性别"), (1, "男"), (2, "女")],
    #     description="请选择性别",
    #
    #     render_kw={
    #         "class": "contrller",
    #     }
    # )
    identity = SelectField(
        label="请选择用户身份",
        validators=[
            DataRequired()
        ],
        coerce=int,
        choices=[(0, "用户身份"), (1, "招标单位"), (2, "投标单位"), (3, "评标员")],
        description="请选择用户身份",

        render_kw={
            "class": "contrller",
        }
    )
    mobile = StringField(
        label='请输入电话号码',
        validators=[
            DataRequired()
        ],
        description="请输入电话号码",
        render_kw={
            "type": "text",
            "class": "layui-input",
            "placeholder": "请输入电话号码！",
            "lay-verify": "required",
        }
    )
    email = StringField(
        label='请输入邮箱',
        validators=[
            DataRequired()
        ],
        description="请输入邮箱",
        render_kw={
            "type": "text",
            "class": "layui-input",
            "placeholder": "请输入邮箱！",
            "lay-verify": "required",
        }
    )
    submit = SubmitField(
        "注册",
        render_kw={
            "class": "layui-btn",
            "lay-filter": "subm",
            "onclick": "mesg()"
        }
    )

# 招标单位搜索
class TenderList(FlaskForm):
    username = StringField(
        description="请输入招标名称",
        render_kw={
            "type": "text",
            "class": "layui-input",
            "placeholder": "请输入招标名称！",
            "lay-verify": "required",
        }
    )
    submit = SubmitField(
        "搜索",
        render_kw={
            "class": "layui-btn",
            "lay-filter": "subm",
            "onclick": "mesg()"
        }
    )


# 招标成功单搜索
class BidSuccessfulSearch(FlaskForm):
    tender_unit = StringField(
        description="请输入招标单位名称",
        render_kw={
            "type": "text",
            "class": "layui-input",
            "placeholder": "请输入招标单位名称！",
            "lay-verify": "required",
        }
    )
    # person_name = StringField(
    #     description="评标员名称查询",
    #     render_kw={
    #         "type": "text",
    #         "placeholder": "评标员名称查询",
    #         "autocomplete": "off",
    #         "class": "layui-input"
    #     }
    # )
    submit = SubmitField(
        "搜索",
        render_kw={
            "class": "layui-btn",
            "lay-filter": "subm",
            "onclick": "mesg()"
        }
    )

# 招投标项目公告搜索
class NoticeList(FlaskForm):
    notice_title = StringField(
        description="请输入公告标题",
        render_kw={
            "type": "text",
            "class": "layui-input",
            "placeholder": "请输入公告标题！",
            "lay-verify": "required",
        }
    )
    # person_name = StringField(
    #     description="评标员名称查询",
    #     render_kw={
    #         "type": "text",
    #         "placeholder": "评标员名称查询",
    #         "autocomplete": "off",
    #         "class": "layui-input"
    #     }
    # )
    submit = SubmitField(
        "搜索",
        render_kw={
            "class": "layui-btn",
            "lay-filter": "subm",
            "onclick": "mesg()"
        }
    )

# 添加招标信息
# with app.app_context():
    # goodsall = Project.query.all()

class IncreaseBidSuccessfulOrder(FlaskForm):
    project_number = StringField(
        label="项目编号",
        validators=[
            DataRequired("请输入项目编号！")
        ],
        description="项目编号",
        render_kw={
            "type": "text",
            "placeholder": "项目编号",
            "autocomplete": "off",
            "lay-verify": "required",
            "class": "layui-input"
        }
    )
    project_name = StringField(
        label='招标名称',
        validators=[
            DataRequired("请输入招标名称！")
        ],
        description="招标名称",
        render_kw={
            "type": "text",
            "placeholder": "招标名称",
            "autocomplete": "off",
            "lay-verify": "required",
            "class": "layui-input"
        }
    )
    project_introduction = StringField(
        label="项目简介",
        validators=[
            DataRequired("请输入项目简介！")
        ],
        description="项目简介",
        render_kw={
            "type": "text",
            "placeholder": "项目简介",
            "autocomplete": "off",
            "lay-verify": "required",
            "class": "layui-input"
        }
    )
    notes = StringField(
        label="备注",
        validators=[
            DataRequired("请输入备注！")
        ],
        description="备注",
        render_kw={
            "type": "text",
            "placeholder": "备注",
            "autocomplete": "off",
            "lay-verify": "required",
            "class": "layui-input"
        }
    )
    tender_unit = StringField(
        label='招标单位',
        validators=[
            DataRequired("请输入招标单位！")
        ],
        description="招标单位",
        render_kw={
            "type": "text",
            "placeholder": "招标单位",
            "autocomplete": "off",
            "lay-verify": "required",
            "class": "layui-input"
        }
    )
    submit = SubmitField(
        "添加",
        render_kw={
            "class": "layui-btn",
            "lay-filter": "subm",
            "onclick": "mesg()"
        }
    )

class TenderRevise(FlaskForm):
    id = StringField(
        label="项目id",
        validators=[
            DataRequired("请输入项目id！")
        ],
        description="项目id",
        render_kw={
            "type": "text",
            "placeholder": "项目id",
            "autocomplete": "off",
            "lay-verify": "required",
            "class": "layui-input"
        }
    )
    project_introduction = StringField(
        label="项目简介",
        validators=[
            DataRequired("请修改项目简介！")
        ],
        description="项目简介",
        render_kw={
            "type": "text",
            "placeholder": "项目简介",
            "autocomplete": "off",
            "lay-verify": "required",
            "class": "layui-input"
        }
    )
    notes = StringField(
        label="备注",
        validators=[
            DataRequired("请修改备注！")
        ],
        description="备注",
        render_kw={
            "type": "text",
            "placeholder": "备注",
            "autocomplete": "off",
            "lay-verify": "required",
            "class": "layui-input"
        }
    )
    tender_unit = StringField(
        label='招标单位',
        validators=[
            DataRequired("请修改招标单位！")
        ],
        description="招标单位",
        render_kw={
            "type": "text",
            "placeholder": "招标单位",
            "autocomplete": "off",
            "lay-verify": "required",
            "class": "layui-input"
        }
    )
    bid_unit = StringField(
        label='投标单位',
        validators=[
            DataRequired("请修改投标单位！")
        ],
        description="投标单位",
        render_kw={
            "type": "text",
            "placeholder": "投标单位",
            "autocomplete": "off",
            "lay-verify": "required",
            "class": "layui-input"
        }
    )
    status_id = StringField(
        label='招标状态',
        validators=[
            DataRequired("请修改招标状态！")
        ],
        description="招标状态",
        render_kw={
            "type": "text",
            "placeholder": "招标状态",
            "autocomplete": "off",
            "lay-verify": "required",
            "class": "layui-input"
        }
    )
    submit = SubmitField(
        "修改",
        render_kw={
            "class": "layui-btn",
            "lay-filter": "subm",
            "onclick": "mesg()"
        }
    )
# # 招标成功单搜索
# class purchsearch(FlaskForm):
#     goods_name = StringField(
#         description="请输入招标名称",
#         render_kw={
#             "type": "text",
#             "class": "layui-input",
#             "placeholder": "请输入招标名称！",
#             "lay-verify": "required",
#         }
#     )
#     person_name = StringField(
#         description="评标员名称查询",
#         render_kw={
#             "type": "text",
#             "placeholder": "评标员名称查询",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#     submit = SubmitField(
#         "搜索",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
#
# # 退标单搜索
# class returnordersearch(FlaskForm):
#     goods_name = StringField(
#         description="请输入招标名称！",
#         render_kw={
#             "type": "text",
#             "placeholder": "请输入招标名称！",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#     person_name = StringField(
#         description="评标员名称查询",
#         render_kw={
#             "type": "text",
#             "placeholder": "评标员名称查询",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#     submit = SubmitField(
#         "搜索",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
# # 招标信息查询搜索
# class goodssearch(FlaskForm):
#     goods_name = StringField(
#         description="招标信息查询",
#         render_kw={
#             "type": "text",
#             "placeholder": "招标信息查询",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#     submit = SubmitField(
#         "搜索",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
# # 添加商品名
# class addgoodsname(FlaskForm):
#     name = StringField(
#         label='招标名称',
#         validators=[
#             DataRequired()
#         ],
#         description="招标名称",
#         render_kw={
#             "type": "text",
#             "placeholder": "招标名称",
#             "autocomplete": "off",
#             "lay-verify": "required",
#             "class": "layui-input"
#         }
#     )
#     price = FloatField(
#         label='商品单价',
#         validators=[
#             DataRequired()
#         ],
#         description="商品单价",
#         render_kw={
#             "type": "text",
#             "placeholder": "商品单价",
#             "autocomplete": "off",
#             "lay-verify": "required",
#             "class": "layui-input"
#         }
#     )
#     info = TextAreaField(
#         label='商品简介',
#         description="商品简介",
#         render_kw={
#             "type": "text",
#             "placeholder": "商品简介",
#             "autocomplete": "off",
#             "lay-verify": "required",
#             "class": "layui-input"
#         }
#     )
#     submit = SubmitField(
#         "添加",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
#
# # 添加订单
# with app.app_context():
#     goodsall = goods.query.all()
#
# class increasePurchaseOrders(FlaskForm):
#     goods_name = SelectField(
#         label="货物名称",
#         validators=[
#             DataRequired("请选择供应商级别！")
#         ],
#         coerce=int,
#         choices=[(i.goods_id, i.goods_name) for i in goodsall],
#         description="供应商级别",
#         render_kw={
#             "class": "contrller",
#             "type": "text",
#             "placeholder": "商品名称",
#             "autocomplete": "off",
#             "lay-verify": "required",
#         }
#     )
#     num = IntegerField(
#         label='进货数量',
#         validators=[
#             DataRequired("请输入进货数量！")
#         ],
#         description="进货数量",
#         render_kw={
#             "type": "text",
#             "placeholder": "进货数量",
#             "autocomplete": "off",
#             "lay-verify": "required",
#             "class": "layui-input"
#         }
#     )
#     suppliers = {1: "5"}
#     gys = SelectField(
#         label="供应商名称",
#         validators=[
#             DataRequired("请选择供应商名称！")
#         ],
#         coerce=int,
#         description="供应商名称",
#         render_kw={
#             "class": "form-control",
#         }
#     )
#     users = {1: "1"}
#     ywy = SelectField(
#         label="业务员名称",
#         validators=[
#             DataRequired("请选择供业务员名称！")
#         ],
#         coerce=int,
#         description="业务员名称",
#         render_kw={
#             "class": "form-control",
#         }
#     )
#     submit = SubmitField(
#         "添加",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
#
# # 销售订单搜索
# class salesorderssearch(FlaskForm):
#     goods_name = StringField(
#         description="招标名称查询",
#         render_kw={
#             "type": "text",
#             "placeholder": "招标名称查询",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#     person_name = StringField(
#         description="投标单位查询",
#         render_kw={
#             "type": "text",
#             "placeholder": "投标单位查询",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#
#     submit = SubmitField(
#         "搜索",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
#
# # 添加销售订单
#
# warehouses = {1: "1"}
# class addsaleorder(FlaskForm):
#     goods_name = SelectField(
#         label="货物名称",
#         validators=[
#             DataRequired("货物名称！")
#         ],
#         coerce=int,
#         description="供应商级别",
#         render_kw={
#             "class": "contrller",
#             "type": "text",
#             "placeholder": "商品名称",
#             "autocomplete": "off",
#             "lay-verify": "required",
#         }
#     )
#     num = IntegerField(
#         label='销售数量',
#         validators=[
#             DataRequired("请输入销售数量！")
#         ],
#         description="销售数量",
#         render_kw={
#             "type": "text",
#             "placeholder": "销售数量",
#             "autocomplete": "off",
#             "lay-verify": "required",
#             "class": "layui-input"
#         }
#     )
#     clients = {1: "k"}
#     gk = SelectField(
#         label="顾客名称",
#         validators=[
#             DataRequired("请选择顾客名称！")
#         ],
#         coerce=int,
#         description="顾客名称",
#         render_kw={
#             "class": "form-control",
#         }
#     )
#     # users = User.query.all()
#     users = {"1": 5}
#     ywy = SelectField(
#         label="业务员名称",
#         validators=[
#             DataRequired("请选择供业务员名称！")
#         ],
#         coerce=int,
#         # choices=[(i.user_id, i.user_name) for i in users],
#         description="业务员名称",
#         render_kw={
#             "class": "form-control",
#         }
#     )
#
#     submit = SubmitField(
#         "添加",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
#
# # 退货订单搜索
# class returnsalessearch(FlaskForm):
#     goods_name = StringField(
#         description="招标名称查询",
#         render_kw={
#             "type": "text",
#             "placeholder": "招标名称查询",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#     person_name = StringField(
#         description="投标单位查询",
#         render_kw={
#             "type": "text",
#             "placeholder": "投标单位查询",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#
#     submit = SubmitField(
#         "搜索",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
#
# # 添加退货单
# class addreturnorder(FlaskForm):
#     goods_name = SelectField(
#         label="货物名称",
#         validators=[
#             DataRequired("请选择供应商级别！")
#         ],
#         coerce=int,
#         # choices=[(i.goods_id, i.goods_name) for i in goodsall],
#         description="供应商级别",
#         render_kw={
#             "class": "contrller",
#             "type": "text",
#             "placeholder": "商品名称",
#             "autocomplete": "off",
#             "lay-verify": "required",
#         }
#     )
#     num = IntegerField(
#         label='进货数量',
#         validators=[
#             DataRequired("请输入进货数量！")
#         ],
#         description="进货数量",
#         render_kw={
#             "type": "text",
#             "placeholder": "进货数量",
#             "autocomplete": "off",
#             "lay-verify": "required",
#             "class": "layui-input"
#         }
#     )
#     # suppliers = supplier.query.all()
#     suppliers = {1: "l"}
#     gys = SelectField(
#         label="供应商名称",
#         validators=[
#             DataRequired("请选择供应商名称！")
#         ],
#         coerce=int,
#         # choices=[(i.supplier_id, i.supplier_name) for i in suppliers],
#         description="供应商名称",
#         render_kw={
#             "class": "form-control",
#         }
#     )
#     # users = User.query.all()
#     users = {"1": 5}
#     ywy = SelectField(
#         label="业务员名称",
#         validators=[
#             DataRequired("请选择供业务员名称！")
#         ],
#         coerce=int,
#         # choices=[(i.user_id, i.user_name) for i in users],
#         description="业务员名称",
#         render_kw={
#             "class": "form-control",
#         }
#     )
#     submit = SubmitField(
#         "添加",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
#
# # 客户管理查询
# class customesserch(FlaskForm):
#     name = StringField(
#         description="投标商姓名查询",
#         render_kw={
#             "type": "text",
#             "placeholder": "投标商姓名查询",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#     phone = StringField(
#         description="手机号查询",
#         render_kw={
#             "type": "text",
#             "placeholder": "手机号查询",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#     submit = SubmitField(
#         "搜索",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
#
# # 添加客户
# class addcustomes(FlaskForm):
#     name = StringField(
#         label='客户名',
#         validators=[
#             DataRequired()
#         ],
#         description="客户名",
#         render_kw={
#             "type": "text",
#             "placeholder": "客户名",
#             "autocomplete": "off",
#             "lay-verify": "required",
#             "class": "layui-input"
#         }
#     )
#     addr = StringField(
#         label='客户地址',
#         validators=[
#             DataRequired()
#         ],
#         description="客户地址",
#         render_kw={
#             "type": "text",
#             "placeholder": "客户地址",
#             "autocomplete": "off",
#             "lay-verify": "required",
#             "class": "layui-input"
#         }
#     )
#     phone = StringField(
#         label='客户手机',
#         description="客户手机",
#         render_kw={
#             "type": "text",
#             "placeholder": "客户手机",
#             "autocomplete": "off",
#             "lay-verify": "required",
#             "class": "layui-input"
#         }
#     )
#     credit = SelectField(
#         label="客户级别",
#         coerce=int,
#         # choices=[(0, "客户级别"), (1, "一星"), (2, "二星"), (3, "三星"), (4, "四星"), (5, "五星")],
#         description="客户级别",
#         render_kw={
#             "class": "contrller",
#         }
#     )
#     submit = SubmitField(
#         "添加",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
#
# # 库存查询
# class warehouseserch(FlaskForm):
#     name = StringField(
#         description="招标名称查询",
#         render_kw={
#             "type": "text",
#             "placeholder": "招标名称查询",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#     gys = StringField(
#         description="评标员查询",
#         render_kw={
#             "type": "text",
#             "placeholder": "评标员查询",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#     submit = SubmitField(
#         "搜索",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
#
# # 入库搜索
# class enteringwarehouseserach(FlaskForm):
#     name = StringField(
#         description="招标名称查询",
#         render_kw={
#             "type": "text",
#             "placeholder": "招标名称查询",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#     ywy = StringField(
#         description="评标员查询",
#         render_kw={
#             "type": "text",
#             "placeholder": "评标员查询",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#     submit = SubmitField(
#         "搜索",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
#
# # 出库搜索
# class outWarehousingsearch(FlaskForm):
#     name = StringField(
#         description="招标名称查询",
#         render_kw={
#             "type": "text",
#             "placeholder": "招标名称查询",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#     ywy = StringField(
#         description="评标员查询",
#         render_kw={
#             "type": "text",
#             "placeholder": "评标员查询",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#     submit = SubmitField(
#         "搜索",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
# # 添加部门
# class addsection(FlaskForm):
#     name = StringField(
#         label='部门名',
#         validators=[
#             DataRequired()
#         ],
#         description="部门名",
#         render_kw={
#             "type": "text",
#             "placeholder": "部门名",
#             "autocomplete": "off",
#             "lay-verify": "required",
#             "class": "layui-input"
#         }
#     )
#     submit = SubmitField(
#         "添加",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
# # 添加职务
# class adddutys(FlaskForm):
#     name = StringField(
#         label='职务名',
#         validators=[
#             DataRequired()
#         ],
#         description="职务名",
#         render_kw={
#             "type": "text",
#             "placeholder": "职务名",
#             "autocomplete": "off",
#             "class": "layui-input"
#         }
#     )
#     submit = SubmitField(
#         "添加",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
# # 修改权限
# powers = {"1": 6}
# users = {"5": 6}
#
#
# class powerss(FlaskForm):
#     account = SelectField(
#         label="请选择用户名",
#         validators=[
#             DataRequired()
#         ],
#         coerce=int,
#         # choices=[(i.user_id, i.user_name) for i in users],
#         description="请选择权限",
#         render_kw={
#             "class": "contrller",
#         }
#     )
#
#     powerss = SelectField(
#         label="请选择权限",
#         validators=[
#             DataRequired()
#         ],
#         coerce=int,
#         # choices=[(i.power_id, i.power_name) for i in powers],
#         description="请选择权限",
#         render_kw={
#             "class": "contrller",
#         }
#     )
#
#     submit = SubmitField(
#         "修改",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
#
# # 修改部门和职务
#
# dutys = {1: 5}
# sections = {"p": 5}
#
# class bumens(FlaskForm):
#     account = SelectField(
#         label="请选择用户名",
#         validators=[
#             DataRequired()
#         ],
#         coerce=int,
#         # choices=[(i.user_id, i.user_name) for i in users],
#         description="用户名",
#         render_kw={
#             "class": "contrller",
#         }
#     )
#
#     dutyser = SelectField(
#         label="请选择职务",
#         validators=[
#             DataRequired()
#         ],
#         coerce=int,
#         # choices=[(i.duty_id, i.duty_name) for i in dutys],
#         description="请选择职务",
#         render_kw={
#             "class": "contrller",
#         }
#     )
#     sectionsr = SelectField(
#         label="请选择部门",
#         validators=[
#             DataRequired()
#         ],
#         coerce=int,
#         # choices=[(i.section_id, i.section_name) for i in sections],
#         description="请选择部门",
#         render_kw={
#             "class": "contrller",
#         }
#     )
#     submit = SubmitField(
#         "修改",
#         render_kw={
#             "class": "layui-btn",
#             "lay-filter": "subm",
#             "onclick": "mesg()"
#         }
#     )
#
# 修改密码
class alertpasswd(FlaskForm):
    account = StringField(
        label='请输入旧密码',
        validators=[
            DataRequired()
        ],
        description="请输入旧密码",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入旧密码！",
            'autocomplete': 'off'
        }
    )
    password = PasswordField(
        label='请输入新密码',
        validators=[
            DataRequired()
        ],
        description="输入密码的输入框",
        render_kw={
            "type": "password",
            "class": "layui-input",
            "placeholder": "请输入新密码！",
            "lay-verify": "required",
            'autocomplete': 'off'
        }
    )
    re_password = PasswordField(
        label='请确认密码',
        validators=[
            DataRequired()
        ],
        description="确认密码的输入框",
        render_kw={
            "type": "password",
            "class": "layui-input",
            "placeholder": "请确认密码！",
            "lay-verify": "required",
            'autocomplete': 'off'
        }
    )
    submit = SubmitField(
        "修改密码",
        render_kw={
            "class": "layui-btn",
            "lay-filter": "subm",
        }
    )


# 忘记密码
class wjpasswd(FlaskForm):
    count = StringField(
        label='请输入登陆账号',
        validators=[
            DataRequired()
        ],
        description="请输入登陆账号",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入登陆账号！",
            'autocomplete': 'off'
        }
    )
    email = StringField(
        label='请输入邮箱',
        validators=[
            DataRequired()
        ],
        description="请输入邮箱",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入邮箱！",
            'autocomplete': 'off'
        }
    )
    password = PasswordField(
        label='请输入新密码',
        validators=[
            DataRequired()
        ],
        description="输入密码的输入框",
        render_kw={
            "type": "password",
            "class": "layui-input",
            "placeholder": "请输入新密码！",
            "lay-verify": "required",
            'autocomplete': 'off'
        }
    )
    re_password = PasswordField(
        label='请确认密码',
        validators=[
            DataRequired()
        ],
        description="确认密码的输入框",
        render_kw={
            "type": "password",
            "class": "layui-input",
            "placeholder": "请确认密码！",
            "lay-verify": "required",
            'autocomplete': 'off'
        }
    )
    submit = SubmitField(
        "修改密码",
        render_kw={
            "class": "layui-btn",
            "lay-filter": "subm",
        }
    )

# 备份
class beifenser(FlaskForm):
    submit = SubmitField(
        "立即备份数据",
        render_kw={
            "class": "layui-btn",
            "lay-filter": "formDemo",
        }
    )

