from django.shortcuts import render,redirect

WINNING_COMBINATIONS = [
    (0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)
]

def check_winner(board):
    for a,b,c in WINNING_COMBINATIONS:
        if board[a]==board[b] and board[b]==board[c]:
            return board[a] 
    if '' not in board:
        return "Draw"
    return None

def index(request):
    # Initialize Game/Board
    if 'board' not in request.session:
        request.session['board'] = ['']*9
        request.session['player'] = 'X'
        request.session['winner'] = None
    
    if request.method == "POST":
        move = int(request.POST.get('cell'))
        board = request.session['board']
        player = request.session['player']

        if board[move] == '' and not request.session['winner']:
            board[move] = player

            winner = check_winner(board)
            if winner:
                request.session['winner'] = winner
            else:
                request.session['player'] = 'O' if player == 'X' else 'X'
        request.session['board'] = board
    context = {
        'board':request.session['board'],
        'player':request.session['player'],
        'winner':request.session['winner']
    }
    return render(request , "index.html",context)

def reset(request):
    request.session.flush()
    return redirect('/')


