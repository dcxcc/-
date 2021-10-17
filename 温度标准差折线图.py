import pyecharts.options as opts
from pyecharts.charts import Line
import pandas as pd
import numpy as np
def t_std_line():
    all_data=pd.read_csv("data/中国气候.csv")
    df=all_data
    df['平均降雨量'] = df['平均降雨量'].str.lower().str.extract(r'(\d+)mm').applymap(lambda x: x)
    df['平均最高气温'] = df['平均最高气温'].str.lower().str.extract(r'(\d+)').applymap(lambda x: x)
    df['平均最低气温'] = df['平均最低气温'].str.lower().str.extract(r'(\d+)').applymap(lambda x: x)
    df['月份'] = df['月份'].str.lower().str.extract(r'(\d+)').applymap(lambda x: x)
    std=[]

    wx_list=df["温差"].tolist()
    for i in range(0,len(wx_list),12):
        a=wx_list[i: i + 12]
        std.append(round(np.std(a),2))

    name=[]
    for i in range(0,len(df["地区"]),12):
        # print(i)
        name.append(df["地区"][i])

    week_name_list = name
    high_temperature = std


    (
        Line(init_opts=opts.InitOpts(width="900px", height="600px"))
        .add_xaxis(xaxis_data=week_name_list)
        .add_yaxis(
            series_name="温度标准差",
            y_axis=high_temperature,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                    opts.MarkPointItem(type_="average", name="平均值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="全国主要城市温度的稳定情况", subtitle="越小越稳定"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
            datazoom_opts=opts.DataZoomOpts(
                    range_start=0,
                    range_end=10
                ),
        )
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False)
        )
        .render("templates/t_std_line.html")
    )
