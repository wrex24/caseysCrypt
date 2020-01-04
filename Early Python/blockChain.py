import datetime as date
import math
import hashlib
import rsaFunctions

def getInfo(block):
    information = []
    sender = input('Sender: ')
    receiver = input('Receiver: ')
    amount = input('Amount: ')
    newKey = block[-1]
    rawInformation = [sender,receiver,amount,newKey]
    keyFile = ("%s_publicKey.txt" %sender)
    for rawData in rawInformation:
        data = rsaFunctions.encrypt(rawData, keyFile)
        print(data)
        byteData = data.encode('utf-8')
        information.append(byteData)
    

        
    #information = [sender.encode('utf-8'),receiver.encode('utf-8'),amount.encode('utf-8'), newKey.encode('utf-8')]
    return(information)

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

def readFile():
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

def main():
    block = readFile()
    while(True):
        print(block)
        information = getInfo(block)
        newBlock = pow(information)
        block.append(newBlock)
        writeFile(newBlock)
        again = input('Again y/n?: ')
        if(again == 'n'):
            break
        
if(__name__ == "__main__"):
    main()

