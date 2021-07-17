"""
Ini adalah script untuk view cctv melalui ip

Coded By KZ

Ini adalah script sederhana
"""

import os
import re
import time
from requests import *
from bs4 import BeautifulSoup as bs

url = []
px = []

g = "\033[1;32m"
w = "\033[1;97m"
r = "\033[1;91m"

country = ['US', 'JP', 'IT', 'KR', 'FR', 'DE', 'TW', 'RU', 'GB', 'NL', 'CZ', 'TR', 'AT', 'CH', 'ES', 'CA', 'SE', 'IL', 'PL', 'IR', 'NO', 'RO', 'IN', 'VN', 'BE', 'BR', 'BG', 'ID', 'DK', 'AR', 'MX', 'FI', 'CN', 'CL', 'ZA', 'SK', 'HU', 'IE', 'EG', 'TH', 'UA', 'RS', 'HK', 'GR', 'PT', 'LV', 'SG', 'IS', 'MY', 'CO', 'TN', 'EE', 'DO', 'SI', 'EC', 'LT', 'PS', 'NZ', 'BD', 'PA', 'MD', 'NI', 'MT', 'IT', 'SA', 'HR', 'CY', 'PK', 'AE', 'KZ', 'KW', 'VE', 'GE', 'ME', 'SV', 'LU', 'CW', 'PR', 'CR', 'BY', 'AL', 'LI', 'BA', 'PY', 'PH', 'FO', 'GT', 'NP', 'PE', 'UY']


def main(code):
  kz = bs(get("http://www.insecam.org/en/bycountry/"+code,headers={"user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36"}).text, 'html.parser').find('ul',{'class':'pagination'}).find('script')
  page = re.search(", (\d+)",str(kz)).group(1)
  halaman = input(f"\n{g} •{w} Total Page ({g}{page}{w}) > ")
  print("")
  echa = get("http://www.insecam.org/en/bycountry/"+code+"?page="+halaman,headers={"user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36"}).text
  rev = bs(echa,'html.parser').findAll('div',{'class':'row thumbnail-items'})
  for rainz in rev:
    cr = re.findall("https?://\d+.\d+.\d+.\d+:\d+",str(rainz))
    url.append(cr)
    for dark in cr:
      print(f" {g}• {w}{dark}")


while True:
  os.system("clear")
  print(f"{w}[{g}1{w}]. List Code Country\n[{g}2{w}]. Get IP Address")
  select = input(f"\n{g} • {w}Option > ")
  print("")
  if select == "1" or select == "01":
    px.append(country)
    for j in country:
      print(f"{g}• {w}{j}")
    home = input(f"\n{w}[{g}?{w}] Kembali ke Halaman Utama y/n? ")
    if home == "y" or home == "Y":
      continue
    
    elif home == "n" or home == "N":
      break
    
    else:
      print(f"\n{w}[{r}!{w}] Wrong Input! ")
      continue
    
  elif select == "2" or select == "02":
    code = input(f"{w}[{g}•{w}] Enter Code Country : ")
    main(code)
    print(f"\n {w}[{r}!{w}] Pastekan Salah satu IP di browser ")
    back = input(f"\n\n{w}[{g}?{w}] Mau lanjut lagi y/n? ")
    if back == "y" or back == "Y":
      continue
    
    elif back == "n" or back == "N":
      break
    
  else:
    print(f"{w}[{r}!{w}] Wrong Input! ")
    time.sleep(2.5)
    continue
