from bs4 import BeautifulSoup
import requests

url = "https://kur.doviz.com"

response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

deneme = soup.find_all("td",{"class":"column-row5"})
doviz = []
for j in deneme:
    
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
