import os
import time

def getFileSize(file):
	return os.path.getsize(file)


def getFileExtension(file):
	filename, fileExtension = os.path.splitext(file)
	return fileExtension


def getFileModificationDateTime(file):
	return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(file)))
	

def getFileCreationDateTime(file):
	return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getctime(file)))