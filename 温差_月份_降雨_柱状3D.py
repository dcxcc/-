from pyecharts.charts import Bar3D, Pie,Grid
from pyecharts import options as opts
import pandas  as pd
from pyecharts.globals import ThemeType

all_data = pd.read_csv("data/中国气候.csv")

df = all_data
df['平均降雨量'] = df['平均降雨量'].str.lower().str.extract(r'(\d+)mm').applymap(lambda x: x)
df['平均最高气温'] = df['平均最高气温'].str.lower().str.extract(r'(\d+)').applymap(lambda x: x)
df['平均最低气温'] = df['平均最低气温'].str.lower().str.extract(r'(\d+)').applymap(lambda x: x)
df['月份'] = df['月份'].str.lower().str.extract(r'(\d+)').applymap(lambda x: x)

mon_name=["一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","一二月"]
m_r=df["平均降雨量"].tolist()
# print(m_r)
m_r = list(map(int, m_r))
mon1_r=[]
mon2_r=[]
mon3_r=[]
mon4_r=[]
mon5_r=[]
mon6_r=[]
mon7_r=[]
mon8_r=[]
mon9_r=[]
mon10_r=[]
mon11_r=[]
mon12_r=[]
province_data = [
    [
        df['地区'][i],
        int(df["平均降雨量"][i]),
        int(df["月份"][i])
    ]
    for i in range(0,len(df))
]
# print(province_data)
for i in range(0,len(df)-1):
    if province_data[i][2]==1:
        mon1_r.append(province_data[i][1])
    elif province_data[i][2]==2:
        mon2_r.append(province_data[i][1])
    elif province_data[i][2]==3:
        mon3_r.append(province_data[i][1])
    elif province_data[i][2]==4:
        mon4_r.append(province_data[i][1])
    elif province_data[i][2]==5:
        mon5_r.append(province_data[i][1])
    elif province_data[i][2]==6:
        mon6_r.append(province_data[i][1])
    elif province_data[i][2]==7:
        mon7_r.append(province_data[i][1])
    elif province_data[i][2]==8:
        mon8_r.append(province_data[i][1])
    elif province_data[i][2]==9:
        mon9_r.append(province_data[i][1])
    elif province_data[i][2]==10:
        mon10_r.append(province_data[i][1])
    elif province_data[i][2]==11:
        mon11_r.append(province_data[i][1])
    elif province_data[i][2]==12:
        mon12_r.append(province_data[i][1])
mon_r_m_list=[]
mon_r_m_list.append(sum(mon1_r))
mon_r_m_list.append(sum(mon2_r))
mon_r_m_list.append(sum(mon3_r))
mon_r_m_list.append(sum(mon4_r))
mon_r_m_list.append(sum(mon5_r))
mon_r_m_list.append(sum(mon6_r))
mon_r_m_list.append(sum(mon7_r))
mon_r_m_list.append(sum(mon8_r))
mon_r_m_list.append(sum(mon9_r))
mon_r_m_list.append(sum(mon10_r))
mon_r_m_list.append(sum(mon11_r))
mon_r_m_list.append(sum(mon12_r))
mon_data = [
    [
        mon_name[i],
        mon_r_m_list[i]
    ]
    for i in range(0,len(mon_r_m_list))
]
province_data1 = [
    (
        int(df['温差'][i]),
        int(df['平均降雨量'][i]),
        int(df["月份"][i])
    )
    for i in range(0, len(df))
]

province_data1 = sorted(province_data1, key=lambda x: x[1], reverse=True)
data = province_data1



def wx_m_r_bar3d():



    bar3d = (

        Bar3D(init_opts=opts.InitOpts(width="300px", height="500px"))
        .add(
            "",
            [[d[0], d[2], d[1]] for d in data],
            xaxis3d_opts=opts.Axis3DOpts(name="温差"),
            yaxis3d_opts=opts.Axis3DOpts(name="月份"),
            zaxis3d_opts=opts.Axis3DOpts(name="平均降雨量"),
        )
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=90000),
            title_opts=opts.TitleOpts(title="温差_月份_降雨_柱状3D"),
        )
        .set_series_opts(
        )

    )
    pie = (
        Pie()
            .add("", mon_data,
                 radius=["10%", "20%"],
                 center=["88%", "65%"],
                 itemstyle_opts=opts.ItemStyleOpts(
                     border_width=1, border_color="rgba(0,0,0,0.3)"
                 ),
                 )
            .set_global_opts(title_opts=opts.TitleOpts(title=""),
                             visualmap_opts=opts.VisualMapOpts(max_=90000),)
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            # .render("pie_set_color.html")
    )
    grid_chart = (
        Grid(init_opts=opts.InitOpts(
            theme=ThemeType.WHITE, width='1200px', height='600px'))
            .add(
            bar3d,
            grid_opts=opts.GridOpts(),
        )
            .add(
            pie,
            grid_opts=opts.GridOpts(pos_left="45%", pos_top="60%"),
        )
            .render("templates/wx_m_r_bar3d.html")
    )