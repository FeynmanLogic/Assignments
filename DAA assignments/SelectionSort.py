import time
import copy
def selection_sort(arr):
    start_time=time.time()
    for i in range (0,len(arr)):
        min=i
        
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min]):
                temp=arr[min]
                arr[min]=arr[j]
                arr[j]=temp
                
    
    end_time=time.time()
    print(f'time taken : {end_time-start_time}')

f=open("./files/File 6.txt","r")

contents=f.readlines()#for average case
contents = list(map(lambda x : int(x.replace('\n','')),contents))
contents2=copy.copy(contents)
contents3=copy.copy(contents)
contents2.sort()
contents3.sort(reverse=True)

selection_sort(contents2)

