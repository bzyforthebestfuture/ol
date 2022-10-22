import requests
import re
import xlwt


url='https://www.zhihu.com/hot'
headers={'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'}#伪装

response=requests.get(url=url,headers=headers)
html_data=response.text

title_list=re.findall('\{"HotItem-title":.*?\}',html_data)

for title_ in title_list:
    a1=re.findall('"a1":"(.*?)"',title_)[0]
    print(a1)
for title_ in title_list:
    a1=re.findall('"a2":"(.*?)"',title_)[0]
    print(a1)
for title_ in title_list:
    a1=re.findall('"a3":"(.*?)"',title_)[0]
    print(a1)
for title_ in title_list:
    a1=re.findall('"a4":"(.*?)"',title_)[0]
    print(a1)
for title_ in title_list:
    a1=re.findall('"a5":"(.*?)"',title_)[0]
    print(a1)


book=xlwt.Workbook(encoding='utf-8',style_comprehession=0)  #创建excel表格类型文件
sheet=book.add_sheet('第一题')                          #建立一张表单
col=('热点分类','标题','链接','热力值')                             #自定义列名
for i in range(0,4):                    #n为列数
    sheet.write(0,i,col[i])    #将元组col写入sheet表单中


datalist=[['1','2','3']]        #将数据写进表单中           ！！！！！！！！！！！！！！！！！！！！
for i in range(0,2):
    data=datalist[i]
    for j in range(0,8):
        sheet.write(i+1,j,data[j])

#保存excel文件完成任务撒花
savepath='C:/Users/DELL/Desktop/excel表格.xls'
book.save(savepath)



















