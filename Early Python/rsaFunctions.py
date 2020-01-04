import math, sys
symbols = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.!?"'


def encrypt(rawMessage, keyFile):
    message = filterText(rawMessage)
    information = encryptWriteFile(keyFile, message)
    return(information)




def filterText(rawMessage):
    message = ''
    for i in rawMessage:
        if symbols.find(i) != -1:
            message += i
    return message

def encryptWriteFile(fileName, message):
    keySize, n, e = readFile(fileName)
    encryptedBlocks = encode(e,n, message)
    for i in range(0, len(encryptedBlocks)):
        encryptedBlocks[i] = str(encryptedBlocks[i])
    encryptedMessage = ','.join(encryptedBlocks)

    return encryptedMessage

def encode(e,n, message):
    encryptedBlocks = []
    blocks = createBlocks(message)
    for i in range(0,len(blocks)):
        encryptedBlocks.append(pow(blocks[i], e, n))
    #print(encryptedBlocks)
    return encryptedBlocks

def readFile(fileName):
    '''read file and get information'''
    file = open(fileName)
    information = file.read()
    file.close()
    information = information.split(',')
    keySize, n , key = information
    return (int(keySize), int(n), int(key))

def createBlocks(message):
    """creates blocks from message"""
    blockSize = 0
    while (2**1024)> (len(symbols)**(blockSize+1)):
        blockSize += 1
    blockInteger = 0 #number represented by characters
    blocks = [] #list of blockIntegers
    blockPosition = 0
    blockNumber = 0

    for i in range(0,len(message)):
        blockInteger += (symbols.index(message[i])) * (len(symbols) ** (i % blockSize))
        blockPosition += 1
        if blockPosition >= blockSize or i == (len(message) - 1):
            #if block is full move to next block
            blocks.append(blockInteger)
            blockInteger = 0
            blockPosition = 0
            blockNumber += 1
    return(blocks)
