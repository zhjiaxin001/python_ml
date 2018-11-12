import urllib2
import cookielib

cookie =  cookielib.CookieJar

cookie_handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(cookie_handler)

opener.add_handler()
