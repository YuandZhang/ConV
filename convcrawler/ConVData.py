###https://www.cnblogs.com/jlt965256450/p/12605486.html
import requests
from lxml import  etree
import pandas as pd
import json
import ConV_mysql as mysql

#
class nCoV_2019:
    def __init__(self):
        self.headers={ 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36 Edg/86.0.622.63'}
        self.url='https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'

    def parse_url(self):
        #get请求网页
        r=requests.get(url=self.url,headers=self.headers)
        #断言判断状态码是否为200 ， 如果不是则报错
        assert r.status_code==200
        r.encoding='utf-8'

        return r.text

    def getDataList(self):
        conn=mysql.getConnection()
        data=json.loads(self.parse_url())
        data=json.loads(data['data'])
        china=data['areaTree'][0]['children']
        chinaTotals = "确诊人数:" + str(data['chinaTotal']['confirm']) + \
                      "疑似人数:" + str(data['chinaTotal']['suspect']) + \
                      "死亡人数:" + str(data['chinaTotal']['dead']) + \
                      "治愈人数:" + str(data['chinaTotal']['heal']) + \
                      "更新日期:" + data['lastUpdateTime']

        Total=[]
        #'nowConfirm': 65, 'confirm': 1305, 'suspect': 0, 'dead': 7, 'deadRate': '0.54', 'showRate': False, 'heal': 1233, 'healRate': '94.48', 'showHeal': True
        for i in range(len(china)):

            name=china[i]['name']
            nowConfirm=int(china[i]['total']['nowConfirm'])
            confirm=int(china[i]['total']['confirm'])
            suspect=int(china[i]['total']['suspect'])
            dead=int(china[i]['total']['dead'])
            heal=int(china[i]['total']['heal'])


            # mysql.truncate_data(conn)
            # mysql.insert_data(conn,name,nowConfirm,confirm,suspect,dead,heal)
            mysql.update_data(conn,name,nowConfirm,confirm,suspect,dead,heal)
    def chinamapdraw(self):
        map=map_draw.map_draw()
        map.china_conv_map()
    def main(self):
        self.getDataList()

nCoV_2019=nCoV_2019()
nCoV_2019.main()


