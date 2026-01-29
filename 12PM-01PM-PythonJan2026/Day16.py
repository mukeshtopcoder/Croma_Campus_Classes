"""
String:-
String is a collection of characters
String behave like a tuple

string_name = "charcters"
st = "AMAN"

st = "Aman"
st = str(123)
st = str("23756(^&#^kbdkhKJVK")
st = ""
print(st)
print( type(st) )


STRING works on INDEX (backward and forward)
st = "AMANKUMAR"
print(st)
print(st[3])

STRING can be SLICED
st = "AMANKUMAR"
print(st)
print(st[3])
print(st[2:7])

STRING CAN BE REPLICATES
st = "AMANKUMAR"
print(st)
print(st*3)

String Supports TRAVERSING/ITTERATION
st = "AMANKUMAR"
print(st)
for x in st:
    print(x)

Built-in Funtions
    max , min , len

st = "AMANKUMAR"
print(st)
print(max(st))
print(min(st))
print(len(st))

String's Methods
    upper , lower , capitalize , strip(remove leading and trailing over spaces)

a = "  aman kumar  "
print(a)
print(a.upper())
print(a.lower())
print(a.strip())
a = a.strip()
print(a.capitalize())

    split , join , endswith , startswith
st = "Aman is a good boy"
print(st)
print( st.split())
print( st.split(" "))
print( st.split("is"))
print( "$".join(st) )
print( "$".join(st.split()) )
print( st.endswith("boy") )
print( st.endswith("good") )
print( st.startswith("Aman") )
print( st.startswith("boy") )


    isnumeric , isalpha , isalnum
st1 = "15456"
st2 = "aman"
st3 = "aman123"
st4 = "aman$123"
print( st1.isnumeric())
print( st3.isnumeric())
print( st2.isalpha() )
print( st3.isalpha() )
print( st2.isalnum() )
print( st3.isalnum() )
print( st1.isalnum() )
print( st4.isalnum() )

    replace , count , find

st = "Python Programming"
print(st)
print(st.replace("Programming",'Language'))
# String is immuteable (You can not change anything in th string)
print(st)
print( st.find("Programming") )
print( st.find("aman") )
print( st.count("r") )  

    
st = "AmanKumarZishan"
print( max(st) )  # u
print( min(st) )  # A

num = 65
print(num)
print( chr(num) )

A => 65
Z => 90
a => 97
z => 122
A and a has exactly 32 difference

"""

