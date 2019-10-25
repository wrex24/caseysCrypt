
symbols = ' abcdefghijklmnopqrstuvwxyz'

def makeKey():
    global symbols
    intKey = []
    print("what's the key?")
    strKey = input()
    for i in strKey:
        position = symbols.find(i)
        intKey.append(position)
    return(intKey)
        

def check_encrypt():
    global key
    print('Would you like to encrypt a message?\ny/n')
    answer = input()
    if answer == 'y':
        return True
    return False

def crypt(message, key):
    global symbols
    encrypted_message = ''
    for i in range(0,len(message)):
        new_position = (symbols.find(message[i]) + key[i%len(key)])%27
        encrypted_message = encrypted_message + symbols[new_position]
        
    return encrypted_message

while True:
    if check_encrypt():
        encrypted_message = ''
        print('What is the message?')
        message = input()
        key = makeKey()
        encrypted_message = crypt(message, key)
        print(encrypted_message)
    else:
        break
