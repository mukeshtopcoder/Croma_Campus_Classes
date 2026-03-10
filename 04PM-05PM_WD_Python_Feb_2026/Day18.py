"""
String :- String is a collection of characters and
it behaves like a tuple

s = "amankumar"
s = 'aman@kumar123'


s = 'aman@kumar123'
print(s)
print( type(s) )


String works on INDEX
forward indexing
backward indexing

s = 'amankumar'
print(s)
print( s[0:4] )
print( s[4:9] )
print( s[4] )

Strning also supports SLICING
print( s[4:] )
print( s[:4] )
print( s[2:7] )


String supports REPLICATION
st = "Ha"
print(st*3)

String Supports TRAVERSING/ITTERATION

st = "AMANKUMAR"
for ch in st:
    print(ch)


Built-in Functions
    max , min , len

String works on ASCII value
A = 65 , B = 66 --- Z = 90
a = 97 , b = 98 --- z = 122

st = "AmanKumar"
print( st )
print( max(st) )
print( min(st) )
print( len(st) )


0 = 48 , 1 = 49  --- 9 = 57

st = "aman@1234kumar"
print( st )
print( max(st) )
print( min(st) )
print( len(st) )


String's Built-in Functions
    upper , lower , capitalize

st = "aman Kumar"
print( st )
print( st.upper() )
print( st.lower() )
print( st.capitalize() )


    strip , lstrip , rstrip

st = "    aman       "
print( st )
print( len(st) )
print( st.strip() )
print( len(st.strip()) )
print( st.lstrip() )
print( len(st.lstrip()) )
print( st.rstrip() )
print( len(st.rstrip()) )


    find , index , count

st = "pythonprogramming"
print( st )
print( st.count('p') )  # will count 'p'
print( st.find('o') )
print( st.find('o',5) )
print( st.find("program") )
print( st.index('g') )
print( st.find('z') )  # it return -1 if not found
print( st.index('z') )  # it return error if not found


    replace , split


s = "I Love Python"
print(s)
print( s.replace('Python','Java') )   
print( s.split() )
s = "I$Love$Python"
print( s.split('$') )


    join
s = ['I','Love','Python']
print(s)
print( ''.join(s) )
print( ' '.join(s) )
print( '$'.join(s) )


s = "Honesty is the policy"
print( s.split() )
print( s.split(' ') )
print( s.split('is') )


CHECKING STRING CONTENT
    isalpha , isdigit , isalnum , islower , isupper

s = "aman"
print( s.isalpha() )
s = "aman123"
print( s.isalpha() )
s = "aman"
print( s.isdigit() )
s = "276"
print( s.isdigit() )
s = "276"
print( s.isalnum() )
s = "aman"
print( s.isalnum() )
s = "aman275"
print( s.isalnum() )
s = "aman@72"
print( s.isalnum() )
s = "aman"
print( s.islower() )
print( s.isupper() )


# WAP to convert into uppercase all first characters
of words of a sentence


s = "aman is my yonger brother"
print( s )
st = ""
for word in s.split():
    st = st+ word.capitalize()+" "

print(st)



s = 'aman'
st = ""
print(s)
for ch in s:
    st = st+chr(ord(ch)-32)
print(st)


s = 'AMAN'
st = ""
print(s)
for ch in s:
    st = st+chr(ord(ch)+32)
print(st)



# Write A Program to convert a word into toggle case
aman => Aman (Capitalize)   aMAN (toggle case)


s = 'AmANKumaR'
print(s)
st = ""
flag = 1
for ch in s:
    if flag==1:
        st=st+ch.lower()
        flag = 0
    else:
        st=st+ch.upper()
print(st)

"""
