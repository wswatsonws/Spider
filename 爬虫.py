import json
import re
import urllib.request as request
import _json
# if has Chinese, apply decode()
url = 'https://api.douban.com/v2/movie/top250'
html = request.urlopen(url).read().decode('utf8')
top20 = json.loads(html)['subjects']

for movie in top20:
    url = 'https://api.douban.com/v2/movie/'+movie['id']
    movieContent = request.urlopen(url).read().decode('utf8')
    #print(json.loads(movieContent))
    print(json.loads(movieContent)['title'] + ': ' + json.loads(movieContent)['rating'][
        'average'])


print(json.loads(html))
#print(html)



