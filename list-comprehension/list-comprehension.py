arr1 = [i for i in range(10)]
print(arr1) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

arr2 = [x for x in arr1 if x%2==0]
print(arr2) # [0,2,4,6,8]

arr3 = [x for x in arr1 if x>=3 and x % 2]
print(arr3) #[3,5,7,9]

arr4 = [(x,y) for x in range(3) for y in range(4)]
print(arr4) # [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]
