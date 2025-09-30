"""
TIC-TAC-TOE
"""
choices = [1,2,3,4,5,6,7,8,9]
player = 'X'
selected = []
flag = 0
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
while True:
    print("\n\t\tTIC TAC TOE")
    print(f"\n\t\t {choices[0]} | {choices[1]} | {choices[2]}")
    print("\t\t-----------")
    print(f"\t\t {choices[3]} | {choices[4]} | {choices[5]}")
    print("\t\t-----------")
    print(f"\t\t {choices[6]} | {choices[7]} | {choices[8]}")
    if flag==1:
        break
    if len(selected)==9:
        print("\n\t       It's A TIE MATCH")
        break
    print(f"\n\t      Player {player} Truns : ",end="")
    ch = int(input())
    if ch >=1 and ch<=9:
        if ch not in selected:
            selected.append(ch)
            choices[ch-1] = player
            for w in wins:
                if choices[w[0]]==choices[w[1]] and choices[w[1]]==choices[w[2]]:
                    print(f'\n\t ###### Player {player} WIN! ######')
                    flag = 1
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        else:
            print("\n\tThis is Selected Position")
            print("\tTry Another Position!")
    else:
        print("\n\t\tWrong Entered!\n\t\tTry Again!")

