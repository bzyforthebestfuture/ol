import requests
import pandas
import xlwt
from bs4 import BeautifulSoup
# useragent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36
#https://www.zhihu.com/creator/hot-question/hot/100001/hour
headers = {'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'
         'Cookie=https://www.zhihu.com/'}
url = 'https://www.zhihu.com/creator/hot-question/hot/100001/hour'
resp = requests.get(url=url,headers=headers).text
soup = BeautifulSoup(resp,'lxml')
contents = soup.find_all('div',class_='HotItem-content')
title_list, hot_list, excerpt_list = [], [], []
for content in contents:
    title = content.find('h2').string
    hot = content.find('div', class_='HotItem-metrics').get_text()
    try:
        excerpt=content.find('p').string
    except AttributeError:
        excerpt=''
    title_list.append(title)
    hot_list.append(hot.split(' ')[0])
    excerpt_list.append(excerpt)

data = {
    '热度': hot_list,
    '标题': title_list,
    '摘录': excerpt_list,
}


book=xlwt.Workbook(encoding='utf-8',style_comprehession=0)  #创建excel表格类型文件
sheet=book.add_sheet('知乎热门榜单')                          #建立一张表单
col=('热度', '标题', '摘录')                             #自定义列名
for i in range(0,3):                    #n为列数
    sheet.write(0,i,col[i])    #将元组col写入sheet表单中


data_list=[['title_list', 'hot_list', 'excerpt_list']]        #将数据写进表单中
for i in range(0,3):
    data = data_list[i]
    for j in range(0,100):
        sheet.write(i+1,j,data[j])

#保存excel文件完成任务撒花
savepath = 'C:/Users/20253/Desktop/新建文件夹 (2)/excel表格.xls'
book.save(savepath)






#dataframe = pandas.DataFrame(data=data)
# dataframe.to_excel('C:/Users/20253/Desktop/openlab/hot.XLSX', index=False, encoding='utf-8')