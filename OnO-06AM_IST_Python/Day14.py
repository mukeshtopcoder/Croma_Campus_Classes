# STRING
"""
String:- it is also a collection of characters
st = "aman725(^&#"


st = 'aman'
st = "aman"
st = '''aman'''
st = str(1234)
print(st)


String works on INDEX
forward index and backward index

st = 'amankumar'
print(st)
print(st[4])
print(st[-5])

String can be sliced

st = 'amankumar'
print(st)
print(st[2:7])


REPLICATION
st = 'HA'
print(st*3)

TRAVERSING
st = 'AMANKUMAR'
print(st)
for x in st:
    print(x)

Built-in FUnctions
max , min , len
st = 'AMANKUMAR'
print(max(st))
print(min(st))
print(len(st))


String's Method
lower , upper , title , strip , replace , split , join

"""
st = 'AmAnkuMar'
print(st.lower())
print(st.upper())
print(st.title()) # first letter capital rest small
print(st.replace('AmAn','Suman'))  # return a new string
print(st)  # it is immuteable
st = "aman is a very good boy"
li = st.split()
print(li)
li = st.split("very")
print(li)
st = 'AMAN'
print( '$'.join(st) )
st1 = 'AMAN'
st2 = 'Kumar'
st3 = 'Sharma'
print( '#'.join([st1,st2,st3]) )

st1 = "    aman     singh  "
st2 = "         kumar "
print(st1.strip())
print(st2.strip())
# count , endswith , startswith , 

st = "AMANKUMAR"
print(st.count('A'))
print(st.endswith("KUMAR"))
print(st.endswith("AMAN"))
print(st.startswith("AMAN"))
print(st.startswith("KUMAR"))

name = "aman"
print(f"My name is {name} and i am from Noida")


st = "aman is a good boy"
li = st.split()
print(li)
st = ''.join(li)
print(st)


"""

Collections
list, tuple , set , dictionary , string , range()
list hetreogenous [] muteable
tuple hetreogenurs () immuteable
set hetreogenous {} only keys (unique data) unorder no index
dic {key:value} pair's collection , key(unique) , ordered
string homogenour (only characters) - behave like a tuple
range works with int only (homogenous) works like a list
"""
