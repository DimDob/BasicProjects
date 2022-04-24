nums=[1,4,2,3,7]
print("Най-голяма стойност: ", max(nums))
print("Заден ред: ", list(reversed(nums)))
print("Възходяща стойност: ", sorted(nums))
print("Низходяща стойност: ", sorted(nums, reverse=True))
print("Брой аргументи: ", len(nums))
nums[0]="балон"
print("Замяна на аргумент във функцията: ", nums)
print("Срез: ", nums[1:len(nums)-1])
symbs=list("Baloon")
print("Думата разделена на нейните букви: ", symbs)
print(symbs[:2], symbs[2], symbs[3:])
nums=list(range(5,8))
print(nums)
nums=list(range(5,9))
print(nums)
nums=[1,5,6,4,9]
print(nums)
nums[1:3]=[]
print(nums)
nums=[1,5,6,4,9]
print(len(nums))
del nums[len(nums)-1]
nums=list(range(5,9+1))
print(nums)
del nums[len(nums-1)]
nums=list(range(5,9+1))
print(nums)
del nums[len(nums)-1]
print(nums)
nums=list(range(5,9+1))
del nums[len(nums)-1]
print(nums)
del nums[len(nums)-2+1]
print(nums)
del nums[len(nums)-3+1]
print(nums)
nums=list(range(5,9+1))
del nums[len(nums)-5]
print(nums)
nums=[2*k+1 for k in range(10)]
print(nums)
nums=[2*k for k in range(6)]
print(nums)
del nums[(len(nums)-5)]
print(nums)
symbs=list("Computer")
print(symbs[0:2], symbs[2:3+1], symbs[4:])

