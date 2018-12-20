#pip install requests
#pipenv install requests
import sys, re
import requests

URL = "https://freeapi.robtex.com/ipquery/"
IpRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";

if len(sys.argv) == 2:
    f = open("robtex-api-result.csv", "w")
    f.write("IP;Country;City;Description;Route\n")
    print("IP ; Country ; City ; Description;Route")
    for ip in open(sys.argv[1]):
        ip = ip.replace("\n" ,"")
        if re.match(IpRegex, ip):
            r = requests.get(URL + ip)
            if r.status_code == 200:
                country = r.json()['country'] if 'country' in r.json() else "N/A"
                city = r.json()['city'] if 'city' in r.json() else "N/A"
                descr = r.json()['whoisdesc'] if 'whoisdesc' in r.json() else "N/A"
                route = r.json()['bgproute'] if 'bgproute' in r.json() else "N/A"
                moreInfo = "https://www.robtex.com/ip-lookup/" + ip + "#records"
                f.write(ip + ";" + country + ";" + city + ";" + descr + ";" + route + ";" + moreInfo + "\n")
                print(ip, ";", country, ";", city, " ; ", descr, ";", route, ";", moreInfo)
        else:
            f.write("Invalid IP format:" + ip + "\n")
            print("Invalid IP format:", ip)
    f.close()
else:
    print("Usage: robtex-api.py \"IP_file.txt\"")
    print("Provide only one file as argument")
    print("Each line in the file must be a valid IPv4")