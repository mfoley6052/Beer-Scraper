from bs4 import BeautifulSoup
import requests

a=requests.get("http://www.thebeerstore.ca/beers/search/")
b=requests.get("http://thebeerstore.ca/beers/sale")
allbeer=a.text
allsoup = BeautifulSoup(allbeer)
beer=b.text
bsoup=BeautifulSoup(beer)
deal=[]
regulars=[]
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
f.write(str(deal))
f.close()
g=open("regulars.txt",'w')
for i in allsoup.find_all('a'):
    s=i.text
    if not(s.strip()==""):
        used = False
        for q in s:
            if q == '%' and used==False:
                used = True
                print s.strip()
                regulars.append(s.strip())
                exit
print "Done"
g.write(str(regulars))
g.close()
