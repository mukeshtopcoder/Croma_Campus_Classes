"""
String:- String is a collection of characters
a = "amankumar"   # this is a string
string behave like a tuple

st = "amankumar"
st = ""
st = str("amankumar123")
print(st)

String can work on index
forward index   0,1,2,3..
backward index  -1,-2,-3..

st = "amankumar"
print(st)
print(st[3])
print(st[-6])


String can be sliced
st_name[start:stop:step]

st = "amankumar"
print(st)
print(st[2:7])
print(st[2:7:2])


String can be replicated
Replication

st = "Ha"
print(st)
print(st*3)


Traversing
st = "AMANKUMAR"
print(st)
for ch in st:
    print(ch)

String Operations
    + (Concatenation)
    * (Replication)

st1 = "aman"
st2 = "kumar"
print( st1*3 )
print( st1+st2 )


Built-in Functions
    len , max , min

st = "amankumar"
print(st)
print(max(st))
print(min(st))
print(len(st))


String's Methods
    upper , lower , title , capitalize , strip ,
    replace , find , split , join

st = "   Aman Kumar   "
print(st)
print( st.upper() )
print( st.lower() )
print( st.title() )
print( st.capitalize() )
print( st.strip() )   #  remove extra spaces
print( st.replace("Aman","Vijay") )
print( st.find("an") )
print( st.split() )
print( "$".join(st) )

st = ['Python','is','a','porgramming','langauge']
print(st)
print( " ".join(st) )


Check String Content
    isalpha() , isdigit() , isalnum() , startswith , endswith

st = "Python123"
print( st )
print( st.isalpha() )
print( st.isdigit() )
print( st.isalnum() )
print( st.startswith("Py") )
print( st.endswith("on") )

String is immuteable

st = "aman kumar"
print( st.replace("aman",'vijay') )
print(st)   # it will print the actual value


st = "RAHUL"
print( st )
print( st[ : : -1 ] )

WAP to count number of vowels in a string

st = "Amankumar"
count = 0
for ch in st:
    if ch in "AEIOUaeiou":
        count+=1
print("Total Vowels :",count)

WAP to remove duplicate characters from a string
st1 = 'aman kumar'
st2 = ""

for ch in st1:
    if ch not in st2:
        st2 = st2+ch

print(st2)

WAP to count words in a sentence

st = "aman is a good boy"
print( st )
print( len(st.split()) )

st = "aman is a good boy "
print(st.split())
print(st.split("good"))

WAP to Reverse every word in a sentence

st = "I LOVE PYTHON PROGRAMMING"
print(st)
st2 = ""
for word in st.split():
    st2 = st2+word[::-1]+" "
print(st2)


st = "I LOVE PYTHON PROGRAMMING"
print( st )
print( " ".join([word[::-1] for word in st.split()]) )

"""

