dict1 = {'name':'Charles','age': 34, 'sex':'Male'}
print(dict1['name']) # Charles

dict1['age'] = 33
print(dict1['age']) # 33

del dict1['sex']
print(dict1) # {'name': 'Charles', 'age': 33}

dict1.clear()
print(dict1) # {}