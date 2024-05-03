key = input('Enter key = ')
M =  [['0' for i in range(5)] for j in range(5)]
D={}
for i in range(ord('A'),ord('Z')+1,1):
    if chr(i)== 'J':
        continue
    else:
        D[chr(i)]=0
print(D)
pos = 0
row = 0
column = 0
for i in range(len(key)):
    if key[pos]=='J':
        M[row][column]='I'
        D['I']=[row,column]
        column+=1
        if column == 5 :
            column = 0
            row+=1
        pos+=1
    elif D[key[pos]]==0:
        M[row][column]=key[pos]
        D[key[pos]]=[row,column]
        column+=1
        if column == 5 :
            column = 0
            row+=1
        pos+=1
    else:
        pos+=1
print(row)
print(column)
print(M)
for i in D.keys():
    if D[i]==0:
        M[row][column]=i
        D[i]=[row,column]
        column+=1
        if column == 5 :
            column = 0
            row+=1
print(M)
print(D)
plaintext=input('Enter text = ')
to_encrypt=''
for i in range(0,len(plaintext)-1,2):
    if plaintext[i]!=plaintext[i+1]:
        to_encrypt+=plaintext[i]
        to_encrypt+=plaintext[i+1]
    elif plaintext[i]==' ':
        i-=1
        continue
    else:
        to_encrypt+=plaintext[i]
        to_encrypt+='X'
to_encrypt+=plaintext[-1]
if len(to_encrypt)%2!=0:
    to_encrypt+='X'
print(to_encrypt)
encrypted=''
for i in range(0,len(to_encrypt)-1,2):
    pos1=D[to_encrypt[i]]
    pos2=D[to_encrypt[i+1]]
    print(pos1)
    print(pos2)
    if pos1[0]==pos2[0]:
        npos1=[pos1[0],(pos1[1]+1)%5]
        npos2=[pos2[0],(pos2[1]+1)%5]
    elif pos1[1]==pos2[1]:
        npos1=[(pos1[0]+1)%5,pos1[1]]
        npos2=[(pos2[0]+1)%5,pos2[1]]
    else:
        temp=pos1
        npos1=[pos2[0],pos1[1]]
        npos2=[temp[0],pos2[1]]
    encrypted+=M[npos1[0]][npos1[1]]+M[npos2[0]][npos2[1]]
print(encrypted)

decrypted=''
print(D)
for i in range(0,len(encrypted),2):
    print(encrypted[i])
    print(encrypted[i+1])
    pos1=D[encrypted[i]]
    pos2=D[encrypted[i+1]]
    print(pos1)
    print(pos2)
    if pos1[0]==pos2[0]:
        nnpos1=[pos1[0],(pos1[1]-1)%5]
        nnpos2=[pos2[0],(pos2[1]-1)%5]
    elif pos1[1]==pos2[1]:
        nnpos1=[(pos1[0]-1)%5,pos1[1]]
        nnpos2=[(pos2[0]-1)%5,pos2[1]]
    else:
        temp=pos1
        temp2=pos2
        nnpos1=[temp2[0],temp[1]]
        nnpos2=[temp[0],temp2[1]]
    decrypted+=M[nnpos1[0]][nnpos1[1]]+M[nnpos2[0]][nnpos2[1]]
print(decrypted)
