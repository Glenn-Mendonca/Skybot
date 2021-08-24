#-----------------GAME CODE-----------------#
import discord

class connect_4:
    reactMoji= ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣"]
    def __init__(self,ctx,bot,mem):
        self.ctx = ctx
        self.bot = bot
        self.players = [ctx.author,mem]
        self.token = []
        self.count = 42
        wb = ':white_large_square:'
        self.arr = [[wb,wb,wb,wb,wb,wb,wb],
                    [wb,wb,wb,wb,wb,wb,wb],
                    [wb,wb,wb,wb,wb,wb,wb],
                    [wb,wb,wb,wb,wb,wb,wb],
                    [wb,wb,wb,wb,wb,wb,wb],
                    [wb,wb,wb,wb,wb,wb,wb]] 

    async def getChar(self,p):
        def checkReact(reaction, user):
            return user != self.bot.user and p==user and str(reaction.emoji) != ':white_large_square:'
        reaction,_ = await self.bot.wait_for("reaction_add",timeout=30, check=checkReact)
        return str(reaction.emoji)

    async def intro(self):
        embed=discord.Embed(
        title="Welcome to Connect-4",
        description=f"Token Distribution:\nPlayer 1: {self.players[0].name}\nPlayer 2: {self.players[1].name}\nReact with your character token"
        )
        await self.ctx.channel.purge(limit=1)
        await self.ctx.send(embed=embed)
        for i in range(2):
            self.token.append(await self.getChar(self.players[i]))
        await self.ctx.channel.send(f"{self.players[0].name} {self.token[0]}\n{self.players[1].name} {self.token[1]}")
        return self.token

    def drawGrid(self):
        current=''
        for x in range(6):
            for y in range(7):
                current += self.arr[x][y]
            current+="\n"
        return current

    async def getMoves(self):
        def checker(reaction,user):
            return (user != self.bot.user and (str(reaction.emoji) in self.reactMoji) and (user == self.players[self.count%2]))
        reaction,user= await self.bot.wait_for("reaction_add",timeout=30,check=checker)
        return int(self.reactMoji.index(str(reaction)))

    async def insert(self,y,tok):
        while(True):
            if(y<0 or y>6 or self.arr[0][y]!=':white_large_square:'):
                await self.ctx.channel.send('! Invalid Input !\n')
                await self.getMoves()
            else: 
                break
        col = 6
        while(col):
            if(self.arr[col-1][y]==':white_large_square:'):
                self.arr[col-1][y] = tok
                break
            col -= 1

    def hCheck(self,tok):
        for i in range(6):
            count = 0
            for j in range(7):
                if(self.arr[i][j]==tok): count += 1
                else: count = 0
                if(count==4): return 1
        return 0

    def vCheck(self,tok):
        for i in range(7):
            count = 0
            for j in range(6):
                if(self.arr[j][i]==tok): count += 1
                else: count = 0
                if(count==4): return 1
        return 0

    def majdCheck(self,tok):
        for i in range(3):
            for j in range(4):
                count,len = 0,4
                while(len):
                    if(self.arr[i+len-1][j+len-1]==tok): count += 1
                    else: count = 0
                    len -= 1
                if(count==4): return 1
        return 0

    def mindCheck(self,tok):
        for i in range(3):
            for j in range(3,7):
                count,len = 0,4
                while(len):
                    if(self.arr[i+len-1][j-len+1]==tok): count += 1
                    else: count = 0
                    len -= 1
                if(count==4): return 1
        return 0
        
    async def connect4game(self):
        self.token = await self.intro()
        while(self.count):
            tok = self.token[self.count%2]
            board = discord.Embed(
                title=f"Connect-4\n{self.players[0].name} vs {self.players[1].name}",
                description=f"{self.drawGrid()}\n{self.players[self.count%2]}\'s chance."
                )
            msg =await self.ctx.send(embed=board)
            await msg.add_reaction("1️⃣")
            await msg.add_reaction("2️⃣")
            await msg.add_reaction("3️⃣")
            await msg.add_reaction("4️⃣")
            await msg.add_reaction("5️⃣")
            await msg.add_reaction("6️⃣")
            await msg.add_reaction("7️⃣")

            move= await self.getMoves()     
            await self.insert(move,tok)
            if(self.hCheck(tok) or self.vCheck(tok) or self.majdCheck(tok) or self.mindCheck(tok)):
                board=discord.Embed(
                title=f"Connect-4\n{self.players[0].name} vs {self.players[1].name}",
                description=f"{self.drawGrid()}\n{self.players[self.token.index(tok)].name} has won the game."
                )
                msg = await self.ctx.send(embed = board)
                break
            self.count-=1

        if(self.count==0):
            await self.ctx.channel.send('It was a Draw. LOL!\nBoth of you lost.\n')

    #-----------------GAME CODE-----------------#
