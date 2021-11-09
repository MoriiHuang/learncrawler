import requests
import collections
import json
followers = []
ids=collections.deque()
id_used=[6662895]
def dumptojson(res):
    fp = open('homework.json', 'w', encoding='utf-8')
    json.dump(res, fp=fp, ensure_ascii=False)
def getSinglefollow1(id):
    follower=[{'main_id':id}]
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'cookie': 'first_visit_datetime_pc=2021-01-28+09:37:46; yuid_b=NkaTUSk; p_ab_id=1; p_ab_id_2=4; p_ab_d_id=1577289544; a_type=0; b_type=1; cto_bundle=EFPR519GUjBEVzRkSTFYeXlWSVpHb0VaWmROeldnV0tBTG9paFNWUUV5JTJCNDZLJTJGbE9lMGdrbHBYRE9OUUYzJTJCdGdvTkpzZnJwRFBGeVBwOWUlMkJNNExxM0RneTJCNGlsVzlzczd1VlRjMkI3bEgzQXRJTXllSFpLaGlUWHVlWnNidVVZZjJi; c_type=25; login_ever=yes; __utmz=235335808.1631336752.3.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not provided); __utmv=235335808.|2=login ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=14078221=1^9=p_ab_id=1=1^10=p_ab_id_2=4=1^11=lang=zh=1; _ga=GA1.2.257473138.1612919016; privacy_policy_notification=0; ki_s=; _im_uid.3929=b.cec15a91dc4d4c65; tag_view_ranking=RTJMXD26Ak~_EOd7bsGyl~QaiOjmwQnI~jk9IzfjZ6n~_hSAdpN9rx~WuRP3NHCdl~geozHUfkjH~jO2POikggL~3ogUTkvvsO~CFcfY7SdnH~qx-Tlvmbdj~azESOjmQSV~_Jc3XITZqL~q303ip6Ui5~zIv0cf5VVk~WdKNu4p5bE~Ce-EdaHA-3~hW_oUTwHGx~eVxus64GZU~HY55MqmzzQ~ZTBAtZUDtQ~iUx3FpZLw5~cIofvt9YXx~y3NlVImyly~O7QBeW3lwy~LjyHBw5hxm~ETjPkL0e6r~g0twlxZSYP~bdaGGvQc_Q~AjBDLpRc95~-djhIhdgci~0xsDLqCEW6~Bd2L9ZBE8q~JXmGXDx4tL~cbmDKjZf9z~r01unnQL0a~Ie2c51_4Sp~KOnmT1ndWG~-StjcwdYwv~cFXtS-flQO; ki_r=; _gcl_au=1.1.1160468973.1636365478; __utma=235335808.257473138.1612919016.1631336752.1636365478.4; __utmc=235335808; __utmt=1; __cf_bm=VN7K1cUnJU6VatjJU_KGoqhNpQpgBoZiy7vAP8adRjg-1636365478-0-AYesem9oKB0HPW9QWWbR0nttmzSNQs9/XdlShp/DVCJHXLlJGu0eWkk4UEWb86B5gq904+djVF5iNtpfBEsmB+AXB12w3hlffm28bvKrQFcm9s0C6zwrqBp+b/hC+CrmT2TnIgFE4UIx1al2bgdsUEoA2tuIxxWU+4EfVpyfmcZA5pKHw65ZqxVhEtXYMoX0RQ==; tags_sended=1; categorized_tags=AjBDLpRc95~BeQwquYOKY~IRbM9pb4Zw~O7QBeW3lwy~Q54wE_yVW1~TPgZgSSzGU~WuRP3NHCdl~m3EJRa33xU; _gid=GA1.2.1197812392.1636365483; PHPSESSID=14078221_nDcRmpTaVc2zq8LO4tq8fm8UxKHr2jiq; device_token=915f62262524cea298b51cf70145f225; privacy_policy_agreement=0; __utmb=235335808.3.10.1636365478; ki_t=1611794303684;1636365488338;1636365512586;6;10',
        'referer': 'https://www.pixiv.net/users/' + id + '/following',
    }
    url = 'https://www.pixiv.net/ajax/user/'+id+'/following?offset=0&limit=24&rest=show&tag=&lang=zh'
    response =requests.get(url, headers=headers).json()
    total = users = response['body']['total']
    for i in range(0,total,24):
        url='https://www.pixiv.net/ajax/user/'+id+'/following?offset='+str(i*24)+'&limit=24&rest=show&tag=&lang=zh'
        response = requests.get(url, headers=headers).json()
        users = response['body']['users']
        for user in users:
            id = user['userId']
            if(id not in id_used):
                ids.append(id)
            username = user['userName']
            illusts = user['illusts']
            imgs_id = []
            imgs_title = []
            imgs_url = []
            for illust in illusts:
                img_id = illust['id']
                img_title = illust['title']
                img_url = illust['url']
                imgs_id.append(img_id)
                imgs_title.append(img_title)
                imgs_url.append(img_url)
            follower.append({'id': id, 'username': username, 'img_id': imgs_id, 'img_title': imgs_title, 'img_url': imgs_url})
            print(follower)
    return follower
def getAllfollow():
    global repeat
    follower=[{'main_id':6662895}]
    s=requests.session()
    url = 'https://www.pixiv.net/ajax/user/6662895/following?offset=0&limit=24&rest=show&tag=&lang=zh'
    headers1 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'cookie': 'first_visit_datetime_pc=2021-01-28+09:37:46; yuid_b=NkaTUSk; p_ab_id=1; p_ab_id_2=4; p_ab_d_id=1577289544; a_type=0; b_type=1; cto_bundle=EFPR519GUjBEVzRkSTFYeXlWSVpHb0VaWmROeldnV0tBTG9paFNWUUV5JTJCNDZLJTJGbE9lMGdrbHBYRE9OUUYzJTJCdGdvTkpzZnJwRFBGeVBwOWUlMkJNNExxM0RneTJCNGlsVzlzczd1VlRjMkI3bEgzQXRJTXllSFpLaGlUWHVlWnNidVVZZjJi; c_type=25; login_ever=yes; __utmz=235335808.1631336752.3.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not provided); __utmv=235335808.|2=login ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=14078221=1^9=p_ab_id=1=1^10=p_ab_id_2=4=1^11=lang=zh=1; _ga=GA1.2.257473138.1612919016; privacy_policy_notification=0; ki_s=; _im_uid.3929=b.cec15a91dc4d4c65; tag_view_ranking=RTJMXD26Ak~_EOd7bsGyl~QaiOjmwQnI~jk9IzfjZ6n~_hSAdpN9rx~WuRP3NHCdl~geozHUfkjH~jO2POikggL~3ogUTkvvsO~CFcfY7SdnH~qx-Tlvmbdj~azESOjmQSV~_Jc3XITZqL~q303ip6Ui5~zIv0cf5VVk~WdKNu4p5bE~Ce-EdaHA-3~hW_oUTwHGx~eVxus64GZU~HY55MqmzzQ~ZTBAtZUDtQ~iUx3FpZLw5~cIofvt9YXx~y3NlVImyly~O7QBeW3lwy~LjyHBw5hxm~ETjPkL0e6r~g0twlxZSYP~bdaGGvQc_Q~AjBDLpRc95~-djhIhdgci~0xsDLqCEW6~Bd2L9ZBE8q~JXmGXDx4tL~cbmDKjZf9z~r01unnQL0a~Ie2c51_4Sp~KOnmT1ndWG~-StjcwdYwv~cFXtS-flQO; ki_r=; _gcl_au=1.1.1160468973.1636365478; __utma=235335808.257473138.1612919016.1631336752.1636365478.4; __utmc=235335808; __utmt=1; __cf_bm=VN7K1cUnJU6VatjJU_KGoqhNpQpgBoZiy7vAP8adRjg-1636365478-0-AYesem9oKB0HPW9QWWbR0nttmzSNQs9/XdlShp/DVCJHXLlJGu0eWkk4UEWb86B5gq904+djVF5iNtpfBEsmB+AXB12w3hlffm28bvKrQFcm9s0C6zwrqBp+b/hC+CrmT2TnIgFE4UIx1al2bgdsUEoA2tuIxxWU+4EfVpyfmcZA5pKHw65ZqxVhEtXYMoX0RQ==; tags_sended=1; categorized_tags=AjBDLpRc95~BeQwquYOKY~IRbM9pb4Zw~O7QBeW3lwy~Q54wE_yVW1~TPgZgSSzGU~WuRP3NHCdl~m3EJRa33xU; _gid=GA1.2.1197812392.1636365483; PHPSESSID=14078221_nDcRmpTaVc2zq8LO4tq8fm8UxKHr2jiq; device_token=915f62262524cea298b51cf70145f225; privacy_policy_agreement=0; __utmb=235335808.3.10.1636365478; ki_t=1611794303684;1636365488338;1636365512586;6;10',
        'referer': 'https://www.pixiv.net/users/6662895/following',
    }
    response = s.get(url, headers=headers1).json()
    total= response['body']['total']
    # url = 'https://www.pixiv.net/ranking.php?mode=daily&content=illust&p=%d&format=json' % n
    # url='https://www.pixiv.net/ajax/user/6662895/following?offset=0&limit=24&rest=show&tag=&lang=zh'
    for i in range(0,total,24):
        url='https://www.pixiv.net/ajax/user/6662895/following?offset='+str(i)+'&limit=24&rest=show&tag=&lang=zh'
        response = s.get(url, headers=headers1).json()
        users = response['body']['users']
        for user in users:
            id = user['userId']
            ids.append(id)
            username=user['userName']
            illusts=user['illusts']
            imgs_id=[]
            imgs_title=[]
            imgs_url=[]
            for illust in illusts:
                img_id=illust['id']
                img_title=illust['title']
                img_url=illust['url']
                imgs_id.append(img_id)
                imgs_title.append(img_title)
                imgs_url.append(img_url)
            follower.append({'id':id,'username':username,'img_id':imgs_id,'img_title':imgs_title,'img_url':imgs_url})
        followers.append(follower)
    while(len(ids)<10000):
        cur_id=ids.popleft()
        id_used.append(cur_id)
        followers.append(getSinglefollow1(cur_id))
    print(len(ids))
    return followers
res=getAllfollow()
dumptojson(res)
