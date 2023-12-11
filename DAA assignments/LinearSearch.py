import time

diff=0
def linear_search(arr,key):
    start_time=time.time()
    for i in range (0,len(arr)): 
        if arr[i]==key:
            end_time=time.time()
            print(f'time taken : {end_time-start_time}')
            return i
    
    diff=end_time-start_time
    
    return i
new=[]
f=open("./files/File 9.txt","r")

contents=f.readlines()
contents = list(map(lambda x : int(x.replace('\n','')),contents))

size=len(new)
key2=0
key=contents[0]
key1=-90
#worst case scenarios
index=linear_search(contents,key)



