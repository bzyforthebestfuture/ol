#https://zhuanlan.zhihu.com/p/574071028
import requests
from lxml import html
import xlwt
import os

# 爬取b站热门视频信息
def spider(video_list):
    url = 'https://zhuanlan.zhihu.com/p/574071028'
    html_data = requests.get(url).text
    selector = html.fromstring(html_data)
    infolist = selector.xpath('//li[@class="rank-item"]/div[@class="content"]/div[@class="info"]')
    rank = 0
    # "".join(item.xpath('./div[@class="num"]/text()'))
    for item in infolist:
        rank += 1
        videolink = "".join(item.xpath('./a/@href'))
        title = "".join(item.xpath('./a/text()')).replace('"','')
        playinfo = "".join(item.xpath('./div[@class="detail"]/span/text()')).split("万")
        play = playinfo[0] + "万"
        comment = playinfo[1]
        if comment.isdigit() == False:
            comment += "万"
        upname = "".join(item.xpath('./div[@class="detail"]/a/span/text()'))
        uplink = "http:" + "".join(item.xpath('./div[@class="detail"]/a/@href'))
        hot = "".join(item.xpath('./div[@class="pts"]/div/text()'))
        video_list.append({
            'rank': rank,
            'videolink': videolink,
            'title': title,
            'play': play,
            'comment': comment,
            'upname': upname,
            'uplink': uplink,
             'hot': hot
        })
    return video_list

# 将爬取到的数据写入Excel表格
def write_Excel(video_list):
    print("将b站热门视频信息导入到Excel表格：")
    workbook = xlwt.Workbook()  # 定义workbook
    sheet = workbook.add_sheet('b站热门视频')  # 添加sheet
    xstyle = xlwt.XFStyle()  # 实例化表格样式对象
    xstyle.alignment.horz = 0x02  # 字体居中
    xstyle.alignment.vert = 0x01  # 字体居中
    head = ['视频名', 'up主','排名', '热度','播放量','评论数']  # 表头
    for h in range(len(head)):
        sheet.write(0, h, head[h],xstyle)  # 把表头写到Excel里面去
    i = 1
    for item in video_list:
        # 向单元格（视频名）添加（该视频的）超链接
        title_data = 'HYPERLINK("'+item["videolink"]+'";"'+item["title"]+'")'  # 设置超链接
        sheet.col(0).width = int(256 * len(title_data) * 3/5)   # 设置列宽
        sheet.write(i, 0, xlwt.Formula(title_data), xstyle)
        name_data = 'HYPERLINK("' + item["uplink"] + '";"' + item["upname"] + '")'  # 设置超链接
        sheet.col(1).width = int(256 * len(title_data) * 3 / 10)
        sheet.write(i, 1, xlwt.Formula(name_data), xstyle)
        sheet.write(i, 2, item['rank'], xstyle)
        sheet.write(i, 3, item['hot'], xstyle)
        sheet.write(i, 4, item['play'], xstyle)
        sheet.write(i, 5, item['comment'], xstyle)
        i += 1
    # 如果文件存在，则将其删除
    if os.path.exists('D:/Test/b站热门视频信息.xls'):
        os.remove('D:/Test/b站热门视频信息.xls')
    workbook.save('D:/Test/b站热门视频信息.xls')
    print('写入excel成功')
    print("文件位置：D:/Test/b站热门视频信息.xls")

if __name__ == '__main__':
    video_list = []
    write_Excel(spider(video_list))