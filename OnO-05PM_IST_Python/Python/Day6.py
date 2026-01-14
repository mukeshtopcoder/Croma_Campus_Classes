"""

ch = input("Enter A Character : ")
if ch=='A':
    print("Vowel")
else:
    if ch=='E':
        print("Vowel")
    else:
        if ch=='I':
            print("Vowel")
        else:
            if ch=='O':
                print("Vowel")
            else:
                if ch=='U':
                    print("Vowel")
                else:
                    print("Consonant")


ELIF

ch = input("Enter A Character : ")
if ch=='A':
    print("Vowel")
elif ch=='E':
    print("Vowel")
elif ch=='I':
    print("Vowel")
elif ch=='O':
    print("Vowel")
elif ch=='U':
    print("Vowel")
else:
    print("Consonant")


Complex Condition


ch = input("Enter A Character : ")
if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U': 
    print("Vowel")
else:
    print("Consonant")


ch = input("Enter A Character : ")
if ch in "AEIOUaeiou": 
    print("Vowel")
else:
    print("Consonant")


# WAP to find greater value among three

n1 = int(input("Enter A Number : "))
n2 = int(input("Enter B Number : "))
n3 = int(input("Enter C Number : "))
if n1>n2 and n1>n3:
    print(n1)
elif n2>n1 and n2>n3:
    print(n2)
else:
    print(n3)


"""

