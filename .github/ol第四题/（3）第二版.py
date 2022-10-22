import re

with open('./sanji_list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1010') as f:
    data = f.read()
re.findall('<div style="float:left"><a href="content.jsp?urltype=news.NewsContentUrl&wbtreeid=1266&wbnewsid=34994" target=_blank title="关于举行第八届山东省大学生单片机应用创新设计大赛的通知" style="">关于举行第八届山东省大学生单片机应用创新设计大赛的通知</a></div>
<div style="float:right;">(.*?)</div>')