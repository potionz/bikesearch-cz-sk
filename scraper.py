# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

import cgitb
import urllib2
import re
import sys
from lxml import html

#print sys.argv[1]
bikesearch = sys.argv[1] 

print "Search for: " + bikesearch + "<hr>"

def cOpen(url):
 sock=urllib2.urlopen(url)
 htmlSource = sock.read()
 sock.close() 
 return htmlSource

def dolekop():
 url=("http://dolekop.com/bazar?typ=1&kategorie=&lokalita=0&prumer=0&velikost=0&rok=0&cenaod=&cenado=&stari=&slovo=" + bikesearch + "&razeni=datumsestupne")
 try: 
  sock=urllib2.urlopen(url)
  sock.headers.getparam('charset') 
  htmlSource = sock.read()
  sock.close() 

  htmlISO = htmlSource.decode('ISO-8859-2')
  htmlUTF = htmlISO.encode('UTF-8')
  
  startBazar = '<h2>Bazar</h2>'
  endBazar = '<br class="cistic"'
  
  dolekopbazar = htmlUTF.split(startBazar)[1].split(endBazar)[0]
  
  dolekopSource = re.sub('=\"/','=\"http://dolekop.com/', dolekopbazar)
 
  print "Dolekop.com:<br>"
  print dolekopSource
  print "<hr>"
 except:
  print "Inzerat neexistuje, alebo error na dolekop.com"


dolekop()


