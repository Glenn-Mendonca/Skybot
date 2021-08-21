#-----------------GAME CODE-----------------#
import discord

count=42
players=[]
tok = ''
token = []




arr = [[':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:'],
       [':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:'],
       [':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:'],
       [':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:'],
       [':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:'],
       [':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:',':white_large_square:']]

reactMoji= ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣"]

async def intro(ctx,bot,p1,p2):
    token=[]
    players.append(p1)
    players.append(p2)
    embed=discord.Embed(
        title="Welcome to Connect-4",
        description=f"Token Distribution:\nPlayer 1: {players[0].name}\nPlayer 2: {players[1].name}\nReact with your character token"
        )

    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)
    token.append(await getChar(ctx, bot,players[0]))
    token.append(await getChar(ctx, bot,players[1]))

    await ctx.channel.send(f"{players[0].name} {token[0]}\n{players[1].name} {token[1]}")
    return token

async def getChar(ctx,bot,p):

    def checkReact(reaction, user):
        return user!=bot.user and str(reaction.emoji) != ':white_large_square:'

    reaction,user=await bot.wait_for("reaction_add",timeout=30, check=checkReact)
    users = await reaction.users().flatten()   
    if p in users:
        return str(reaction)


def drawGrid(arr):
    current=''

    for x in range(6):
        for y in range(7):
            #if arr[x][y]==':white_large_square:':
            current += arr[x][y]
            # #elif arr[x][y]==token[0]:
            #     #current=current+token[0]
            # elif arr[x][y]==token[1]:
            #     current=current+token[1]
        current+="\n"
    return current

async def getMoves(ctx,bot):
    def checker(reaction,user):
        return (user !=bot.user and (str(reaction.emoji)=="1️⃣" or str(reaction.emoji)=="2️⃣" or str(reaction.emoji)=="3️⃣" or str(reaction.emoji)=="4️⃣" or str(reaction.emoji)=="5️⃣" or str(reaction.emoji)=="6️⃣" or str(reaction.emoji)=="7️⃣"))
    reaction,user=await bot.wait_for("reaction_add",timeout=30,check=checker)
    if (str(reaction) in reactMoji) and user==players[count%2]:
        return int(reactMoji.index(str(reaction)))


async def insert(arr,y,ctx):
    print(type(y))
    while(True):
        if(y<0 or y>6 or arr[0][y]!=':white_large_square:'):
            ctx.channel.send('! Invalid Input !\n')
        else: 
            break
    col = 6
    while(col):
        if(arr[col-1][y]==':white_large_square:'):
            arr[col-1][y] = tok
            break
        col -= 1
#---------------WINNING CHECKS----------------#
def hCheck(tok):
    for i in range(6):
        count = 0
        for j in range(7):
            if(arr[i][j]==tok): count += 1
            else: count = 0
            if(count==4): return tok
    return 0
def vCheck(tok):
    for i in range(7):
        count = 0
        for j in range(6):
            if(arr[j][i]==tok): count += 1
            else: count = 0
            if(count==4): return tok
    return 0
def majdCheck(tok):
    for i in range(3):
        for j in range(4):
            count,len = 0,4
            while(len):
                if(arr[i+len-1][j+len-1]==tok): count += 1
                else: count = 0
                len -= 1
            if(count==4): return tok
    return 0
def mindCheck(token):
    for i in range(3):
        for j in range(3,7):
            count,len = 0,4
            while(len):
                if(arr[i+len-1][j-len+1]==tok): count += 1
                else: count = 0
                len -= 1
            if(count==4): return tok
    return 0
#---------------WINNING CHECKS----------------#


async def connect4game(ctx,bot,mem):
    token = await intro(ctx,bot,ctx.author,mem)
    count = 42
    tok=token[count%2]
    while(count):
        print(count)
        tok = token[count%2]

        board=discord.Embed(
            title=f"Connect-4\n{ctx.author.name} vs {mem.name}",
            description=f"{drawGrid(arr)}\n{players[count%2]}\'s chance."
            )
        msg =await ctx.send(embed=board)

        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        await msg.add_reaction("3️⃣")
        await msg.add_reaction("4️⃣")
        await msg.add_reaction("5️⃣")
        await msg.add_reaction("6️⃣")
        await msg.add_reaction("7️⃣")

        move=int(await getMoves(ctx,bot))
        print(type(move))      
        await insert(arr,move,ctx)
        if(hCheck(token) or vCheck(token) or majdCheck(token) or mindCheck(token)):
            if tok==token[0]:
                board=discord.Embed(
                title=f"Connect-4\n{ctx.author.name} vs {mem.name}",
                description=f"{drawGrid(arr)}\n{players[0].name}has won the game."
                )
            if tok==token[1]:
                board=discord.Embed(
                title=f"Connect-4\n{ctx.author.name} vs {mem.name}",
                description=f"{drawGrid(arr)}\n{players[1].name}has won the game."
                )
        count-=1

    if(count==0):
        await ctx.channel.send('It was a Draw. LOL!\nBoth of you lost.\n')

#-----------------GAME CODE-----------------#
