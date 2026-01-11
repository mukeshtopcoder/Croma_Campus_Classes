print("\n\t    ***** TIC TAC TOE *****")
li = [1,2,3,4,5,6,7,8,9]
player = 'X'
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
flag = 0
choices = []
# DASHBOARD
while True:
    print(f"\n\t\t   {li[0]} | {li[1]} | {li[2]}")
    print("\t\t  -----------")
    print(f"\t\t   {li[3]} | {li[4]} | {li[5]}")
    print("\t\t  -----------")
    print(f"\t\t   {li[6]} | {li[7]} | {li[8]}")
    if flag==1:
        break
    print(f"\n\t       PLAYER {player} TURN : ",end="")
    ch = int(input())
    if ch not in choices:
        choices.append(ch)
        li[ch-1] = player
        for w in wins:  
            if li[w[0]]==li[w[1]] and li[w[1]]==li[w[2]]:
                print(f"\n\t\t PLAYER {player} WIN!")
                flag = 1
        if player=='X':
            player='O'
        else:
            player='X'
    else:
        print("\n\t    ALREADY SELECTED VALUE!") 
