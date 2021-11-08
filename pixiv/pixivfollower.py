import requests
repeat=0;
def getSinglefollow(id):
    follower=[]
    for i in range(10):
        url='https://www.pixiv.net/ajax/user/'+id+'/following?offset='+i*24+'&limit=24&rest=show&tag=&lang=zh'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
            'cookie':'your cookie',
            'referer': 'https://www.pixiv.net/users/'+id+'/following',
        }
        response = requests.get(url, headers=headers).json()
        users = response['body']['users']
        print(users)
        for user in users:
            id = user['userId']
            getSinglefollow(id)
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
            follower.append(
                {'id': id, 'username': username, 'img_id': imgs_id, 'img_title': imgs_title, 'img_url': imgs_url})
    return follower
def getAllfollow():
    global repeat
    followers=[]
    follower=[]
    s=requests.session()
    headers1 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'cookie': 'your cookie',
        'referer': 'https://www.pixiv.net/users/6662895/following',
    }
    # url = 'https://www.pixiv.net/ranking.php?mode=daily&content=illust&p=%d&format=json' % n
    # url='https://www.pixiv.net/ajax/user/6662895/following?offset=0&limit=24&rest=show&tag=&lang=zh'
    for i in range(10):
        url='https://www.pixiv.net/ajax/user/6662895/following?offset='+i*24+'&limit=24&rest=show&tag=&lang=zh'
        response = s.get(url, headers=headers1).json()
        users = response['body']['users']
        print(users)
        for user in users:
            id=user['userId']
            if(repeat<4):
                followers.append(getSinglefollow(id))
                repeat+=1
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
    print(followers)
getAllfollow()