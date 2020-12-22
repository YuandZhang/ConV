

 

 

 

 

 

 

 

实验过程

本实验数据来自腾讯新冠肺炎实时统计（https://news.qq.com/zt2020/page/feiyan），通过网络爬虫提取各省疫情数据，分别包括现存确诊、累计确诊数、疑似病例、死亡病例、治愈人数。并将这些数据，存储到mySql数据库中，然后通过Django框架读取数据库数据，进行动态页面展示。

![img](file:///C:/Users/YUMING~1/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png)

实验环境

IDE：Pycharm Python 3.8

涉及到的库：Django、echarts 、BeautifulSoup、Pymysql

数据库：mysql 8.0

 

数据库内容展示

![img](file:///C:/Users/YUMING~1/AppData/Local/Temp/msohtmlclip1/01/clip_image004.png)

前端页面展示

使用方法，在命令行打开mysite所在的文件夹，运行python manage.py runserver

在浏览器进入http://127.0.0.1:8000/conv/selectsf/

![img](file:///C:/Users/YUMING~1/AppData/Local/Temp/msohtmlclip1/01/clip_image006.png)

可进行分省份查看疫情情况，和全国疫情整体数据

![img](file:///C:/Users/YUMING~1/AppData/Local/Temp/msohtmlclip1/01/clip_image008.png)

![img](file:///C:/Users/YUMING~1/AppData/Local/Temp/msohtmlclip1/01/clip_image010.png)

并对给类别数据进行了柱状图的可视化数据展示

![img](file:///C:/Users/YUMING~1/AppData/Local/Temp/msohtmlclip1/01/clip_image012.png)