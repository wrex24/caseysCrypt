import detectEnglish as e

message = ''

def check_encrypt():
    global key
    print('Would you like to break a message?\ny/n')
    answer = input()
    if answer == 'y':
        return True
    return False


def crypt():
    global mode
    global key
    key = 0
    symbols = ' abcdefghijklmnopqrstuvwxyz'
    for j in range(0,27):
        encrypted_message = ''
        for i in range(0, len(message)):
            #print(message[i])
            #print(symbols.find(message[i]))
            new_position = (symbols.find(message[i]) - key)%27
            #print(new_position)
            #print(symbols[new_position])
            encrypted_message = encrypted_message + symbols[new_position]
        key = key + 1
        if e.isEnglish(encrypted_message, wordPercentage=20, letterPercentage=85):
                print(encrypted_message + ' Key: ' + str(key-1))
        


while True:
    if check_encrypt():
        print('What is the message?')
        message = input()
        crypt()
    else:
        break
