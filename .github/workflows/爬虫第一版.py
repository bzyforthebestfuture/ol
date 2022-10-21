#https://www.zhihu.com/creator/hot-question/hot/0/hour
#cookie:https://www.zhihu.com
#
import time
import requests
from bs4 import BeautifulSoup

# 设置headers，复制headers的时候注意不要搞错了
url = 'https://www.zhihu.com/hot'
headers = {
'cookie':'...',		# 填入你的cookie
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.3',
}

# python的接口很方便，这么几行就能完成热榜标题的提取
def getHot()->list:
    try:
        # 简单直接的方法获取页面内容
        res = requests.get(url,headers=headers)
        html = res.text
        
        # 处理网页内容，提取热榜标题和链接
        soup = BeautifulSoup(html, 'lxml')
        hot_list = soup.select('#TopstoryContent > div > div > div.HotList-list > section > div.HotItem-content > a')
        hot_list = [hot['title'] + "\n" + hot['href'] +'\n' for hot in hot_list]
        return hot_list[0:10]
    
    # 如果断网了，则上面这段代码会抛出异常，需进行处理
    except:
        print("[",cur_time(),"]:当前网络不可用，60s后将再次尝试连接网络\n")
        time.sleep(60)
        return []








# 检查，每隔一段时间检查一次热榜，将新增的标题打印出来
def checkUpdate():
    # 每10分钟检查一次更新
    print("\n*********************知乎热榜*********************\n")
    hot_list_old = []
    while hot_list_old == []:
        hot_list_old = getHot()
    print("当前热榜前十\t [time:" + cur_time() +']\n')
    for hot in hot_list_old:
        print(hot)
    print("\n\n********************每分钟刷新一次********************\n")
    while(1):
        time.sleep(60)
        hot_list_new = getHot()
        flag = 0
        while(hot_list_new == []):
            flag = 1
            hot_list_new = getHot()
        if flag == 1:
            print("[",cur_time(),"]:网络连接已恢复")
        # 对比两次热榜是否相同，将新榜中新增的标题提取出来
        for hot_new in hot_list_new:
            flag = 0    # 更新标记
            for hot_old in hot_list_old:
                if hot_new == hot_old:
                    flag = 1
            if flag == 0:
                print(cur_time(),"\t",hot_new)
        hot_list_old = hot_list_new
# 获取当前时间
def cur_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 



