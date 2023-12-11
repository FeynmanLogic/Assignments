
nums=[]
nums=input()
nums.split(' ')
ans=[]
target=input()
for i in range(0,len(nums)):
    for j in range(0,len(nums)):
        
        if((nums[i]+nums[j])==target and i!=j):
            ans.append(i)
            ans.append(j)
print(nums)

print(ans)