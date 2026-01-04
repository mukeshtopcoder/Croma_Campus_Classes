"""
Dictionary:- A dictionary is a built-in data type
used to store data in key:value pairs.
dic = {4:76,6:67,8:7895,0:3455}

dic = {4:76,6:6
print(dic)
print( dic[6] )


Key points:-
- Keys are unique
- Values can be any data or can be duplicate
- Dictionaries are mutable (changeable)

dic = {'name':'Raman Kumar' , 'age':25 , 'add':'Noida'}
print(dic)
print( dic['age'] ) 

# Get value from a dictionary
dic = {'name':'Raman Kumar' , 'age':25 , 'add':'Noida'}
print(dic)
print( dic.get("age","Not Available") ) 
print( dic.get("mobile","Not Available") )

student = [
{'name':'Raman Kumar','age':38,'add':'Noida'},
{'name':'Raju','age':28,'mobile':'+919898876786'}
    ]
print(student)

for stu in student:
    print("Name",stu.get('name','Not Available'))
    print("Age",stu.get('age',"Not Available"))
    print("Address",stu.get('add',"Not Available"))
    print("Mobile",stu.get('mobile',"Not Available"))


# Add New Pair
student = {'name':'Rahul','age':23}
print(student)
student['add'] = 'Delhi'
print(student)
# Update an Existing Key
student['age'] = 24
print(student)


# Removing Element
student = {'name':'Rahul','age':23,'add':'Noida','mobile':'+91852373456'}
print(student)
student.pop("age")   # remove pair on key basis
print(student)
student.popitem()    # Automatically last pair remove
print(student)
del student['name']
print(student)
student.clear()
print(student)

# By default it will traverse KEYS
# Iteration / Traversing
dic = {1:34,3:466,5:567,6:785,7:457,8:862}
print(dic)
for key in dic:
    print(key)

# Traverse VALUES
# Iteration / Traversing
dic = {1:34,3:466,5:567,6:785,7:457,8:862}
print(dic)
for val in dic.values():
    print(val)

# Traverse KEYS
# Iteration / Traversing
dic = {1:34,3:466,5:567,6:785,7:457,8:862}
print(dic)
for k in dic.keys():
    print(k)

# Iterate Pairs
# Iteration / Traversing
dic = {1:34,3:466,5:567,6:785,7:457,8:862}
print(dic)
for k in dic.items():
    print(k)

# Iterate key and value seprately 
# Iteration / Traversing
dic = {1:34,3:466,5:567,6:785,7:457,8:862}
print(dic)
for k,v in dic.items():
    print('KEY :',k,' VALUE :',v)


# Update
dic = {'name':'Raju' , 'age':19}
print(dic)
dic['age'] = 28
print(dic)
dic.update({'name':'Raju Singh'})
print( dic )

# Update
dic = {'name':'Raju' , 'age':19}
print(dic)
dic['age'] = 28
print(dic)
dic.update({'name':'Raju Singh'})
print( dic )

# PRACTICE QUESTIONS
1. Create a list of 10 integers.
li = [23,34,45,56,67,78,89,90,25,25]
print(li)

2. Find the sum and average of elements in a list.

li = [23,34,45,56,67,78,89,90,25,25]
print(li)
print( "Sum :",sum(li) )
print( "Average :",sum(li)/len(li) )

3. Find the largest and smallest element in a list.
li = [23,34,45,56,67,78,89,90,25,25]
print(li)
print("Max Value :", max(li))
print("Min Value :", min(li))

4. Reverse a list without using reverse().
li = [23,34,45,56,67,78,89,90,25,25]
newList = []
print(li)
for x in range(-1, -len(li)-1, -1):
    newList.append(li[x])

print(newList)


li = [23,34,45,56,67,78,89,90,25,25]
newList = []
print(li)
for x in li[::-1]:
    newList.append(x)

print(newList)


li = [23,34,45,56,67,78,89,90,25,25]
print(li)
print(li[::-1])

5. Sort a list in ascending and descending order.
li = [23,34,45,56,67,78,89,90,25,25]
print(li)
li.sort()
print(li)
li.sort(reverse=True)
print(li)

6. Remove duplicate elements from a list.

li = [23,34,45,89,67,23,89,90,45,25]
print(li)
print( list( set(li) ) )

"""
