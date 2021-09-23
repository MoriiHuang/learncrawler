import requests
from lxml import etree
import random
import os
from multiprocessing.dummy import Pool

if not os.path.exists('./video'):
    os.mkdir('./video')
headers={
        'User_Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
url='https://www.pearvideo.com/category_5'
page_text=requests.get(url=url,headers=headers).text
tree=etree.HTML(page_text)
li_list=tree.xpath('//*[@id="listvideoListUl"]/li')
urls=[]
for li in li_list:
    detail_url='https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
    #print(detail_url,name)
    #对详情页发起请求
    detail_page_text=requests.get(url=detail_url,headers=headers).text
    new_tree=etree.HTML(detail_page_text)
    name=new_tree.xpath('//*[@id="detailsbd"]/div[1]/div[2]/div/div[1]/h1/text()')[0]
    #print(name)
    id_= str(li.xpath('./div/a/@href')[0]).split('_')[1]
    ajax_url = 'https://www.pearvideo.com/videoStatus.jsp?'
    params = {
    'contId': id_,
    'mrd': str(random.random())
    }
    ajax_headers={
        'User_Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'Referer':'https://www.pearvideo.com/video_'+id_
    }
    detail_obj=requests.get(url=ajax_url,headers=ajax_headers,params=params).json()
    #print(detail_obj)
    video_url=detail_obj["videoInfo"]['videos']["srcUrl"]
    video_true_url = ''
    s_list = str(video_url).split('/')
    #print(s_list)
    for i in range(0, len(s_list)):
        if i < len(s_list) - 1:
            video_true_url += s_list[i] + '/'
        else:
            ss_list = s_list[i].split('-')
    for j in range(0, len(ss_list)):
        if j == 0:
            video_true_url += 'cont-' + id_ + '-'
        elif j == len(ss_list) - 1:
            video_true_url += ss_list[j]
        else:
            video_true_url += ss_list[j] + '-'
        dic={
            'name':name,
            'url':video_true_url
        }
        urls.append(dic)
    def get_video_data(dic_):
        url_=dic_['url']
        print(dic_['name'],"正在下载......")
        video_data=requests.get(url=url_,headers=headers).content
        video_path='./video/'+dic_['name']+'.mp4'
        with open(video_path,'wb') as fp:
            fp.write(video_data)
            print(dic_['name'],'下载成功！')
    pool=Pool(4)
    pool.map(get_video_data,urls)

    pool.close()
    pool.join()