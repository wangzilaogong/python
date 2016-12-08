import requests
from bs4 import BeautifulSoup
res = requests.get("http://www.tjconstruct.cn/index.aspx")
res.encoding="utf-8"
html = res.text
soup = BeautifulSoup(html, "html.parser")
table = soup.find(id='Tp1')
tds = [td.text for td in  table.find_all('td')]
print(tds)




