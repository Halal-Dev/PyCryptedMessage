Mode = int(input('Crypt(1)/Decrypt(2)'))

if Mode == 1:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = int(input('Key  '))

    newMessage = ""
    message = input('Type a message to crypt :  ')

    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + key) % 26
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character
    print('The crypted message is :' + newMessage)
if Mode == 2:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = int(input('Key  '))

    newMessage = ""
    message = input('Type a message to decrypt :  ')

    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position - key) % 26
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character
    print('The Decrypted message is :'+ newMessage)
    
