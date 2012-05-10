#simply get a page and load time
import urllib2
import time
total = 0
start = time.time()
req = urllib2.Request('http://www.tumblr.com')
response = urllib2.urlopen(req)
the_page = response.read()
info = response.info()
clen = len(the_page)
print(clen)
print(info)   
print('time: %f' % (time.time() - start))
print("\n")
