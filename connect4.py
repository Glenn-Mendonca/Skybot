#-----------------GAME CODE-----------------#
import discord


def intro(p1,p2):
    tp=f"""```
    Welcome to Connect-4
    Token Distribution:
    Player 1: {str(p1).partition('#')[0]}
    Player 2: {str(p2).partition('#')[0]}
    ```"""
    return tp

def drawGrid(arr):
    _ = ''
    for i in range(1,8):
        _ += str(i) + ' '
        _ += '\n' + ('--'*7) + '\n'
        for i in range(6):
            for j in range(7):
                _ += arr[i][j] + ' '
            _ += '\n' 
    return _


def insert(arr):
    while(True):
        y = int(input('Enter column number: '))
        y -= 1
        if(y<0 or y>6 or arr[0][y]!=':black_large_square:'):
            ctx.channel.send('! Invalid Input !\n')
        else: 
            break
    col = 6
    while(col):
        if(arr[col-1][y]==':black_large_square:'):
            arr[col-1][y] = token
            break
        col -= 1

#-----------------GAME CODE-----------------#