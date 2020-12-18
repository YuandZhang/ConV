name=['辽宁']
nowconfirm=['90']

# from pyecharts import Bar
# from pyecharts import Geo
from pyecharts import Map
map = Map("给地区现存病例分布", "data from **", title_color="#404a59", title_pos="center")
map.add("", name, nowconfirm, maptype='china', is_visualmap=True, visual_text_color='#000', is_label_show=True)
map.render("中国疫情地图.html")