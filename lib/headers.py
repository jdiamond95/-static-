fileSignatures = [["2321" , "Script or data to be passed to the program following the shebang (#!)."], 
["edabeedb", "RedHat Package Manager (RPM) package [3]"],
["4D5A", "DOS MZ executable file format and its descendants (including NE and PE)"]]

def magicBytes(file):
    with open(file, errors='replace') as f:
        hexdata = bytes(f.read(32), 'utf-8').hex()
        for i in range(0, len(fileSignatures)):
            if fileSignatures[i][0].lower() == hexdata[0:len(fileSignatures[i][0])].lower():
                print(fileSignatures[i][1])
                break

