import requests
import os
from lib.fileDetails import getFileHash, getFileExtension
from colorama import Fore, Back, Style


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


def printVTCLI(file):
    fileHash = getFileHash(file, "SHA256")
    vtOutput = queryVirusTotal(fileHash)

    if vtOutput['response_code'] == 1:
        detectionPercentage = vtOutput['positives']/vtOutput['total']

    fileName, fileExtension = getFileExtension(file)

    if vtOutput['response_code'] == 0:
        print(Back.WHITE + Fore.BLACK)
        print(fileName + fileExtension + Style.RESET_ALL)
        print("Resource: " + vtOutput['resource'])
        print("No VirusTotal results found")
        return

    if detectionPercentage == 0:
        print(Back.GREEN)
    elif detectionPercentage < 0.1:
        print('\033[43m')
    else:
        print(Back.RED)
    print(fileName + fileExtension + " - " + str(vtOutput['positives']) + "/" + str(vtOutput['total']) + Style.RESET_ALL)
    print("VirusTotal Link: " + vtOutput['permalink'])
