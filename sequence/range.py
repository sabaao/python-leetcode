
r1 = range(10)
r2 = range(10,50)
r3 = range(10,50,5)
r4 = range(10)

print(type(r1)) # <class'range'>
print(r1) # range(0,10)
print(list(r1)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(r3)) # [10, 15, 20, 25, 30, 35, 40, 45]
print(len(r1)) # 10
print(r1[1]) # 1

print(r1==r2) # False
print(r1==r4) # True

for i in range(1,10):
    print(i) # print 1 to 9