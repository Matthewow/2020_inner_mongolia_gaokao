import requests
from bs4 import BeautifulSoup
import json
import timeit

start = timeit.default_timer()

def extract(page_number):
    articlepage = 'https://www.hk01.com/anything/' + str(page_number)
    r = requests.get(articlepage)
    soup = BeautifulSoup(r.text, features="lxml")
    found = False

    for pagejson in soup.find_all('script', {'type': "application/ld+json"}):
        found = True
        raw1 = str(pagejson).replace('<script type="application/ld+json">',"")
        raw2 = raw1.replace('</script>',"")
        page_dict = json.loads(raw2)
        tags = str(page_dict["keywords"])
        tag1 = tags.replace("'香港01'", "")
        tag2 = tag1.replace("'hk01'","")
        tag3 = tag2.replace(",","")
        tag4 = tag3.replace(" ","")
        f = open("index.txt", "a")
        f.write("{}: {}\n".format(str(page_number),tag4))
        f.close()

    if found:
        filename = "./Data/" + str(page_number) + ".txt"
        f = open(filename, "a")
        for para in soup.find_all('p', {'class': 'sc-5vyyvj-0 jgHuKE sc-1v3m5dk-0 dKOvNf'}):
            f.write("{}\n".format(str(para.text)))
        f.close()
        print(f"{page_number} Processing..." )
    else:
        print(f"{page_number} Not Found" )

for i in range (580000, 590000):
    extract(i)

stop = timeit.default_timer()
print('Time: ', stop - start)  


