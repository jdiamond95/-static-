# Entropy is the measure of randomness in information
# Compressed/Encypted/Packed data will have close to max entropy
# Text data/code will have lower 
# https://kennethghartman.com/calculate-file-entropy/

import sys
import math

def getFileEntropy(file):

    # Open file as byte array
    with open(file, 'rb') as f:
        byteArr = list(f.read())
        f.close()
    fileLength = len(byteArr)

    # Count frequencies of bytes
    byteFreq = []
    for i in range(0, 256):
        byteFreq.append(float(byteArr.count(i)/fileLength))

    # Calculate Shannon Entropy
    # H(x) = - sumof(i=1, n) pi * log(pi, 2)
    entropy = 0.0
    for freq in byteFreq:
        if freq != 0:
            entropy = entropy + freq * math.log(freq, 2)
    entropy = - entropy
    return entropy, byteFreq

def printEntropyCLI(file):
    shannonEntropy, byteFreq = getFileEntropy(file)
    print("Shannon Entropy: " + str(shannonEntropy))
