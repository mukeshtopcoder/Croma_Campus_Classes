"""
STRING:-
String is a collection of characters. always enclose in
"" inverted commas or single comma.

st = "Hello"
st = 'Aman'
st = 's'
st = "s"
st = '''Aman'''
# Single line comment
st = '''Aman is a good boy
he is doing CA'''
print(st)
print(type(st))


String works on index.
forward    0,1,2,3...
backward    -1,-2,-3...

st = "aman kumar"
print(st)
print(st[3])
print(st[-3])


String can be sliced
string_variable_name[start:stop:step]

st = "aman kumar"
print(st)
print(st[0:4])
print(st[:4])
print(st[5:])

String can be replicate
st = "aman"
print(st*3)


String can be traversed!
st = "HELLOINDIA"
for i in st:
    print(i)


Built-in functions
max , min , len

st = 'helloindia'
print(st)
print(max(st))
print(min(st))
print(len(st))


Character's works on ASCII value.
ASCII Values
A = 65 => 1000001
A,B,---Z   =>  65,66 ---- 90
a = 97 => 1100001
a,b,----z  =>   97,98----122

space's ASCII Value => 32



st = 'Aman Kumar Zishan'
print(min(st))


built-in functions
ord , chr
s = 65
r = 'Z'
print(chr(s))   # convert into character
print(ord(r))   # print the ASCII Value


s = 'A'
print(chr(ord(s)+32))


s = 'AMAN KUMAR'
st = ''
for i in s:
    if i!=' ':
        st = st+chr(ord(i)+32)
    else:
        st = st+i
print(st)




WAP to convert lower case to upper case.
s = 'aman kumar'
st = ''
for i in s:
    if i!=' ':
        st = st+chr(ord(i)-32)
    else:
        st = st+i
print(st)


Numbers's ASCII Value
0 = 48
1 = 49
.
.
9 = 57

s = 'skjdg873t2&@$*irnwer09jh4r'
st = ''
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        st = st+chr(ord(i)-32)
    else:
        st = st+i
print(st)


"""
s = 'AmAn KuMaR'
st = ''
for i in s:
    if ord(i)>=97 and ord(i)<=122:
       st = st+chr(ord(i)-32)
    elif ord(i)>=65 and ord(i)<=90:
       st = st+chr(ord(i)+32)
    else:
        st = st+i
print(st)



