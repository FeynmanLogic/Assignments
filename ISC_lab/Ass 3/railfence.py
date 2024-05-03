def encryptRailFence(text, depth):

    mssg = [['*' for i in range(len(text))] for j in range(depth)] 
    dir = 'down'
    row = 0
    col = 0
    for i in range(len(text)):
        if (row == 0):
            dir = 'down'
        elif (row == depth - 1):
            dir = 'up'
        mssg[row][col] = text[i]
        col += 1
        if dir == 'down':
            row += 1
        else:
            row -= 1
    result = []
    for i in range(depth):
        for j in range(len(text)):
            if mssg[i][j] != '*':
                result.append(mssg[i][j])
    return("" . join(result))

def decryptRailFence(cipher, depth):

    mssg = [['*' for i in range(len(cipher))] for j in range(depth)]
    dir = 'down'
    row = 0
    col = 0
    for i in range(len(cipher)):
        if row == 0:
            dir = 'down'
        if row == depth - 1:
            dir = 'up'
        mssg[row][col] = '0'
        col += 1
        if dir == 'down':
            row += 1
        else:
            row -= 1

    cur_pos = 0
    for i in range(depth):
        for j in range(len(cipher)):
            if ((mssg[i][j] == '0') and (cur_pos < len(cipher))):
                mssg[i][j] = cipher[cur_pos]
                cur_pos += 1
    print(mssg)
         
    result = []
    row = 0
    col = 0
    for i in range(len(cipher)):
         
        if row == 0:
            dir  = 'down'
        if row == depth-1:
            dir = 'up'
             
        if (mssg[row][col] != '*'):
            result.append(mssg[row][col])
            col += 1
        if dir == 'down':
            row += 1
        else:
            row -= 1
    return("".join(result))

string=input("Enter string here: ")
encryptstring=encryptRailFence(string,3)
print(encryptstring)
decryptstring=decryptRailFence(encryptstring,3)
print(decryptstring)
