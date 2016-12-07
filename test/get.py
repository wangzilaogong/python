import urllib
import urllib2
values={}
values['username']="wukai"
values['password']="1234"
data = urllib.urlencode(values)
url="http://www.sqnypt.com/Login.aspx"
geturl=url+"?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
print geturl