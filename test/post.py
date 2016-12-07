import urllib
import urllib2

values = {"username":"wukai","password":"1234"}
data = urllib.urlencode(values)
url = "http://www.sqnypt.com/Login.aspx"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()