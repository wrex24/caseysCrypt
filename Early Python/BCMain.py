import datetime as date
import math
import hashlib
import BCSender


def pow(information):
    nonce = '0'
    while(True):
        #hashes info every time the same way
        keyPart = hashlib.sha256()
        for i in information:
            keyPart.update(i)
        #hash it with the nonce
        keyPart.update(nonce.encode('utf-8'))
        #digest it
        key = keyPart.hexdigest()
        #if it meets requirement
        if(key[0:4] == '0000'):
            print('key: ' + key)
            print('nonce: ' + nonce)
            break
        #else repeat with new nonce
        else:
            nonce = int(nonce)
            nonce += 1
            nonce = str(nonce)
        
    
    return(key)

def readBlock():
    file = open("blockChain.txt","r")
    blockText = file.readlines()
    file.close()
    block = []
    for i in blockText:
        newLine = i[:-1]
        block.append(newLine)
    return(block)

def writeFile(newBlock):
    file = open("blockChain.txt","a")
    file.write("\n%s" %newBlock)
    file.close()

def readInfo(block):
    file = open("senderInfo.txt","r")
    lines = file.readlines()
    file.close()
    rawInformation = []
    information = []
    for i in lines:
        newLine = i[:-1]
        if(newLine != ''):
            rawInformation.append(newLine)
    rawInformation.append(block[-1])
    for i in rawInformation:
        data = i.encode('utf-8')
        information.append(data)

    return(information)

def sendInfo():
    file = open("senderInfo.txt","a")
    file.write("\nv")
    file.close

def main():
    block = readBlock()

    while(True):
        #print(block)
        information = readInfo(block)
        newBlock = pow(information)
        block.append(newBlock)
        writeFile(newBlock)
        sendInfo()
        
if(__name__ == "__main__"):
    main()
