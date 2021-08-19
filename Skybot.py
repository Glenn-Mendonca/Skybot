import discord
import os
import requests
import json
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
bot=commands.Bot(command_prefix=",")

f=open("help.txt","r")
help=f.readlines()


def get_quote():
    response=requests.get("https://zenquotes.io/api/random")
    jd=json.loads(response.text)
    quote=jd[0]['q']
    return quote


#-----------------GAME CODE-----------------#
arr = [[':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:'],
       [':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:'],
       [':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:'],
       [':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:'],
       [':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:'],
       [':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:',':black_large_square:']]


def intro(p1,p2):
    tp=f"""```
    Welcome to Connect-4
    Token Distribution:
    Player 1: {str(p1).partition('#')[0]}
    Player 2: {str(p2).partition('#')[0]}
    ```"""
    return tp


def drawGrid(arr):
    dG=
    for i in range(1,8):
        f"""
        {i}'\n'+('--'*7)
        ```"""
    for i in range(6):
        {for j in range(7):}
            "{arr[i][j],end=' '}"
        ```"""

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


@bot.event
async def on_ready():
    print('I am ready as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author==bot.user:
        return

    if message.content.startswith("hey" or "hello") and message.author!=bot:
        await message.channel.send('Hello Sir')

    if message.content.startswith('inspire'):
        await message.channel.send(get_quote())

    if message.content.startswith('help'):
        await message.channel.send(str(help[0]))
    await bot.process_commands(message)

@bot.command()
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit=amount)

@bot.command(aliases=['p'])
async def play(ctx,mem:discord.Member):
     await ctx.send(intro(ctx.author,mem))
     await ctx.send(drawGrid(arr))





bot.run(os.environ['token'])

#def play():
#     grids = [[0]*n for _ in range(n)]
#     user = 1
#     print('Current board:')
#     print(*grids, sep='\n')
#     while True:
#         user_input = get_input(user, grids, n)
#         place_piece(user_input, user, grids)
#         print('Current board:')
#         print(*grids, sep='\n')

#         if (check_won(grids, user, n) or
#                 check_won(zip(*grids), user, n) or
#                 diagcheck_won(grids, user, n) or
#                 diagcheck_won(grids[::-1], user, n)):
#             print('Player', user, 'has won')
#             return

#         if not any(0 in grid for grid in grids):
#             return

#         user = 2 if user == 1 else 1


# def get_input(user, grids, n):
#     instr = 'Input a slot player {0} from 1 to 7: '.format(user)
#     while True:
#         try:
#             user_input = int(input(instr))
#         except ValueError:
#             print('invalid input:', user_input)
#             continue
#         if 0 > user_input or user_input > n+1:
#             print('invalid input:', user_input)
#         elif grids[0][user_input-1] != 0:
#             print('slot', user_input, 'is full try again')
#         else:
#             return user_input-1


# def place_piece(user_input, user, grids):
#     for grid in grids[::-1]:
#         if not grid[user_input]:
#             grid[user_input] = user
#             return

# def check_won(grids, user, n):
#     return any(all(cell == user for cell in grid) for grid in grids)


# def diagcheck_won(grids, user, n):
#     return all(grids[x][x] == user for x in range(n))
