"""
# Frequency of charcaters in a string
st = "laskdjkjdaksjaksjdalksdjlkajdklasjdkl"
st_set = set(st)
dic = dict()
for c in st_set:
    dic.update({c:st.count(c)})
print(dic)


st = "laskdjkjdaksjaksjdalksdjlkajdklasjdkl"
ch = []
dic = dict()
for c in st:
    if c not in ch:
        ch.append(c)
        count = 0
        for x in st:
            if x==c:
                count+=1
        dic.update({c:count})
print(dic)



# Strings are Anagram
st1 = "LISTEN"
st2 = "SILENT"
if len(st1)==len(st2):
    for c in st1:
        if c in st2:
            if st1.count(c)!=st2.count(c):
                print("Strings Are Not Anagram 2")
                break
        else:
            print("Strings Are Not Anagram 3")
            break
    else:
        print("Strings Are Anagram")
else:
    print("Strings Are Not Anagram 1")



# Strings are Anagram
st1 = "LISTEN"
st2 = "SILENT"
if len(st1)==len(st2):
    for x in st1:
        if st1.count(x)!=st2.count(x):
            print("Not Anagram")
            break
    else:
        print("Anagram")
else:
    print("Strings Are Not Anagram")

    
"""
# TIC_TAC_TOE_GAME
li = [1,2,3,4,5,6,7,8,9]
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
player = 'X'
flag = 0
choice = []
while True:
    print("\n\t\t TIC-TAC-TOE")
    print(f"\n\t\t  {li[0]} | {li[1]} | {li[2]} ")
    print("\t\t -----------")
    print(f"\t\t  {li[3]} | {li[4]} | {li[5]} ")
    print("\t\t -----------")
    print(f"\t\t  {li[6]} | {li[7]} | {li[8]} ")
    if flag == 1:
        break
    if len(choice)==9:
        print("\n\t\t MATCH TIES!")
        break
    print(f"\n\t      Player {player} Turns : ",end="")
    ch = int(input())
    if ch not in choice:
        choice.append(ch)
        li[ch-1] = player
        for win in wins:
            if li[win[0]]==li[win[1]] and li[win[1]]==li[win[2]]:
                print(f"\n\t\tPLAYER {player} WINS")
                flag = 1
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    else:
        input("\n\t  You can Repeat Value\n\t   Select Another One!")

