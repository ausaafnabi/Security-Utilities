import requests
import json

print("#" * 27)
print("="*5 ," jSON API Viewer ","="*5)
print("#" * 27)
print("enter the URL endpoint for json file\n")
requestedURL = input("URL: ")
try:
    r=requests.get(requestedURL)
    res = r.json()
    print(json.dumps(res,indent=4))
except:
    print("404: Error Extracting the API")
