blocksize = int(input("Enter block size here: "))
block = input("Enter block here: ")
newblock = list(block)

print("Enter key here: ")
key = []
encrypttext = ''

for i in range(blocksize):
    x = int(input("Enter number here: "))
    key.append(x - 1)

for i in range(blocksize):
    encrypttext = encrypttext + newblock[key[i]]

print("Encrypted text is:")
print(encrypttext)

print("Now we attempt decryption")
size = int(input("Enter block size: "))
encryptblock = input("Enter encrypted text here: ")

keynew = []

for i in range(size):
    y = int(input("Enter number for key: "))
    keynew.append(y - 1)

decrypttext = ''
newblock2 = list(encryptblock)

for j in range(size):
    decrypttext = decrypttext + newblock2[keynew[j]]

print("Decrypted text is:")
print(decrypttext)
