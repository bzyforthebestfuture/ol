import requests
if __name__=="__main__":
    url='https://www.zhihu.com/creator/hot-question/hot/100001/hour'
    response=requests.get(url=url)
    page_text=response.text
    print(page_text)
    with open('./bilibili.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束')