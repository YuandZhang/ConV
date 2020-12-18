import requests
res = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
res.encoding = 'utf-8'
print(res.text)