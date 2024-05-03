print("we'll try to implement a rcolumnar cipher, length should be less than 25 for now, we'll add x if needed")
plaintext=input("Give plaintext here: ")
word1=''
word2=''
word3=''
word4=''
word5=''
count=1
if len(plaintext)<25:
    for k in range(25-len(plaintext)):
        plaintext=plaintext+'x'
for i in plaintext:
    if count%5==1:
        word1=word1+i
    if count%5==2:
        word2=word2+i
    if count%5==3:
        word3=word3+i
    if count%5==4:
        word4=word4+i
    if count%5==0:
        word5=word5+i
    count=count+1
print("Encrypted text is:")
print(word1+word2+word3+word4+word5)
print("Now we'll attempt decryption")
encryptedtext=input("Enter encrypted text here: ")
word1=''
word2=''
word3=''
word4=''
word5=''
count=1
for i in encryptedtext:
    if count%5==1:
        word1=word1+i
    if count%5==2:
        word2=word2+i
    if count%5==3:
        word3=word3+i
    if count%5==4:
        word4=word4+i
    if count%5==0:
        word5=word5+i
    count=count+1
print("Decrypted text is:")
print(word1+word2+word3+word4+word5)