#!/usr/bin/env python
# coding=utf8

import cgitb
import urllib2
import httplib
import ssl
import re
import sys
from lxml import html

#print sys.argv[1]
bikesearch = sys.argv[1] 

print "Search for: " + bikesearch + "<hr>"


#sslsock=httplib.HTTPSConnection("www.cyklobazar.cz")
#sslsock.request("GET", "/kola?q=mrazek")
#response = sslsock.getresponse()
#htmlSource = response.read()
#print htmlSource


def sOpen(url,search):
 sslsock=httplib.HTTPSConnection(url)
 sslsock.request("GET", "/"+search)
 response = sslsock.getresponse()
 htmlSource = response.read()
 return htmlSource

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

#  htmlISO = htmlSource.decode('ISO-8859-2')
#  htmlUTF = htmlISO.encode('UTF-8')
  
  startBazar = '</form><h2>Nalezené'
  endBazar = '<div data-sticky_column="" class="sidebar">'
  
  dolekopbazar = htmlSource.split(startBazar)[1].split(endBazar)[0]
  
  dolekopSource = re.sub('=\"/','=\"http://dolekop.com/', dolekopbazar)
 
  print "Dolekop.com:<br>"
  print dolekopSource
  print "<hr>"
 except:
  print "Inzerat neexistuje, alebo error na dolekop.com"

def cyklobazar():
# url=("www.cyklobazar.cz/kola?q=" + bikesearch +"")
 url=("www.cyklobazar.cz")
 search=("kola?q="+bikesearch)
 try:
  htmlS = sOpen(url,search)
 
  startBazar = '<div class="page-header">'
#  endBazar = '<div class="col-right">'
  endBazar = '<div class="box-smile box-smile--right">'
 
  cyklobazar = htmlS.split(startBazar)[1].split(endBazar)[0]
  cykloSource = re.sub('=\"/','=\"https://www.cyklobazar.cz/', cyklobazar)
  cykloS = re.sub('url\(','url\(www\\.cyklobazar\\.cz', cykloSource)
  cykloI = re.sub('data-cfsrc','><img src', cykloS)
  cykloV = re.sub('style="display:none;visibility:hidden;"','', cykloI)

  print "Cyklobazar.cz:<br>" 
  print cykloV 
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
  sbazarSource = re.sub('data\-origin=\"/','><img src=\"http:/', sbazarSource)
  
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
