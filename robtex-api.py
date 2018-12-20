#Just a first upload on github for test
import requests

f = open("IPtoBan.csv","w")
f.write("IP;COUNTRY;CITY;ROUTE\n")
for ip in open("IP_list.txt"):
    ip = ip.replace("\n" ,"")
    r = requests.get("https://freeapi.robtex.com/ipquery/"+ip.replace("\n",""))
    if r.status_code == 200:
        country = r.json()['country'] if 'country' in r.json() else "N/A"
        city = r.json()['city'] if 'city' in r.json() else "N/A"
        route = r.json()['bgproute'] if 'bgproute' in r.json() else "N/A"
        f.write(ip + ";" + country + ";" + city + ";" + route + "\n")
f.close()