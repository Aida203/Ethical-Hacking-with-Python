import requests
import json
import socket

domainName = input('Enter Domain Name > ')
#req = requests.get("https://"+ domainName)  


#print(req.status_code)


#print(req)  => prints <Response [200]> for the google.com domainName

#print(req.content)  =>prints a bunch of info

#print(req.headers)



ipAddress = socket.gethostbyname(domainName)
#print(f"Id Address of this domain is {ipAddress}")
# https://ipinfo.io/json

req = requests.get("https://ipinfo.io/"+ipAddress+"/json")
result = json.loads(req.text)
print(result)

#print(req)