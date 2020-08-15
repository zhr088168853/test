import urllib.request
import urllib.parse
content = input('请输入需要翻译的内容：')
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
data = {'from': 'zh',
'to': 'en',
'query': content ,
'simple_means_flag': '3',
'sign': '949163.694426',
'token': '5163907cf8a09f5717c0f94e267644f5',
'domain': 'common'}
re = urllib.request.Request('https://fanyi.baidu.com/v2transapi?from=en&to=zh',headers=headers)
data = urllib.parse.urlencode(data).encode('utf-8')
res = urllib.request.urlopen(re,data)
html = res.read().decode('utf-8')
result = json.loads(html)
print(result)
