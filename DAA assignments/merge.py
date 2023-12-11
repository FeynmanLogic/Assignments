import copy
import time
def MergeSort(a, l, h):
    
    if l < h:
        mid = (l + h) // 2
        MergeSort(a, l, mid)
        MergeSort(a, mid + 1, h)
        Merge(a, l, mid, h)
    
    

def Merge(A, start, mid, end):
    S1 = A[start:mid+1]
    S2 = A[mid+1:end+1]
    i = 0
    j = 0
    k = start
    while i < len(S1) and j < len(S2):
        if S1[i] < S2[j]:
            A[k] = S1[i]
            i += 1
        else:
            A[k] = S2[j]
            j += 1
        k += 1
    while i < len(S1):
        A[k] = S1[i]
        i += 1
        k += 1
    while j < len(S2):
        A[k] = S2[j]
        j += 1
        k += 1
f=open("./files/File 1.txt","r")

contents=f.readlines()#for average case
contents = list(map(lambda x : int(x.replace('\n','')),contents))
contents2=copy.copy(contents)
contents3=copy.copy(contents)
contents2.sort()
contents3.sort(reverse=True)
start_time=time.time()
MergeSort(contents,0,len(contents))
end_time=time.time()

print(f'time taken : {end_time-start_time}')
