import random

def encrypt(plaintext):
    plaintextlist=list(plaintext)
    keylist=[]
    for i in range(len(plaintextlist)):
        keylist.append(chr(int((random.randint(65,97)))))
    encrypttext=""
    print("Key here is:",keylist)
    for i in range(len(plaintextlist)):
       sum=(ord(plaintextlist[i])+ord(keylist[i])-130)%26
       char=chr(sum+65)
       encrypttext=encrypttext+char

    with open('encrypt3.txt', 'w') as output_file:
        output_file.write(encrypttext)
    return keylist,encrypttext

def decrypttext(encrypttext,keylist):
    decrypttext=""
    encrypttextlist=list(encrypttext)
    for i in range(len(encrypttextlist)):
        dif=(ord(encrypttextlist[i])-ord(keylist[i])-130)%26
        char=chr(dif+65)
        decrypttext=decrypttext+char
    with open('decryptt3.txt', 'w') as output_file:
        output_file.write(decrypttext)


with open('input3.txt', 'r') as file:
    
    plaintext=file.readline().strip()
keylist,encrypttext=encrypt(plaintext)
print("This is one time pad")
decrypttext(encrypttext,keylist)