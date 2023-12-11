import copy
import time
def MergeSort(a, l, h):
    
    if l < h:
        mid1 = l+(h-l)//3
        mid2=h-(h-l)//3
        
        MergeSort(a, l, mid1)
        MergeSort(a,mid1+1,mid2)
        MergeSort(a, mid2+1, h)
        Merge(a, l, mid1,mid2, h)
    
    

def Merge(A, start, mid1, mid2, end):
    S1 = A[start:mid1+1]
    S2 = A[mid1+1:mid2+1]
    S3 = A[mid2+1:end+1]
    i = 0
    j = 0
    k = 0
    m = start
    while i < len(S1) and j < len(S2) and k < len(S3):
        if S1[i] <= S2[j] and S1[i] <= S3[k]:
            A[m] = S1[i]
            i += 1
        elif S2[j] <= S1[i] and S2[j] <= S3[k]:
            A[m] = S2[j]
            j += 1
        else:
            A[m] = S3[k]
            k += 1
        m += 1
    while i < len(S1):
        A[m] = S1[i]
        i += 1
        m += 1
    while j < len(S2):
        A[m] = S2[j]
        j += 1
        m += 1
    while k < len(S3):
        A[m] = S3[k]
        k += 1
        m += 1

f=open("./files/File 1.txt","r")

contents=f.readlines()#for average case
contents = list(map(lambda x : int(x.replace('\n','')),contents))
contents2=copy.copy(contents)
contents3=copy.copy(contents)
contents2.sort()
contents3.sort(reverse=True)
start_time=time.time()

MergeSort(contents,0,len(contents)-1)
end_time=time.time()

print(f'time taken : {end_time-start_time}')
