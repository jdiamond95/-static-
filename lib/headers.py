from lib.helper import fileSignatures

def magicBytes(file):
    with open(file, errors='replace') as f:
        hexdata = bytes(f.read(32), 'utf-8').hex()
        for i in range(0, len(fileSignatures)):
            if fileSignatures[i][1].lower() == hexdata[0:len(fileSignatures[i][1])].lower():
                print(fileSignatures[i][0])
                break

