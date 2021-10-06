import re
#  下方引号内添加替换掉请求头内容
headers_str = """
Cache-Control: no-cache
Connection: keep-alive
Content-Length: 14165
Content-Type: application/json;charset=utf-8
Expires: 0
Pragma: no-cache
Set-Cookie: ICITYSession=3e8a0279bc2746559899596a3fec4edd; Path=/; HttpOnly
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Length: 47
Content-Type: application/json
Cookie: ICITYSession=3e8a0279bc2746559899596a3fec4edd
Host: zwfw.san-he.gov.cn
Origin: http://zwfw.san-he.gov.cn
Referer: http://zwfw.san-he.gov.cn/icity/icity/guestbook/interact
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36
X-Requested-With: XMLHttpRequest
"""

pattern = '^(.*?):(.*)$'


for line in headers_str.splitlines():
    print(re.sub(pattern,'\'\\1\':\'\\2\',',line).replace(' ',''))