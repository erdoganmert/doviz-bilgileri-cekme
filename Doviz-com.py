from bs4 import BeautifulSoup
import requests
from decimal import Decimal


url = "https://kur.doviz.com"

# Verileri getirme
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

degerler = soup.find_all("table",{"id":"currencies"})
satir = []
for j in degerler:
    j = j.text
    j = j.split()
    satir.append(j)

satir = str(satir[0][4::])
satir = satir.split(" ")



# Döviz ve paraları çekme

doviz = ['USD']
para = []

for i in satir:
    if(len(i)==6):
        doviz.append(i[0:4])
    i = i.strip("'")
    i = i.strip(",")
    i = i[:-1]
    
    try:
        i = i.replace(",",".")
        para.append(float(i))
    except:
        pass


for i in range(len(doviz)):
    if(doviz[i][0] == "'"):
        doviz[i] = doviz[i][1:]

for i in doviz:
    if(len(i) > 3 ):
        i = i[1:]
    if(not i.isupper() and not i.islower()):
        doviz.remove(i)
        
for i in para:
    i = Decimal("%.4f"%float(i))
    if(i == 100):
        para.remove(i)


# Saatleri çekme

saat = []

for i in satir:
    i = i.strip("',")
    try:
        i = i.replace(":",".")
        saat.append(float(i))
    except:
        pass
saat.append(float(satir[-1].strip("' ]").replace(":",".")))

for i in saat:
    i = Decimal("%.2f"%float(i))
    if(len(str(i)) > 5):
        saat.remove(i)


# Alış satış fiyatları

alis  = para[::2]
satis = para[1::2]

# Birleştirme

birlestir = list(zip(doviz,alis,satis,saat))

# Ekrana yazma
print ("Döviz"+"\t\t"+"Alış"+"\t    "+"Satış"+"\t"+"Saat")
print("----------------------------------------------------")
for doviz,alis,satis,saat in birlestir:
  print("{}\t        {:.4f}      {:.4f}      {:.2f}".format(doviz,alis,satis,saat))




"""
doviz_sutunu = soup.find_all("td",{"class":"column-row5"})
doviz = []
for j in doviz_sutunu:
    
    j = j.text
    j=j.strip("\n")
    j = j.split()
    doviz.append(j)
doviz = doviz[1::]
yeniDoviz = str([])
i = 0
while i < (len(doviz)-1):
    if (i == 1 ):
      yeniDoviz += (doviz[i][2])+","
    elif (i ==11 or i ==13 or i ==16   or i ==23 or i ==39 or i==43 or i ==46 or i ==60  ):
        yeniDoviz += doviz[i][4]+","
    else:
      yeniDoviz +=doviz[i][3] + ","
    i +=1
    

yeniDoviz = yeniDoviz[:-1]
yeniDoviz = yeniDoviz.split(",")

yeniDoviz[0] = yeniDoviz[0].strip("[]")


alisSatisFark = []
saatler = []    
alis_satis_fark = soup.find_all("td",{"class":"column-row4"})
saat = soup.find_all("td",{"class":"column-row2"})
for i in alis_satis_fark:
    i = i.text
    i = i.strip("\n")
    i = i.split()
    alisSatisFark.append(i)
    
alisSatisFark = alisSatisFark[3::]

for i in saat:
    i = i.text
    i = i.strip("\n")
    i = i.split()
    saatler.append(i)

saatler = saatler[3::2]
yeniAlisSatisFark = []
for i in alisSatisFark:
    yeniAlisSatisFark.append(i)

alis = yeniAlisSatisFark[0::3]
satis = yeniAlisSatisFark[1::3]

birlestir = list(zip(yeniDoviz,alis,satis,saatler))

print ("Döviz"+"\t\t"+"Alış"+"\t\t\t"+"Satış"+"\t\t\t"+"Saat")
print("----------------------------------------------------")
for doviz,alis,satis,saat in birlestir:
  print("{}\t      {}      {}      {}".format(doviz,alis,satis,saat))
"""
