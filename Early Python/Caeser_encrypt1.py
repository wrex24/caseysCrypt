mode = ''
key = 0

def check_encrypt():
    global mode
    global key
    print('Would you like to encrypt a message?\ny/n')
    answer = input()
    if answer == 'y':
        print('encrypt (e) or decrypt (d)?')
        mode = input()
        print("what's the key?")
        key = int(input())
        return True
    return False

def crypt(message):
    global mode
    global key
    encrypted_message = ''
    symbols = ' abcdefghijklmnopqrstuvwxyz'
    for i in range(0, len(message)):
        #print(message[i])
        #print(symbols.find(message[i]))
        if mode == 'e':
            new_position = (symbols.find(message[i]) + key)%27
        if mode == 'd':
            new_position = (symbols.find(message[i]) - key)%27
        #print(new_position)
        #print(symbols[new_position])
        encrypted_message = encrypted_message + symbols[new_position]
        
    return encrypted_message

while True:
    if check_encrypt():
        encrypted_message = ''
        print('What is the message?')
        message = input()
        encrypted_message = crypt(message)
        print(encrypted_message)
    else:
        break
