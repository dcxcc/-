from flask import Flask,render_template
from 最冷月_最热月_城市地图 import w_h_c
from 温差_月份_降雨_柱状3D import wx_m_r_bar3d
from 温差_柱状图 import wx_bar
from 温度标准差折线图 import t_std_line
from 降雨量_月份_城市地图 import r_m_c


#创建flask实例对象，并赋值给了app
app = Flask(__name__)


@app.route('/')#路由
def hello_world():#路由对应的视图函数
    return render_template('index.html')

#修改代码之后要重启服务器才能生效
@app.route("/index")
def index():
    return "首页"

#返回test.html页面
@app.route("/test")#浏览器输入的路径跟他一致
def test():
    # return 'test.html'#直接返回的就是字符串，而不是页面
    # render_template:渲染模板页面，默认查找的是templates文件夹中的页面
    return render_template("test.html")#不需要加templates

@app.route("/r_m_c")
def r_m_c_a():
    #先调用数据分析+可视化生成文件
    r_m_c()
    return render_template('r_m_c.html')

@app.route("/w_h_c")
def w_h_c_a():
    w_h_c()
    return render_template('w_h_c.html')

@app.route("/wx_bar")
def wx_bar_a():
    wx_bar()
    return render_template('wx_bar.html')

@app.route("/t_std_line")
def t_std_line_a():
    t_std_line()
    return render_template('t_std_line.html')

@app.route("/wx_m_r_bar3d")
def wx_m_r_bar3d_a():
    wx_m_r_bar3d()
    return render_template('wx_m_r_bar3d.html')

@app.route("/welcome")
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    #启动服务器(运行的是当前的flask项目)
    app.run()
