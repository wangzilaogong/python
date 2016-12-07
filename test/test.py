import urllib2
response = urllib2.urlopen('http://www.sqnypt.com')
html = response.read()
print html
