import urllib
import urllib2
url = "http://my.csdn.net/my/mycsdn"
user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
headers = {'User-Agent': user_agent}
values = { 'username':'997972547@qq.com','password':'wk123456'}
data = urllib.urlencode(values)
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
page = response.read()
print page
