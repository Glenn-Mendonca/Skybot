#-----------------GAME CODE-----------------#
import discord

BLANK="_"

arr = [[BLANK,BLANK,BLANK,BLANK,BLANK,BLANK,BLANK],
       [BLANK,BLANK,BLANK,BLANK,BLANK,BLANK,BLANK],
       [BLANK,BLANK,BLANK,BLANK,BLANK,BLANK,BLANK],
       [BLANK,BLANK,BLANK,BLANK,BLANK,BLANK,BLANK],
       [BLANK,BLANK,BLANK,BLANK,BLANK,BLANK,BLANK],
       [BLANK,BLANK,BLANK,BLANK,BLANK,BLANK,BLANK]]
chance= ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣","❗"]

async def intro(ctx,bot,p1,p2):
    player1=p1
    player2=p2
    token=[]
    embed=discord.Embed(
        title="Welcome to Connect-4",
        description=f"Token Distribution:\nPlayer 1: {player1.name}\nPlayer 2: {player2.name}\nReact with your character token"
        )

    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)
    token.append(await getChar(ctx, bot,player1))
    token.append(await getChar(ctx, bot,player2))

    await ctx.channel.send(f"{player1.name} {token[0]}\n{player2.name} {token[1]}")

async def getChar(ctx,bot,p):

    def checkReact(reaction, user):
        return user!=bot.user and str(reaction.emoji) != ':white_large_square:'

    reaction,user=await bot.wait_for("reaction_add",timeout=30, check=checkReact)
    users = await reaction.users().flatten()   
    if p in users:
        return str(reaction.emoji)


def drawGrid(arr):
    current=""
    bigLength=len(arr)
    smallLength=len(arr[1])

    for x in range(bigLength):
        for y in range (smallLength):
            if arr[x][y]==BLANK:
                current=current+':white_large_square:'
            elif arr[x][y]==token[0]:
                current=current+token[0]
            elif arr[x][y]==token[1]:
                current=current+token[1]
        current+="\n"
    return current


def insert(arr):
    while(True):
        y = int(input('Enter column number: '))
        y -= 1
        if(y<0 or y>6 or arr[0][y]!=BLANK):
            ctx.channel.send('! Invalid Input !\n')
        else: 
            break
    col = 6
    while(col):
        if(arr[col-1][y]==BLANK):
            arr[col-1][y] = token
            break
        col -= 1

async def connect4(ctx,bot):
    currentPlayer=1
    ctx.channel.send('Player ',tok.index(token)+1,'\'s chance.')
    return
#-----------------GAME CODE-----------------#
