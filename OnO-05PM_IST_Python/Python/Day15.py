"""

Dictionary:- A dictionary is a collection of {key:value}
pair, and it is called item. 


d = {1:13,2:56,3:67,7:89,9:76}
print(d)
print(type(d))
print( d[7] )


d = {'name':'Raman','dept':'HR','salary':37640}
print( d ) 
print( d['name'] )


in dictionary
1- keys should be unique
2- values can be duplicate


d = {1:23,2:56,3:52,2:99}
print( d )


Dictionary has no index
Dictionary works on KEYS
Dictionary can not be slice
Dictionary can not replicate

Dictionary can be traverse/itterate

d = {1:23,2:56,3:52,2:99}
print( d )
for x in d:
    print(x)


Dictionary's Method
    keys , values , items

d = {1:23,2:56,3:52,2:99}
print( d )
for x in d.keys():
    print(x)


d = {1:23,2:56,3:52,2:99}
print( d )
for x in d.values():
    print(x)


d = {1:23,2:56,3:52,2:99}
print( d )
for x in d.items():
    print(x)


d = {1:23,2:56,3:52,2:99}
print( d )
for k,v in d.items():
    print(k , v)



students = {
'rollno':[101,102,103,104,105],
'name':['Raman','Shyam','Simran','Renu','Hari'],
'class':['XII','IX','XI','VII','XII']
    }

for k in students:
    for v in students[k]:
        print(v,end='\t')
    print()


    update
d1 = {1:11,2:22,3:33}
d2 = {4:44,2:55,6:66}
d1.update(d2)
print(d1)

"""
