"""
String:- String is a collection of characters.
variable_name = "mention your charcaters"

name = 'A'
name = "A"
name = 'Aman'
name = "Aman"
name = '''Aman'''
name = '''Aman'''
name = '''Aman is a good boy
he is in BCA''' 
name = 'lskdhKUGDSOUH287358(*@%#&%$jgsdk'
print(name)

String behave like a tuple
String is immuteable
name = "RAHUL KUMAR"
print(name)

String works on index
backward(-1,-2,-3..) and forward(0,1,2,3,4) indexing

name = "RAHUL KUMAR"
print(name)
print(name[3])
print(name[-3])


Slicing:-
string_name[start:stop:step]
name = "RAHUL KUMAR"
print(name)
print(name[2:7])


Replcation
print(string_name*3)

name = "RAHUL KUMAR"
print(name*4)


Traversing
for c in string_name:
    print(c)

name = "RAHUL KUMAR"
for i in name:
    print(i)



Built-in Functions
max , min , len

name = "RAHULKUMAR"
print(max(name))
print(min(name))
print(len(name))


A: 65 - Z : 90
a: 97 - z : 122

name = "AmanZishan"
print(max(name))
print(min(name))


st = 'A'
num = 122
print(st)
print(num)
print(ord(st))
print(chr(num))


# WAP to convert uppercase character to lowercase character
st = 'D'
print(chr(ord(st)+32))

# WAP to convert uppercase character to lowercase character
st = 'B'
if ord(st)>=65 and ord(st)<=90:
    print(chr(ord(st)+32))
else:
    print(st)



Methods:-
Basic String Methods
upper , lower , title , capitalize , swapcase

st = 'aMan Kumar'
print(st.upper())
print(st.lower())
print(st.title())
print(st.capitalize())
print(st.swapcase())
print(st)


Searching and sorting methods
find , rfind , index , count , startswith , endswith

st = 'Aman Kumar'
print(st.find("m"))
print(st.find("z"))
print(st.rfind("m"))
print(st.index("K"))
# print(st.index("z"))
# through an error because z is not available
print(st.count('m'))  # it will count 'm'
print(st.startswith("Aman"))
print(st.endswith("ar"))


"""
