#!/usr/bin/env python3

'''
Dibuat Pada : 13-oct-20
Jam         : 16:33:50
Author      : Diki Hermawan
#Note       : Making with emosion :v
Update      : 08-oct-2021
'''

import requests as r, sys, os
from time import sleep as s
from bs4 import BeautifulSoup as bs

c = r.Session ()

CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

#Fungsi
def Loker_Serang ():
  url = "https://serangid.id"
  soup = bs (c.get(url).text, "html.parser")
  angka = 0
  for loker in soup.find_all ('h3', class_='uagb-post__title'):
    angka += 1
    print (str(angka)+f"{loker.text}")

def Loker_Kab ():
  url = "https://serangkab.info"
  req = c.get(url)
  soup = bs (req.text, "html.parser")
  angka = 0
  for list in soup.find_all("h2",class_="entry-title"):
    angka += 1
    print (str([angka])+'\n'+f"{list.text}\n")

def Link_Kab (x):
  url = "https://serangkab.info"
  soup = bs (c.get(url).text, "html.parser")
  angka = 0
  for loker in soup.find_all ('h2', class_='entry-title'):
    angka += 1
    if angka == x:
      for link in loker.findChildren('a'):
        global cari
        cari = link.get ('href')
        os.system("xdg-open "+cari)

def Isi_Kab (x):
  url = "https://serangkab.info"
  soup = bs (c.get(url).text, "html.parser")
  angka = 0
  for loker in soup.find_all ('h2', class_='entry-title'):
    angka += 1
    if angka == x:
      for link in loker.findChildren('a'):
        global cari
        cari = link.get ('href')
        saup = bs(c.get(cari).text, "html.parser")
        for art in saup.find_all("div", class_="entry-content"):
          for arti in art.findChildren ({("p"),("ul"),("li")}):
                print (arti.text)

def Link_Serang(x):
  url = "https://serangid.id"
  soup = bs (c.get(url).text, "html.parser")
  angka = 0
  for loker in soup.find_all ('h3', class_='uagb-post__title'):
    angka += 1
    if angka == x:
      for link in loker.findChildren('a', rel="bookmark noopener noreferrer"):
        global cari
        cari = link.get ('href')
        os.system("xdg-open"+cari)
        
def main ():
  s(1)
  print (CEND+"\nDaftar Web Loker:\n[1] SerangKab.info\n[2] SerangId\n")
  s (1)
  pilihan = int(input(CBLUE+"Masukan "+CRED+"Pilihan : "))
  s(1)
  os.system ("clear")
  if pilihan == 1:
    Loker_Kab()
    if Loker_Kab() == pilihan:
      Isi_Kab()
  elif pilihan == 2:
    Loker_Serang(Link_Serang(pilihan))
  #Isi_Kab (int (pilihan))
  #Link_Kab (int(pilihan))
  #Loker_Kab()
  #Loker_Serang()
    

main()
