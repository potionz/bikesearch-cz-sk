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
#bikesearch = sys.argv[1] 
bikesearch = 'mongoose'

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

def cyklobazar():
 url="http://www.cyklobazar.cz/kola?q=" + bikesearch
 try:
  htmlS = cOpen(url)
 
  startBazar = '<div class="page-header">'
  endBazar = '<div class="col-right">'
 
  cyklobazar = htmlS.split(startBazar)[1].split(endBazar)[0]
  cykloSource = re.sub('=\"/','=\"http://cyklobazar.cz/', cyklobazar)
 
  print "Cyklobazar.cz:<br>" 
  print cykloSource 
  print "<hr>"
 except:
  print "Inzerat neexistuje, alebo error na cyklobazar.cz"


def bazoscz():
 url=("http://sport.bazos.cz/horska/?hledat=" + bikesearch + "&rubriky=sport&hlokalita=&humkreis=25&cenaod=&cenado=&Submit=Hledat&kitx=ano")
 try: 
  htmlS = cOpen(url)
  
  startBazar = 'class="listainzerat"'
  endBazar = '<div align="left">&copy;'
 
  bazoscz = htmlS.split(startBazar)[1].split(endBazar)[0]
  bazosSource = re.sub('=\"/','=\"http://sport.bazos.cz/', bazoscz)
  
  print "bazos.cz:<br>"
  print bazosSource
  print "<hr>"
 except:
  print "Inzerat neexistuje, alebo error na bazos.cz"


def bazossk():
 url=("http://sport.bazos.sk/horska/?hledat=" + bikesearch + "&rubriky=sport&hlokalita=&humkreis=25&cenaod=&cenado=&Submit=H%C4%BEada%C5%A5&kitx=ano")
 try:
  htmlS = cOpen(url)
  
  startBazar = 'class="listainzerat"'
  endBazar = '<div align="left">&copy;'
 
  bazossk = htmlS.split(startBazar)[1].split(endBazar)[0]
  bazosskSource = re.sub('=\"/','=\"http://sport.bazos.sk/', bazossk)
 
  print "bazos.sk:<br>"
  print bazosskSource
  print "<hr>"
 except:
  print "Inzerat neexistuje, alebo error na bazos.sk"


def mtbiker():
 url=("http://www.mtbiker.sk/bazar?kat=all&okres=&typ_predaj=1&typ_kupa=1&order=time&s=" + bikesearch + "&f_category_id=&cena_od=&cena_do=&user_id=0") 
 try: 
  htmlS = cOpen(url)
  
 # startBazar = '<div class=\'bazar_row\'>'
  startBazar = '<button class="btn" data-dismiss="modal" aria-hidden="true">OK</button>'
#  endBazar = '<footer>'
  endBazar = '&copy'
 
  mtbiker = htmlS.split(startBazar)[1].split(endBazar)[0]
  mtbikerSource = re.sub('=\"/','=\"http://mtbiker.sk/', mtbiker)
  mtbikerSource = re.sub('=\'/','=\'http://mtbiker.sk/', mtbikerSource)
 
  print "mtbiker.sk:<br>"
  print mtbikerSource
  print "<hr>"
 
 except:
  print "Inzerat neexistuje, alebo error na mtbiker"


def sbazar():
 url=("http://www.sbazar.cz/hledej/" + bikesearch + "/628-kola")
 try: 
  htmlS = cOpen(url)
  
  startBazar = '<div id="mrEggsResults">'
  endBazar = '<div id="skyStopper">'
  
  sbazar = htmlS.split(startBazar)[1].split(endBazar)[0]
  sbazarSource = re.sub('href=\"/','href=\"http://www.sbazar.cz/', sbazar)
  sbazarSource = re.sub('img=\"/','img=\"http://', sbazarSource)
  
  print "sbazar.cz:<br>"
  print sbazarSource
  print "<hr>"

 except:
  print "Inzerat neexistuje, alebo error na sbazar<hr>"
 
def kolobazar():
 url=("http://www.kolobazar.cz/filtr-inzeratu.html?text=" + bikesearch + "&kategorie=&kraj=cela-cr&cena_od=&cena_do=")
 try: 
  htmlS = cOpen(url)
  
  startBazar = '<script type="text/javascript" src="/funkce/otevri_inzerat.js"></script>'
  endBazar = '<div class="strana">'

  kolobazar = htmlS.split(startBazar)[1].split(endBazar)[0]
  kolobazarSource = re.sub('=\"/','=\"http://www.kolobazar.cz/', kolobazar)
  kolobazarSource = re.sub('zobrazit celý text inzerátu a konta', '<br><br>------------------------------------------------<br><br>', kolobazarSource)

  print "kolobazar.cz:"
  print kolobazarSource
  print "<hr>"
 
 except:
  print "Inzerat neexistuje, alebo error on kolobazar<hr>"

def aukrocz():
 #url=("http://aukro.cz/listing/listing.php?string=" + bikesearch + "&search_scope=v%C5%A1echny+kategorie&buyUsed=1")
 url=("http://aukro.cz/listing/listing.php?string=" + bikesearch + "&search_scope=category-17570&buyUsed=1")
 
 try:
  htmlS = cOpen(url)
  
  startBazar = '<h2 class="listing-header">seznam nabídek</h2>'
  endBazar = '<div class="pager pager-bottom">'
 
  aukrocz = htmlS.split(startBazar)[1].split(endBazar)[0]
  aukroczSource = re.sub('=\"/','=\"http://aukro.cz/', aukrocz)
  aukroczSource = re.sub('<div class=\"photo\" data\-img=\'\[\[\"', '<img src="', aukroczSource)
  aukroczSource = re.sub('\"]]\'', '">', aukroczSource)
 
  print "aukro.cz:"
  print aukroczSource
  print "<hr>"
 except:
  print "Inzerat neexistuje, alebo error na aukro.cz <hr>"
 

dolekop()
cyklobazar()
bazoscz()
bazossk()
mtbiker()
sbazar()
aukrocz()
kolobazar()



