import time
import copy
def insertion_sort(arr):
    start_time=time.time()
    for i in range (1,len(arr)):
        temp=arr[i]
        j=i-1
        while(arr[j]>temp and j>=0):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
        
                
    
    end_time=time.time()
    print(f'time taken : {end_time-start_time}')

f=open("./files/File 6.txt","r")

contents=f.readlines()#for average case
contents = list(map(lambda x : int(x.replace('\n','')),contents))
contents2=copy.copy(contents)
contents3=copy.copy(contents)
contents2.sort()
contents3.sort(reverse=True)

insertion_sort(contents3)


