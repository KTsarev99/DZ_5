# Создайте программу для игры в ""Крестики-нолики""

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def plus_nul(move):
    
    for i,item in enumerate(board):
        if item == move:
            board[i] = 'O'

def plus_krest(move2):

    for g,item in enumerate(board): 
        if item == move2:
         board[g] = 'x'  
    

for i in range(5):
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])
    
    a=int(input("player 1 turns"))   
    print(plus_nul(a))
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])
    if (board[0] == board[4] ==board[8] or board[0]==board[1]==board[2]
    or board[3]==board[4]==board[5] or board[6]==board[7]==board[8]
    or board[0]==board[3]==board[6] or board[1]==board[4]==board[7]
    or board[2]==board[5]==board[8] or board[2]==board[4]==board[6]):
        print("player 1 win")
        break
    
    b=int(input("player 2 turns"))
    print(plus_krest(b))
    if a == b :
        print("same, enter others values")
        b=int(input("player 2 turns"))
    if (board[0] == board[4] ==board[8] or board[0]==board[1]==board[2]
    or board[3]==board[4]==board[5]== 'x' or board[6]==board[7]==board[8]
    or board[0]==board[3]==board[6]== 'x' or board[1]==board[4]==board[7]
    or board[2]==board[5]==board[8]== 'x'or board[2]==board[4]==board[6]):
        print("player 2 win")
        break

print("game over")
