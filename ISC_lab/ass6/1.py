
def encrypt(plaintext,key):
    
    plaintextlist=list(plaintext)
    print(plaintextlist)
    something=list(key)
    keylist=[]
    encrypttext=""
    x=len(something)
    for i in range(len(plaintextlist)):
        keylist.append(something[i%x])
    i=0
    print(keylist)
    for i in range(len(plaintextlist)):
       sum=(ord(plaintextlist[i])+ord(keylist[i])-130)%26
       char=chr(sum+65)
       encrypttext=encrypttext+char

    with open('encrypt.txt', 'w') as output_file:
        output_file.write(encrypttext)
    return keylist,encrypttext
def decrypt(encrypttext,keylist):
    decrypttext=""
    encrypttextlist=list(encrypttext)
    for i in range(len(encrypttextlist)):
        dif=(ord(encrypttextlist[i])-ord(keylist[i])-130)%26
        char=chr(dif+65)
        decrypttext=decrypttext+char
    with open('decryptt.txt', 'w') as output_file:
        output_file.write(decrypttext)
  
with open('input.txt', 'r') as file:
    
    key = file.readline().strip()
    plaintext=file.readline().strip()
keylist,encrypttext=encrypt(plaintext,key)
decrypt(encrypttext,keylist)