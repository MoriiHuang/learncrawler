import tesserocr
import requests
from lxml import etree
import time
from PIL import Image
s=requests.session()
headers={
        'User_Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
r=s.get(url,headers=headers)
res=etree.HTML(r.text)
VIEWSTATE=res.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
VIEWSTATEGEN=res.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]
r=res.xpath('//*[@id="imgCode"]/@src')[0]
url0='https://so.gushiwen.cn'
url1=url0+r
code_img_data=s.get(url=url1,headers=headers).content
with open('./03.jpeg','wb') as fp:
     fp.write(code_img_data)
# image = Image.open('03.jpeg')
# #text = pytesseract.image_to_string(image,lang='chi_sim') # 这样就'./能识别中文了
# text = tesserocr.image_to_text(image)
# print(text)
#post请求的发送（模拟登陆）
result=input("请输入验证码：")
login_url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
data={
'__VIEWSTATE':VIEWSTATE,
'__VIEWSTATEGENERATOR':VIEWSTATEGEN,
'from': 'http://so.gushiwen.cn/user/collect.aspx',
'email': 'nv5110911jiaobei7@163.com',
'pwd': '1513120xxy',
'code': result,
'denglu': '登录'
}
response=s.post(url=login_url,headers=headers,data=data)
print(response.status_code)
login_page_text=response.text
with open('./guwen.html','w') as fp:
    fp.write(login_page_text)
