import rsaFunctions



def writeFile(information):
    file = open("senderInfo.txt","w+")
    for data in information:
        file.write("%s\n"%data)
    file.close()

def infoHash():

    information = []
    sender = input('Sender: ')
    receiver = input('Receiver: ')
    amount = input('Amount: ')
    rawInformation = [sender,receiver,amount]
    keyFile = ("%s_publicKey.txt" %sender)
    for rawData in rawInformation:
        data = rsaFunctions.encrypt(rawData, keyFile)
        information.append(data)
    return(information)

def getInfo():
    information = infoHash()
    writeFile(information)

if(__name__ == "__main__"):
    getInfo()
