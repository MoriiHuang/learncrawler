import requests
import re
import time
print("目前支持的方法有：Ranking，Search（请不要修改格式）")
word=input("请输入爬取方式：")
repeat = 1
def getSinglePic(url,headers):
    global repeat
    response = requests.get(url, headers=headers)
    # 提取图片名称
    name = re.search('"illustTitle":"(.+?)"', response.text)
    name=name.group(1)
    if re.search('[\\\ \/ \* \? \" \: \< \> \|]', name) != None:
        name = re.sub('[\\\ \/ \* \? \" \: \< \> \|]', str(repeat), name)
        repeat += 1
    # 提取图片原图地址
    picture = re.search('"original":"(.+?)"},"tags"', response.text)
    pic = requests.get(picture.group(1), headers=headers)
    print(picture.group(1))
    f = open("./html/" + '%s.%s' % (name, picture.group(1)[-3:]), 'wb')
    f.write(pic.content)
    f.close()


def getAllPicUrlRank():
    headers1 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'referer': 'https://www.pixiv.net/ranking.php?mode=daily&content=illust',
    }
    count = 1
    for n in range(1, 10 + 1):
        url = 'https://www.pixiv.net/ranking.php?mode=daily&content=illust&p=%d&format=json' % n
        response = requests.get(url, headers=headers1)
        illust_id = re.findall('"illust_id":(\d+?),', response.text)
        picUrl = ['https://www.pixiv.net/artworks/' + i for i in illust_id]
        for url in picUrl:
            print('正在下载第 %d 张图片' % count, end='   ')
            getSinglePic(url,headers1)
            time.sleep(5)
            print('下载成功', end='\n')
            count += 1
    return None
def getALlPicUrlSearch():

    keyword = input("请输入关键字:")
    referer = ('https://www.pixiv.net/tags/' + keyword + '/artworks').encode("utf-8").decode("latin1")
    headers2 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'referer': referer,
    }
    for i in range(1,11):
        url = 'https://www.pixiv.net/ajax/search/artworks/' + keyword + '?word=' + keyword + '&order=date_d&mode=all&p=%d&s_mode=s_tag_full&type=all&lang=zh' % i
        response = requests.get(url=url, headers=headers2)
        # step3 获取相应数据text返回的是字符串形式的相应数据
        page_text = response.json()
        html = []
        count = 1
        for page in page_text['body']['illustManga']['data']:
            html.append(page['id'])
        picUrl = ['https://www.pixiv.net/artworks/' + i for i in html]
        for url in picUrl:
            print('正在下载第 %d 张图片' % count, end='   ')
            getSinglePic(url,headers2)
            time.sleep(5)
            print('下载成功', end='\n')
            count += 1
if(word=="Ranking"):
    getAllPicUrlRank()
if(word=="Search"):
    getALlPicUrlSearch()

