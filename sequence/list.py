arr1 = [1, 2, 3]
print(type(arr1)) # <class 'list'>


arr2 = [10, 'hello world', 8.7]
print(arr2) # [10, 'hello world', 8.7]

arr1[0] = [1, 2, 3]
print(arr1) # [[1, 2, 3], 2, 3]

arr4 = []
print(arr4) # []

arr5 = list(range(0,10,1))
print(arr5[1:3]) # [1, 2]

print(arr5[-3]) # 7