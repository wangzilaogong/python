import requests
from bs4 import BeautifulSoup
import os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
all_url = 'http://www.mzitu.com/all'
start_html =requests.get(all_url,headers=headers)
Soup = BeautifulSoup(start_html.text,'lxml')
all_a = Soup.find('div',class_='all').find_all('a')
for a in all_a:
    title = a.get_text()
    href  = a['href']
    path = str(title).strip()
    os.makedirs(os.path.join("D:\mzitu",path))
    os.chdir("D:\mzitu\\"+path) ##切换到上面创建的文件夹
    html = requests.get(href,headers = headers)
    html_Soup = BeautifulSoup(html.text,'lxml')
    max_span = html_Soup.find('div',class_='pagenavi').find_all('span')[-2].get_text()
    for page in range(1,int(max_span)+1):
        page_url =  href + '/'+ str(page)
        img_html = requests.get(page_url,headers=headers)
        img_Soup = BeautifulSoup(img_html.text,'lxml')
        img_url = img_Soup.find('div',class_="main-image").find('img')['src']
        print(img_url)
        name = img_url[-9:-4] ##取URL 倒数第四至第九位 做图片的名字
        img = requests.get(img_url, headers=headers)
        f = open(name+'.jpg', 'ab')
        f.write(img.content) ##多媒体文件要是用conctent哦！
        f.close()


