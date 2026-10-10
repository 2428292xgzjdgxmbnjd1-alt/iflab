import cloudscraper
from curl_cffi import requests
my_proxies = {
    "http":"http://127.0.0.1:7897",
    "https":"http://127.0.0.1:7897",
}
com_url='https://greasyfork.org/zh-CN/scripts/398151-%E8%B6%85%E6%98%9F-%E5%AD%A6%E4%B9%A0%E9%80%9A%E8%87%AA%E5%8A%A8%E6%8A%A2%E7%AD%94/feedback'


com = requests.get(
        com_url, 
        proxies=my_proxies, 
        impersonate="edge",
        timeout=20
    )
from bs4 import BeautifulSoup
soup=BeautifulSoup(com.text, 'html.parser')
comments = soup.find_all("div", class_="discussion-list-container")
data=[]
for comment in comments:
    user=comment.find("a", class_="user-link").text.strip()
    content=comment.find("span", class_="discussion-snippet").text.strip()
    time=comment.find("relative-time").text.strip()
    c={
        '用户名':user,
        '评论内容':content,
        '评论时间':time
    }
    data.append(c)
import csv
with  open('所有评论.csv', 'w', encoding='utf-8-sig') as f:
    f_csv = csv.DictWriter(f, fieldnames=['用户名', '评论内容', '评论时间'])
    f_csv.writeheader()
    f_csv.writerows(data)



