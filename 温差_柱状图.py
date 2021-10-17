
from pandas import DataFrame
from pyecharts import options as opts
from pyecharts.charts import Map, Timeline,Bar
import pandas  as pd
from pyecharts.globals import ThemeType
def wx_bar():
    all_data=pd.read_csv("data/中国气候.csv")

    df=all_data

    df['月份'] = df['月份'].str.lower().str.extract(r'(\d+)').applymap(lambda x: x)

    province_data = [
        [
            df['地区'][i],
            int(df["温差"][i]),
            int(df["月份"][i])
        ]
        for i in range(0,len(df))
    ]
    province_data = sorted(province_data, key=lambda x: x[1],reverse=True)

    mon1_x_data=[]
    mon1_y_data=[]
    mon2_x_data=[]
    mon2_y_data=[]
    mon3_x_data=[]
    mon3_y_data=[]
    mon4_x_data=[]
    mon4_y_data=[]
    mon5_x_data=[]
    mon5_y_data=[]
    mon6_x_data=[]
    mon6_y_data=[]
    mon7_x_data=[]
    mon7_y_data=[]
    mon8_x_data=[]
    mon8_y_data=[]
    mon9_x_data=[]
    mon9_y_data=[]
    mon10_x_data=[]
    mon10_y_data=[]
    mon11_x_data=[]
    mon11_y_data=[]
    mon12_x_data=[]
    mon12_y_data=[]
    # province_data = sorted(province_data, key=lambda x: x[1], reverse=True)
    for i in range(0,len(df)-1):
        if province_data[i][2]==1:
            mon1_x_data.append(province_data[i][0])
            mon1_y_data.append(province_data[i][1])
        elif province_data[i][2]==2:
            mon2_x_data.append(province_data[i][0])
            mon2_y_data.append(province_data[i][1])
        elif province_data[i][2]==3:
            mon3_x_data.append(province_data[i][0])
            mon3_y_data.append(province_data[i][1])
        elif province_data[i][2]==4:
            mon4_x_data.append(province_data[i][0])
            mon4_y_data.append(province_data[i][1])
        elif province_data[i][2]==5:
            mon5_x_data.append(province_data[i][0])
            mon5_y_data.append(province_data[i][1])
        elif province_data[i][2]==6:
            mon6_x_data.append(province_data[i][0])
            mon6_y_data.append(province_data[i][1])
        elif province_data[i][2]==7:
            mon7_x_data.append(province_data[i][0])
            mon7_y_data.append(province_data[i][1])
        elif province_data[i][2]==8:
            mon8_x_data.append(province_data[i][0])
            mon8_y_data.append(province_data[i][1])
        elif province_data[i][2]==9:
            mon9_x_data.append(province_data[i][0])
            mon9_y_data.append(province_data[i][1])
        elif province_data[i][2]==10:
            mon10_x_data.append(province_data[i][0])
            mon10_y_data.append(province_data[i][1])
        elif province_data[i][2]==11:
            mon11_x_data.append(province_data[i][0])
            mon11_y_data.append(province_data[i][1])
        elif province_data[i][2]==12:
            mon12_x_data.append(province_data[i][0])
            mon12_y_data.append(province_data[i][1])


    mon_x_data=[mon1_x_data,mon2_x_data,mon3_x_data,mon4_x_data,mon5_x_data,mon6_x_data,mon7_x_data,mon8_x_data,mon9_x_data,mon10_x_data,mon11_x_data,mon12_x_data]

    mon_y_data=[mon1_y_data,mon2_y_data,mon3_y_data,mon4_y_data,mon5_y_data,mon6_y_data,mon7_y_data,mon8_y_data,mon9_y_data,mon10_y_data,mon11_y_data,mon12_y_data]

    i=0



    tl=Timeline(init_opts=opts.InitOpts(width="900px", height="600px", theme=ThemeType.DARK))
    for i in range(0,12):
        c = (
            Bar()
            .add_xaxis(mon_x_data[i])
            .add_yaxis("温差",mon_y_data[i])
            .set_global_opts(
                title_opts=opts.TitleOpts(title="温差_柱状图"),
                visualmap_opts=opts.VisualMapOpts(
                max_=30,min_=0,

                ),datazoom_opts=opts.DataZoomOpts(
                    range_start=0,
                    range_end=10
                ),
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        tl.add(c, "{}月".format(i+1))
        tl.add_schema(
            orient="vertical",
            is_auto_play=True,
            is_inverse=True,
            play_interval=5000,
            pos_left="null",
            pos_right="5",
            pos_top="20",
            pos_bottom="20",
            width="60",
            label_opts=opts.LabelOpts(is_show=True, color="#fff"),
        )

    tl.render("templates/wx_bar.html")

