#pip install requests
#pipenv install requests
import sys, re
import requests

URL = "https://freeapi.robtex.com/ipquery/"
IpRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";

def write(file, txt):
    f.write(txt + "\n")
    print(txt.replace(";"," ; "))

if len(sys.argv) == 2:
    f = open("robtex-api-result.csv", "w")
    write(f, "IP;Country;City;Description;Route")
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
                write(f, ip + ";" + country + ";" + city + ";" + descr + ";" + route + ";" + moreInfo)
            else:
                write(f, "HTTP error code: " + str(r.status_code) + " while checking for ip: " + ip)
        else:
            write(f, "Invalid IP format: " + ip)
    f.close()
else:
    print("Usage: robtex-api.py \"IP_file.txt\"")
    print("Provide only one file as argument")
    print("Each line in the file must be a valid IPv4")