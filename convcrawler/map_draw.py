
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
class map_draw():
    def china_conv_map(self,name, nowconfirm):
        pieces=[

            {"max": 9999, "min": 500, 'label': 'str', 'color': '#660000'},
            {"max": 500, "min": 100, 'label': 'str', 'color': '#a61c00'},
            {"max": 100, "min": 50, 'label': 'str', 'color': '#ff0000'},
            {"max": 50, "min": 5, 'label': 'str', 'color': '#ff9900'},
            {"max": 5, "min": 1, 'label': 'str', 'color': '#fff2cc'},
            {"max": 00, "min": 00, 'label': 'str', 'color': '#ffffff'},

        ]

        c = (
            Map(init_opts=opts.InitOpts(width='1000px',height='800px'))#设置页面大小
                .add("现存确诊病例", [list(z) for z in zip(name, nowconfirm)], "china")
                .set_global_opts(
                title_opts=opts.TitleOpts(title="中国现存确诊病例"),
                visualmap_opts=opts.VisualMapOpts(max_=200,is_piecewise=True,pieces=pieces),
            )
            .render("中国疫情地图.html")
        )



map=map_draw()
map.china_conv_map()
