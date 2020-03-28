import requests
from lxml import etree 
import os

output_dir = 'output'

try:
    os.makedirs(output_dir)
except:
    pass


# 发起requests 获取Html内容
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 Edg/80.0.361.66'}
r = requests.get('https://movie.douban.com/top250',headers =headers)

# 解析Html，提取数据
html = etree.HTML(r.text)
xpath_name = '//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()'
movie_names = html.xpath(xpath_name)
# print(movie_names)


# 存储数据
with open(os.path.join(output_dir, 'movies.csv'), 'w') as outfile:
    outfile.write('movie_name\n')
    for movie_name in movie_names:
        # print(movie_name)
        outfile.write(movie_name)
        outfile.write('\n')
