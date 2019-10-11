import sys, random, os, primeNum, cryptoMath

def main():
    print('input name')
    name = input()
    print('input key size')
    keySize = int(input())
    createFiles(name, keySize)



def createKey(keysize):
    p = 0
    q = 0
    e = 0
    d = 0
    print('finding p, q, and n')
    while q == p:
        q = primeNum.generateLargePrime(keysize=1024)
        p = primeNum.generateLargePrime(keysize=1024)
    n = p * q

    print('finding e')
    while cryptoMath.gcd(e, (p-1)*(q-1)) != 1:
        e = random.randrange(2 ** (keysize-1), 2 ** (keysize))

    print('finding d')
    d = cryptoMath.findModInverse(e, (p-1)*(q-1))

    publicKey = (n, e)
    privateKey = (n, d)

    return(publicKey, privateKey)

def createFiles(name, keySize):
    if os.path.exists('%s_publickey.txt' %(name)) or os.path.exists('%s_privatekey,txt' %(name)):
        sys.exit('%s_publickey.txt or %s_privatekey already exists. Use a new name or delete files to continue' %(name, name))

    public, private = createKey(keySize)

    print('\ncopying to public key file')
    file = open('%s_publickey.txt' % (name), 'w')
    file.write('%s,%s,%s' %(keySize, public[0], public[1]))
    file.close()

    print('\ncopying to prvate key file')
    file = open('%s_privatekey.txt' % (name), 'w')
    file.write('%s,%s,%s' %(keySize, private[0], private[1]))
    file.close()


if __name__ == '__main__':
    main()
    print('press any key to exit')
    pause = input()
