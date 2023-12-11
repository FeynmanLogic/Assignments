import time
import copy
def bubble_sort(arr):
    start_time=time.time()
    for i in range (0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                
    
    end_time=time.time()
    print(f'time taken : {end_time-start_time}')

f=open("./files/File 5.txt","r")

contents=f.readlines()#for average case
contents = list(map(lambda x : int(x.replace('\n','')),contents))
contents2=copy.copy(contents)
contents3=copy.copy(contents)
contents2.sort()
contents3.sort(reverse=True)

bubble_sort(contents2)
