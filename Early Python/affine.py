import cryptoMath, sys



def getKey():
    print('What is the first key?')
    getKey_one = int(input())
    print('What is the second key?')
    getKey_two = int(input())
    return getKey_one, getKey_two

def encrypt(message, key_one, key_two):
    symbols = ' abcdefghjklmnopqrstuvwxyz'
    new_message = ''
    for i in range(0, len(message)):
        position = symbols.find(message[i])
        position = int(position * key_one)%27
        position = (position + key_two)%27
        new_message += symbols[position]
    return new_message

while True:
    file = open('message.txt', 'r+')
    message = file.read()
    file.close()
    key_one, key_two = getKey()
    new_message = encrypt(message, key_one, key_two)
    print(new_message)
    print('press e to exit')
    pause = input()
    if pause == 'e':
        sys.exit()



