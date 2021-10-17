
from pandas import DataFrame
from pyecharts import options as opts
from pyecharts.charts import Map, Timeline,Bar
import pandas  as pd
from pyecharts.globals import ThemeType
def w_h_c():
    all_data=pd.read_csv("data/中国气候.csv")

    df=all_data
    df['平均最高气温'] = df['平均最高气温'].str.lower().str.extract(r'(^.*\d+)').applymap(lambda x: x)
    df['平均最低气温'] = df['平均最低气温'].str.lower().str.extract(r'(^.*\d+)').applymap(lambda x: x)
    df['月份'] = df['月份'].str.lower().str.extract(r'(\d+)').applymap(lambda x: x)

    province_data = [
        [
            df['地区'][i],
            int(df["平均最高气温"][i]),
            int(df["平均最低气温"][i]),
            int(df["月份"][i])
        ]
        for i in range(0,len(df))
    ]
    province_data = sorted(province_data, key=lambda x: x[1], reverse=True)
    mon2=[]
    mon8=[]
    # max_t=province_data[0][1]
    # min_t=province_data[0][2]
    # a=(max_t+min_t)/2

    for i in range(0,len(df)-1):
        if province_data[i][3]==2:
            max_t=province_data[i][1]
            min_t=province_data[i][2]
            mean_t=(max_t+min_t)/2
            traindata = [province_data[i][0],mean_t]

            mon2.append(traindata)
        elif province_data[i][3]==8:
            max_t=province_data[i][1]
            min_t=province_data[i][2]
            mean_t=(max_t+min_t)/2
            traindata = [province_data[i][0],mean_t]
            mon8.append(traindata)

    mon_mean=[mon2,mon8]
    mon_mean1=["二月","八月"]
    mon_type=["最冷月","最热月"]
    tl=Timeline()
    for i in range(2):
        c = (
            Map()
            .add(
                "全国主要城市{}平均温度".format(mon_type[i]),
                mon_mean[i],
                "china-cities",
                label_opts=opts.LabelOpts(is_show=False),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="最冷月_最热月_城市地图"),
                visualmap_opts=opts.VisualMapOpts(
                max_=40,min_=-30
                )
            )
            .set_series_opts(
                label_opts=opts.LabelOpts(is_show=False)
            )

        )
        tl.add(c, "{}".format(mon_mean1[i]))
    tl.render("templates/w_h_c.html")