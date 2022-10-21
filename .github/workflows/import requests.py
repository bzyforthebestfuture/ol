import requests
from bs4 import BeautifulSoup
 
 
url = 'https://www.bilibili.com/v/popular/rank/all'  # 爬取B站排行榜（总榜）上视频链接
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
# 定义列表来存储数据
Type = []  # 作品的类型
URL = []  # 链接
Name = []  # 标题
Author=[] #作者
Degree_heat=[] #热力值
# 利用bs4，找到视频链接以及视频名字和up主
get_Author = soup.find_all('span', class_='data-box up-name', )
get_url = soup.find_all('a', class_="title")
# 将数据存入列表中
for data in get_Author:
    author = data.text.replace('\n', '').replace(' ', '')
    Author.append(author)
for item in get_url:
    URL.append(item['href'].replace('//', 'https://'))  # 找到链接并转换成链接形式
    Name.append(item.text)
 
# 将数据写入文件中保存下来
header = ['类型', '作者', '作品名','作品链接','热力值']
headers = ','.join(header)
date = (list(z) for z in zip(Type,URL,Name,Degree_heat))  # 把数据成组，方便写入文件。
with open("作品数据.csv", 'w+', encoding='utf-8') as f:
    f.write(headers+'\n')
    for i in date:
        i = ','.join(i)  # 将列表转为字符串
        f.writelines(i+'\n')
print('{:*^30}'.format('保存成功！'))