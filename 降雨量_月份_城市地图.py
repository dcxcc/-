from pandas import DataFrame
from pyecharts import options as opts
from pyecharts.charts import Map, Timeline,Pie
import pandas  as pd
def r_m_c():
    all_data=pd.read_csv("data/中国气候.csv")

    df=all_data
    df['平均降雨量'] = df['平均降雨量'].str.lower().str.extract(r'(\d+)mm').applymap(lambda x: x)
    df['平均最高气温'] = df['平均最高气温'].str.lower().str.extract(r'(^.*\d+)').applymap(lambda x: x)
    df['平均最低气温'] = df['平均最低气温'].str.lower().str.extract(r'(^.*\d+)').applymap(lambda x: x)
    df['月份'] = df['月份'].str.lower().str.extract(r'(\d+)').applymap(lambda x: x)
    # print(df['平均降雨量'])

    list=[]
    for i in range(0,len(df)):
        max_t=int(df['平均最高气温'][i])
        min_t=int(df['平均最低气温'][i])
        list.append(abs(max_t-min_t))


    province_data = [
        [
            df['地区'][i],
            int(df['平均降雨量'][i]),
            int(df["月份"][i])
        ]
        for i in range(0,len(df))
    ]
    mon1=[]
    mon2=[]
    mon3=[]
    mon4=[]
    mon5=[]
    mon6=[]
    mon7=[]
    mon8=[]
    mon9=[]
    mon10=[]
    mon11=[]
    mon12=[]
    province_data = sorted(province_data, key=lambda x: x[1], reverse=True)
    for i in range(0,len(df)-1):
        if province_data[i][2]==1:
            traindata=[province_data[i][0],province_data[i][1]]
            mon1.append(traindata)
        elif province_data[i][2]==2:
            traindata = [province_data[i][0],province_data[i][1]]
            mon2.append(traindata)
        elif province_data[i][2]==3:
            traindata = [province_data[i][0],province_data[i][1]]
            mon3.append(traindata)
        elif province_data[i][2]==4:
            traindata = [province_data[i][0],province_data[i][1]]
            mon4.append(traindata)
        elif province_data[i][2]==5:
            traindata = [province_data[i][0],province_data[i][1]]
            mon5.append(traindata)
        elif province_data[i][2]==6:
            traindata = [province_data[i][0],province_data[i][1]]
            mon6.append(traindata)
        elif province_data[i][2]==7:
            traindata = [province_data[i][0],province_data[i][1]]
            mon7.append(traindata)
        elif province_data[i][2]==8:
            traindata = [province_data[i][0],province_data[i][1]]
            mon8.append(traindata)
        elif province_data[i][2]==9:
            traindata = [province_data[i][0],province_data[i][1]]
            mon9.append(traindata)
        elif province_data[i][2]==10:
            traindata = [province_data[i][0],province_data[i][1]]
            mon10.append(traindata)
        elif province_data[i][2]==11:
            traindata = [province_data[i][0],province_data[i][1]]
            mon11.append(traindata)
        elif province_data[i][2]==12:
            traindata = [province_data[i][0],province_data[i][1]]
            mon12.append(traindata)

    mon=[mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12]
    i=0
    tl=Timeline()
    for m in mon:
        i+=1
        c = (
            Map()
            .add(
                "全国主要城市{}月平均降雨量".format(i),
                m,
                "china-cities",
                label_opts=opts.LabelOpts(is_show=False),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="降雨量_月份_城市地图"),
                visualmap_opts=opts.VisualMapOpts(
                max_=500,min_=0
                )
            )
            .set_series_opts(
                label_opts=opts.LabelOpts(is_show=False)
            )

        )
        tl.add(c, "{}月".format(i))
    tl.render("templates/r_m_c.html")
