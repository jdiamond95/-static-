import requests
import os

vtAPIKey = os.environ.get('VTAPIKey')
virusTotalBase = "https://www.virustotal.com/vtapi/v2/"
vtFileReport = "file/report"
session = requests.Session()

def queryVirusTotal(hash):
    params = {
            'apikey':vtAPIKey,
            'resource':hash
    }
    url = virusTotalBase + vtFileReport

    try:
        r = session.get(virusTotalBase + vtFileReport, params=params)
        return r.json()        

    except requests.exceptions.RequestException as e:
        return 0       

def printVTCLI(hash):
    data = queryVirusTotal(hash)
    print(data)
