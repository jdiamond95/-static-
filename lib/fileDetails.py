import os
import time
import string
import hashlib

fileBlockSize = 65536

def getFileSize(file):
	return os.path.getsize(file)


def getFileExtension(file):
	filename, fileExtension = os.path.splitext(file)
	return fileExtension


def getFileModificationDateTime(file):
	return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(file)))
	

def getFileCreationDateTime(file):
	return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getctime(file)))


def getFileHash(file, hash):
	if hash == "MD5":
		newHash = hashlib.md5()
	elif hash == "SHA256":
		newHash = hashlib.sha256()
	else:
		newHash = hashlib.sha1()
	with open(file, 'rb') as f:
		fileBlock = f.read(fileBlockSize)
		while len(fileBlock) > 0:
			newHash.update(fileBlock)
			fileBlock = f.read(fileBlockSize)
	return newHash.hexdigest()


def getStrings(file, n):
    with open(file, errors='replace') as f:
        results = []
        currResult = ''
        for c in f.read():
            if c in string.printable:
                currResult += c
                continue
            if len(currResult) >= n:
                results.append(currResult)
            currResult = ''
        if len(currResult) >= n:
            results.append(currResult)  
    return results