import requests
import re
from bs4 import BeautifulSoup
res = requests.get("http://www.tjconstruct.cn/index.aspx")
res.encoding="utf-8"
html = res.text
soup = BeautifulSoup(html, "html.parser")
FIELDS=('title','address','date')
results = {}
for filed in FIELDS:
    results[filed]= soup.findAll('tr',{})



