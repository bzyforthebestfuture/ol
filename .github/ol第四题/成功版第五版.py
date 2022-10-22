import random
import requests
import re
from bs4 import BeautifulSoup
import xlwt
#头部列表
agent_list = [
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    # IPod
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    # IPAD
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    # Android
    "Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    # QQ浏览器 Android版本
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    # Android Opera Mobile
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    # Android Pad Moto Xoom
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    # BlackBerry
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    # WebOS HP Touchpad
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    # Nokia N97
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    # Windows Phone Mango
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    # UC浏览器
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    # UCOpenwave
    "Openwave/ UCWEB7.0.2.37/28/999",
    # UC Opera
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999"
    ]

head = {"user-agent":random.choice(agent_list)}

url = "https://www.zhihu.com/billboard"
response = requests.get(url,headers=head)

#创建BeautifulSoup对象
html = BeautifulSoup(response.text,"lxml")

#通过find爬取script并返回字符串
script_text = html.find("script",id="js-initialData").get_text()

#通过正则抓取hotList到huestFeeds中的内容
result = re.findall(r'"hotList":(.*),"guestFeeds"',script_text)
#把false,ture转为False,True
temp = result[0].replace("false","False").replace("true","True")
#把字符串转为python数据
hot_list = eval(temp)

for i in hot_list:
    BT = i["target"]["titleArea"]["text"]
    HOST = i["target"]["metricsArea"]["text"]
    zh_url = i["target"]["link"]["url"]
    print(BT, HOST, zh_url)



book=xlwt.Workbook(encoding='utf-8')  #创建excel表格类型文件
sheet=book.add_sheet('知乎热门榜单')                          #建立一张表单
col=('标题', '热度', '链接')                             #自定义列名
for i in range(0,3):                    #n为列数
    sheet.write(0,i,col[i])    #将元组col写入sheet表单中


data_list=[['BT', 'HOST', 'zh_url']]        #将数据写进表单中
for i in range(0,3):
    data = data_list[i]
    print(data.__len__())
    for j in range(0,1):
        sheet.write(i+1,j,data[j])

#保存excel文件完成任务撒花
savepath = 'C:/Users/20253/Desktop/新建文件夹 (2)/新建 Microsoft Excel 工作表.XLSX'
book.save(savepath)



#,style_comprehession=0