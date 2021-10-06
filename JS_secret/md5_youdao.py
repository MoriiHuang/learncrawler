import time
from hashlib import md5
str1="123456"
import random
import requests
# md=md5()
# md.update(str1.encode())
# res=md.hexdigest()
# print(res)
url='https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers={
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': "zh-CN,zh;q=0.9",
'Connection': 'keep-alive',
'Content-Length': '237',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'OUTFOX_SEARCH_USER_ID=1272382747@10.108.160.105; JSESSIONID=aaaAxXyYFg35j5TSmf4Hx; OUTFOX_SEARCH_USER_ID_NCOO=890743602.9092418; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcQPDESQ9IiH6RQ9UXIx; _ntes_nnid=5b8d33d5d50c6cd7bdb5f73284de9ce1,1617889582660; ___rl__test__cookies=1633489547089',
'Host': 'fanyi.youdao.com',
'Origin': 'https://fanyi.youdao.com',
'Referer': 'https://fanyi.youdao.com/',
# 'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
# 'sec-ch-ua-mobile': '?0',
# 'sec-ch-ua-platform':' "macOS"',
# 'Sec-Fetch-Dest': 'empty',
# 'Sec-Fetch-Mode': 'cors',
# 'Sec-Fetch-Site': 'same-origin',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest',
}
word=input('请输入想要翻译的单词：')
ts=str(int(time.time()*1000))
salt=ts+str(random.randint(0,10))
str_="fanyideskweb"+word+salt+"Y2FYu%TNSbMCxc3t2u^XT"
md=md5()
md.update(str_.encode())
sign=md.hexdigest()
data={
'i': word,
'from': 'AUTO',
'to': 'AUTO',
'smartresult':' dict',
'client': 'fanyideskweb',
'salt': salt,
'sign': sign,
'lts': ts,
'bv': 'd9afd7419c0c736c1d10ae4179955b06',
'doctype': 'json',
'version': '2.1',
'keyfrom': 'fanyi.web',
'action':'FY_BY_REALTlME',
}
html=requests.post(url=url,data=data,headers=headers).json()
print(html['translateResult'][0][0]['tgt'])