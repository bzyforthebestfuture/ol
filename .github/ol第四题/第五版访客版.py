import requests
import pandas
import xlwt
from bs4 import BeautifulSoup
# useragent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36
#https://www.zhihu.com/creator/hot-question/hot/100001/hour
headers = {'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'
         'Cookie=_zap=08b91689-ad8c-482f-a389-d6885a21b98a; d_c0=AACYu_jdgBWPTmQ7WnVayFQgwUJSRn8IXlM=|1662205375; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=pLzv8rqti6FBUUUBBRKAHpYoXTV5lV9Q; captcha_session_v2=2|1:0|10:1665908883|18:captcha_session_v2|88:OFZWNFM4REVqVnNqTE1zVEhPTXNiTy9YTDEwaWpjeDZNYkl0WitTUDBjVW5lVzVvTUZCM1kyK21hS0hUckJNKw==|7256789e16a2a6f80dc8cc3d10b34117e71aac6f1cd6f341afc7d4df6c18f293; __snaker__id=bj7vJBY6Bg1VgKcN; gdxidpyhxdE=Cp33N%2FT860nH8zBRfpDmm6tv4cYgxcJpx3OYEVKWcc3oeDaKYWjGkOn1Btnf8ceJI4Uxpc6mVKVvr0WXzUOb1c%2FMiQ38ROWIPiMZLBkCNi4m5BGi%5CTkzs3Mne6oAHBZSXdyznsMDu6V47Qi%2FjoA88gQQ2yCQM1QVj0gk4irB%2Fl2Un%2BjD%3A1665909782352; captcha_ticket_v2=2|1:0|10:1665908903|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfeS1RWG1fUjlPckdmSlJLY0o5cnJpNk1XMk1qUmFiMTEtdnJoRGIyNGZBakxMTFVDT2JtcGJBZHRib3dsZVhjTFdWazE1QlotcVZIRktMTEE2dTBTMlEyamRuZjBUYy5FbDRiWVU2TllfSzIydzk4RlNzSnlvdTRINU9LdjZ0WXhCYjFmdndRV3E4RU5RQTJiYTlJUm4wWGQweEhIQzRRLmlYLXRZNWZyaS1ldUNRb1VSTmpUMGlMSHh0dC45Ulh1Tk5ZZk91emlrQS1pZHluUFoydXVDZDFySW5FLVlxelNCWUI0cnk0bVVpTy1hWjZ6dkdQZUtGbVpsdXNDV3lqRGd6UTBKd1BnZy5sRW1qcy1SV2hENFZtaG5fYmd6ZmxpQ0xnMU9PaWRuWjdPWWdKMExKamQ1dnpOUGFmWE5oejBfOWpXb3lOYjBwUmlHLWpTa0dRX0JJVHhUcHVRd3BxbFNvZjlHYkJRV2VPek42Mk53dG80UmsxWEZqN29sSjhKd3BzZHAyMWRoOFVtaGhENTdSR19YNDlFQ0IxUERVUElkdmdwOUFnTFpXQkhvTi45dTFpOTRPNzlqdVFMOWlzcWNqNTF5end1cGp6MGljQjRWN1lXZy1DVU9hUmkyNF9hQmtvbmJJaVJKS2I3MU9aRGJKRUhJT1c4NmFaMyJ9|b5a6ca25f0f419005495978db1612f40dcc69f44e1c759553203182ae402edc6; YD00517437729195%3AWM_NI=2YSJocYMJYBcccZoyBYY687LakJxcnXgSF4E4O%2BgibNbhFrkgGnktrPLiNMjK6ZW%2Bn2cShpF1cy9Q%2FQwACDdSEG6eDJQVBTJ2Od0yisBjKws23cDKniq%2FELjD8iM4mPqSHk%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed2f7498ae7f9add649a68e8fa2d55b978a8aadd544f5babad7e7448898be85f72af0fea7c3b92af2879dabee699b9386bac169a1bd9690fc4a9b87fad9b648a3b58699e2669cb99da7b74ff891e588ec6a8ebea8a7f161a599a28cf77a9494a7afd06289ea96b8aa66f2bd9d89f34ef3bdb7dad42593a98fa4c770919b89d7e8508a8f9aa3d742f291acd1fc63b19ea6acf679f2edada5ca66abafe1a6cf6288e8a7aeb76794af9da9ea37e2a3; z_c0=2|1:0|10:1665908916|4:z_c0|92:Mi4xOU5RbVBBQUFBQUFBQUppNy1OMkFGU1lBQUFCZ0FsVk50QTQ1WkFDajU5dHdxTFRnWUZfbzVvczVQNlB0NlNVYXdR|68c14fc9619bff33fb45cbae10573eeb8bdb07a32943a7db132326de65a184bb; q_c1=922d79d720f047e882bc659efc7348c2|1665908916000|1665908916000; tst=h; _xsrf=e3d535b0-4627-4952-a306-d3905de576a3; SUBMIT_0=71bdb433-4cc0-4125-93ec-2b0264cbaff6; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1666279488,1666347273,1666363948,1666398180; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1666398180; NOT_UNREGISTER_WAITING=1; KLBRSID=f48cb29c5180c5b0d91ded2e70103232|1666398201|1666398180'}
url = 'https://www.zhihu.com/creator/hot-question/hot/100001/hour'
resp = requests.get(url=url,headers=headers)
html=resp.text
soup = BeautifulSoup(html, 'lxml')
contents = soup.find_all('div', class_='HotItem-content')
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
#
#
book=xlwt.Workbook(encoding='utf-8',style_comprehession=0)  #创建excel表格类型文件
sheet=book.add_sheet('知乎热门榜单')                          #建立一张表单
col=('热度', '标题', '摘录')                             #自定义列名
for i in range(0,3):                    #n为列数
    sheet.write(0,i,col[i])    #将元组col写入sheet表单中


data_list=[['title_list', 'hot_list', 'excerpt_list']]        #将数据写进表单中
for i in range(0,3):
    data = data_list[i]
    print(data.__len__())
    for j in range(0,100):
        sheet.write(i+1,j,data[j])

#保存excel文件完成任务撒花
savepath = 'C:/Users/20253/Desktop/新建文件夹 (2)/excel表格.xls'
book.save(savepath)
#
#
#
#
#
# dataframe = pandas.DataFrame(data=data)
# dataframe.to_excel('C:/Users/20253/Desktop/openlab/hot.XLSX', index=False, encoding='utf-8')
