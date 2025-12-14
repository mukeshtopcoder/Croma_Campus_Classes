"""
PATTERN BUILDING

A
AB
ABC
ABCD
ABCDE
A => 1000001 => 65
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end="")
    print()

    
A
BB
CCC
DDDD
EEEEE
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end="")
    print()

A
BC
DEF
GHIJ
KLMNO

ch = 65
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(ch),end="")
        ch=ch+1
    print()


12344321
123**321
12****21
1******1

"""
ch = 65
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(ch),end="")
        ch=ch+1
    print()
