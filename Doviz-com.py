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


