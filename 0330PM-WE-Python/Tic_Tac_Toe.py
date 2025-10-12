# TIC-TAC-TOE_Game
li = [1,2,3,4,5,6,7,8,9]
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
player = 'X'
flag = 0
selected = []
while True:
    print("\n\t\t  TIC-TAC-TOE")
    print("\n\t\t  ",li[0],"|",li[1],"|",li[2])
    print("\t\t  -----------")
    print("\t\t  ",li[3],"|",li[4],"|",li[5])
    print("\t\t  -----------")
    print("\t\t  ",li[6],"|",li[7],"|",li[8])
    if flag==1:
        break
    if len(selected)==9:
        print("\n\t\t It's A Tie Match")
        break
    print("\n\t\tPlayer",player,"Turns : ",end="")
    ch = int(input())
    if ch not in selected and (ch>0 and ch<10):
        selected.append(ch)
        li[ch-1] = player
        # Check Wining Stage
        for win in wins:
            if li[win[0]]==li[win[1]] and li[win[1]]==li[win[2]]:
                print("\n\t\t Player",player,"Wins!")
                flag = 1
        # Change Player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    else:
        print("\n\t  Already Selected Value!")
        print("\t  Or Invalid Value!")
        print("\t  Try Another Value!")

