import requests
import random
import time
from lxml import etree
import json
url='http://zwfw.san-he.gov.cn/icity/icity/guestbook/interact'
s=requests.session()
headers={
# 'Cache-Control':'no-cache',
# 'Connection':'keep-alive',
# 'Content-Length':'14165',
# 'Content-Type':'application/json;charset=utf-8',
# 'Expires':'0',
# 'Pragma':'no-cache',
# 'Set-Cookie':'ICITYSession=3e8a0279bc2746559899596a3fec4edd;Path=/;HttpOnly',
# 'Accept':'application/json,text/javascript,*/*;q=0.01',
# 'Accept-Encoding':'gzip,deflate',
# 'Accept-Language':'zh-CN,zh;q=0.9',
# 'Connection':'keep-alive',
# 'Content-Length':'47',
# 'Content-Type':'application/json',
'Cookie':'ICITYSession=3e8a0279bc2746559899596a3fec4edd',
# 'Host':'zwfw.san-he.gov.cn',
# 'Origin':'http://zwfw.san-he.gov.cn',
# 'Referer':'http://zwfw.san-he.gov.cn/icity/icity/guestbook/interact',
'User-Agent':'Mozilla/5.0(Macintosh;IntelMacOSX10_15_7)AppleWebKit/537.36(KHTML,likeGecko)Chrome/94.0.4606.61Safari/537.36',
'X-Requested-With':'XMLHttpRequest',
}
data='{"start":  ,"limit": 7,"TYPE@=":"2","OPEN@=": "1",}'
for page in range(6):
    tmp=data
    tmp=data[:10]+str(page*7)+data[11:]
    print(tmp)
    m = s.get(url=url, headers=headers).text
    tree = etree.HTML(m)
    r = tree.xpath('/html/head/script[1]/text()')
    word1 = r[0][57:76]
    key = ''
    keyindex = -1
    chars = '0123456789abcdef'
    for i in range(6):
        c = word1[keyindex + 1]
        key += c
        if (c in chars):
            keyindex = chars.index(c)
        else:
            keyindex = i
    print(key)
    word2 = str(int(random.randint(999, 10000))) + "_" + key + "_" + str(int(time.time())) + '000'
    word2.replace('+', "_")
    print(word1, word2)
    start_url='http://zwfw.san-he.gov.cn/icity/api-v2/app.icity.guestbook.WriteCmd/getList?s='+word1+'&t='+word2;
    response=requests.post(url=start_url,headers=headers,data=tmp)
    print(response.json())
    filename='三和市政府报告.json'
    fp=open(filename,'w')
    json.dump(response.json(),fp=fp,ensure_ascii=False)