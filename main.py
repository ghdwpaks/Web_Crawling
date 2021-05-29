from re import sub
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://blog.naver.com/PostView.nhn?blogId=cdh0584&logNo=222361383092"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

#print(soup)
i = 0
t1 = []
while True :
    try :    
        print(soup.select(".se-ff-")[i].get_text())
        t1.append(soup.select(".se-ff-")[i].get_text())
        i += 1
    except IndexError :
        break
#lens1 = len(res1)

#print(res)
