"""
TIC-TAC-TOE
"""
li = [1,2,3,4,5,6,7,8,9]
player = 'X'
flag = 0
choices = []
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
while True:
    print("\n\t\t  TIC-TAC-TOE")
    print(f"\n\t\t   {li[0]} | {li[1]} | {li[2]} ")
    print("\t\t  -----------")
    print(f"\t\t   {li[3]} | {li[4]} | {li[5]} ")
    print("\t\t  -----------")
    print(f"\t\t   {li[6]} | {li[7]} | {li[8]} ")
    if flag==1:
        break
    if len(choices)==9:
        print("\n\t\t    MATCH TIE!")
        break
    print(f"\n\t\tPLAYER {player} TURNS : ",end="")
    ch = int(input())
    if ch not in choices and ch>=1 and ch<=9:
        choices.append(ch)
        li[ch-1] = player
        # Check WINING CONDITION
        for i,j,k in wins:
            if li[i]==li[j] and li[j]==li[k]:
                print(f"\n\t\t PLAYER {player} WIN!")
                flag = 1
        if player=='X':
            player='O'
        else:
            player='X'
    elif ch>=1 and ch<=9:
        print("\n\t    VALUE ALREADY SELECTED")
    else:
        print("\n\t    INVALID VALUE")
        
