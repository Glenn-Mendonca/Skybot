#Dependencies
from os import system,name

#Functions
def intro():
    print('Welcome to Connect-4')
    print('Token Distribution: ')
    print('Player 1: ',tok[0])
    print('Player 2: ',tok[1])
def drawGrid(arr):
    for i in range(1,8):
        print(i,end=' ')
    print('\n'+('--'*7))
    for i in range(6):
        for j in range(7):
            print(arr[i][j],end=' ')
        print()      
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
def hCheck(token):
    for i in range(6):
        count = 0
        for j in range(7):
            if(arr[i][j]==token): count += 1
            else: count = 0
            if(count==4): return token
    return 0
def vCheck(token):
    for i in range(7):
        count = 0
        for j in range(6):
            if(arr[j][i]==token): count += 1
            else: count = 0
            if(count==4): return token
    return 0
def majdCheck(token):
    for i in range(3):
        for j in range(4):
            count,len = 0,4
            while(len):
                if(arr[i+len-1][j+len-1]==token): count += 1
                else: count = 0
                len -= 1
            if(count==4): return token
    return 0
def mindCheck(token):
    for i in range(3):
        for j in range(3,7):
            count,len = 0,4
            while(len):
                if(arr[i+len-1][j-len+1]==token): count += 1
                else: count = 0
                len -= 1
            if(count==4): return token
    return 0

#Main Program
arr = [[':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:'],
       [':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:'],
       [':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:'],
       [':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:'],
       [':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:'],
       [':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:']]
tok = ['#','$']
count  = 42
intro()

#Game Loop
async def play():
    while(count):
        clear()
        token = tok[count%2]
        drawGrid(arr)
        ctx.channel.send('Player ',tok.index(token)+1,'\'s chance.')
        insert(arr)
        if(hCheck(token) or vCheck(token) or majdCheck(token) or mindCheck(token)):
            drawGrid(arr)
            ctx.channel.send('Player ',tok.index(token)+1,' is the Winner \U0001F973\U0001F389')
            break
        count -= 1
    if(count==0):
        ctx.channel.send('It was a Draw. LOL!\nBoth of you lost.\n')