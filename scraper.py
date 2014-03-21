from bs4 import BeautifulSoup
import requests

b=requests.get("http://thebeerstore.ca/beers/sale")
beer=b.text
bsoup=BeautifulSoup(beer)
deal=[]
f=open("sales.txt",'w')
for i in bsoup.find_all('a'):
    s=i.text
    if not(s.strip()==""):
        used = False
        for q in s:
            if q == '$' and used==False:
                used = True
                #print s.strip()
                deal.append(s.strip())
                exit
print "Done"
print deal
f.write(str(deal))
f.close()
