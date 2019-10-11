import math, sys

symbols = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.!?"'


def main():
    global blockSize

    file = open('message.txt')
    rawMessage = file.read()
    file.close()
    message = filterText(rawMessage)
    messageFile = 'messageFile.txt'

    print('mode e/d')
    mode = input()
    
    if mode == 'e':
        print('whats the block size?')
        blockSize = 0
        blockInput = (input())
        if blockInput == 'max':
            while (2**1024)> (len(symbols)**(blockSize+1)):
                blockSize += 1
            
        else:
            blockSize = int(blockInput)
        print('Block Size = ' + str(blockSize))
        if (2**1024) < (len(symbols)**blockSize):
            sys.exit("block size too large")
        pubKeyFile = 'casey_publickey.txt'
        encryptWriteFile(pubKeyFile, messageFile, message)

    elif mode == 'd':
        privateKeyFile = 'casey_privatekey.txt'
        decryptedText = readDecryptFile(messageFile, privateKeyFile)

        print(decryptedText)


def filterText(rawMessage):
    message = ''
    for i in rawMessage:
        if symbols.find(i) != -1:
            message += i
    return message

def createBlocks(message):
    """creates blocks from message"""
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


def createText(encryptedBlocks, messageLength, blockSize):
    message = []
    for j in encryptedBlocks:
        blockMessage = []
        for i in range(blockSize-1, -1, -1):
            if len(message) + i < messageLength:
                charIndex = j // (len(symbols) ** i)
                j = j % (len(symbols) ** i)
                blockMessage.insert(0, symbols[charIndex])
        message.extend(blockMessage)
    return ''.join(message)


def encrypt(e,n, message):
    encryptedBlocks = []
    blocks = createBlocks(message)
    for i in range(0,len(blocks)):
        encryptedBlocks.append(pow(blocks[i], e, n))
    print(encryptedBlocks)
    return encryptedBlocks



def decrypt(encryptedBlocks, n, d, blockSize, messageLength):
    decryptedBlocks = []
    for i in encryptedBlocks:
        decryptedBlocks.append(pow(i, d, n))
    text = createText(decryptedBlocks, messageLength, blockSize)
    file = open('decryptedMessage.txt', 'w')
    file.write(text)
    file.close()
    return text

def readFile(fileName):
    '''read file and get information'''
    file = open(fileName)
    information = file.read()
    file.close()
    information = information.split(',')
    keySize, n , key = information
    return (int(keySize), int(n), int(key))


def encryptWriteFile(fileName, messageFile, message):
    keySize, n, e = readFile(fileName)
    encryptedBlocks = encrypt(e,n, message)
    for i in range(0, len(encryptedBlocks)):
        encryptedBlocks[i] = str(encryptedBlocks[i])
    encryptedMessage = ','.join(encryptedBlocks)

    file = open(messageFile, 'w')
    file.write('%s_%s_%s'%(len(message), blockSize, encryptedMessage))
    file.close()
    return encryptedMessage

def readDecryptFile(messageFile, fileName):
    encryptedBlocks = []
    keySize, n, d = readFile(fileName)
    
    file = open(messageFile)
    information = file.read()
    file.close()
    #print(information)
    #print(information.split('_'))
    messageLength, blockSize, encryptedMessage = information.split('_')
    messageLength = int(messageLength)
    blockSize = int(blockSize)

    for i in encryptedMessage.split(','):
        encryptedBlocks.append(int(i))
        
    decryptedMessage = decrypt(encryptedBlocks, n, d, blockSize, messageLength)
    return decryptedMessage
    

if __name__ == '__main__':
    main()
    print('press any key to exit')
    pause = input()
