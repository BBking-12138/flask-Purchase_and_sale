# -*- coding:utf-8 -*-
# author:Agam
# datetime:2018-11-05

import datetime
import random
import string
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Pie
from sqlalchemy import extract, func
from app.apps import db
# from app.models import Purchase, sales, warehouse, goods


# ... [验证码生成函数不变] ...
def rndColor():
    '''随机颜色'''
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def gene_text():
    '''生成4位验证码'''
    return ''.join(random.sample(string.ascii_letters+string.digits, 4))

def draw_lines(draw, num, width, height):
    '''划线'''
    for num in range(num):
        x1 = random.randint(0, width / 2)
        y1 = random.randint(0, height / 2)
        x2 = random.randint(0, width)
        y2 = random.randint(height / 2, height)
        draw.line(((x1, y1), (x2, y2)), fill='black', width=1)

def get_verify_code():
    '''生成验证码图形'''
    code = gene_text()
    # 图片大小120×50
    width, height = 120, 50
    # 新图片对象
    im = Image.new('RGB',(width, height),'white')
    # 字体
    font = ImageFont.truetype('app/static/arial.ttf', 40)
    # draw对象
    draw = ImageDraw.Draw(im)
    # 绘制字符串
    for item in range(4):
        draw.text((5+random.randint(-3,3)+23*item, 5+random.randint(-3,3)),
                  text=code[item], fill=rndColor(),font=font )
    # 划线
    draw_lines(draw, 2, width, height)
    # 高斯模糊
    im = im.filter(ImageFilter.GaussianBlur(radius=1.5))
    return im, code

# # 进货图表
# def bars():
#     bar = bar_chart()
#     return bar
#
#
# def bar_chart():
#     d = db.session.query(
#         func.count(extract('Day', Purchase.purchase_addtime)),
#         extract('Day', Purchase.purchase_addtime)
#     ).group_by(extract('Day', Purchase.purchase_addtime)).all()
#
#     attr = ["{}号".format(j) for _, j in d]
#     v1 = [i for i, _ in d]
#
#     bar = Bar()
#     bar.add_xaxis(attr)
#     bar.add_yaxis("采购量", v1)
#     bar.set_global_opts(
#         title_opts=opts.TitleOpts(title="日采购量"),
#         datazoom_opts=[
#             opts.DataZoomOpts(type_="slider", range_start=10, range_end=25),
#             opts.DataZoomOpts(type_="inside", range_start=10, range_end=25)
#         ]
#     )
#     return bar
#
#
# # 库存图表
# def pies():
#     d = db.session.query(
#         func.sum(warehouse.warehouse_goods_num).label('total'),
#         goods.goods_name
#     ).join(goods, warehouse.warehouse_goods_name == goods.goods_name)\
#     .group_by(goods.goods_name).all()
#
#     attr = [j for _, j in d]
#     v1 = [i for i, _ in d]
#
#     pie = Pie()
#     pie.add("", [list(z) for z in zip(attr, v1)])
#     pie.set_global_opts(
#         title_opts=opts.TitleOpts(title="库存统计"),
#         legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%")
#     )
#     pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#     return pie
#
# # 销售图表
# def lines():
#     sale = db.session.query(
#         func.count(extract('Day', sales.sales_addtime)).label('count'),
#         extract('Day', sales.sales_addtime).label('day')
#     ).group_by(extract('Day', sales.sales_addtime)).all()
#
#     attr = [i for _, i in sale]
#     v1 = [j for j, _ in sale]
#
#     line = Line()
#     line.add_xaxis(attr)
#     line.add_yaxis("销售量", v1)
#     line.set_global_opts(
#         title_opts=opts.TitleOpts(title="日销售量"),
#         datazoom_opts=[
#             opts.DataZoomOpts(type_="slider", range_start=10, range_end=25),
#             opts.DataZoomOpts(type_="inside", range_start=10, range_end=25)
#         ]
#     )
#     return line

def on_created():
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S");  # 生成当前时间
    randomNum = random.randint(0, 100);  # 生成的随机整数n，其中0<=n<=100
    if randomNum <= 10:
        randomNum = str(0) + str(randomNum);
    uniqueNum = str(nowTime) + str(randomNum);
    return uniqueNum