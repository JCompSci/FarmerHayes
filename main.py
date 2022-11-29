import discord
import math
import random
from discord.ext import commands

class hayes:
    def __init__(self):
        
        productFile = open("productChoice.txt", "r")
        self.item = []
        for line in productFile:
            self.item.append(line.strip())
        
        
        flavorFile = open("FlavorChoice.txt", "r")
        self.flavor = []
        for line in flavorFile:
            self.flavor.append(line.strip())
        
        
        promptFile = open("PromptFormat.txt", "r")
        self.prompt = []
        for line in promptFile:
            self.prompt.append(line.strip())
            
        adjectiveFile = open("adjectives.txt", "r")
        self.adjectiveList = []
        for line in adjectiveFile:
            self.adjectiveList.append(line.strip())

    def newFood(self):
            
        flavor1 = self.adjectiveList[random.randint(0,len(self.adjectiveList)-1)]
        flavor2 = self.flavor[random.randint(0,len(self.flavor)-1)]
        prompt1 = self.prompt[random.randint(0,len(self.prompt)-1)]
        product1 = self.item[random.randint(0,len(self.item)-1)]
    
        flavor1Loc = prompt1.find("<flavor1>")
        flavor2Loc = prompt1.find("<flavor2>")
        productLoc = prompt1.find("<product>")
    
        result = prompt1[0:flavor1Loc] + flavor1 + " " + flavor2 + prompt1[flavor2Loc+9: productLoc] + product1 + prompt1[productLoc+9]
        return result
    



##BREAK     
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = ".", intents = intents)


badWordFile = open("badWords.txt", "r")
shameful_words = []
for line in badWordFile:
    shameful_words.append(line.strip())
    
responseFile = open("Responses.txt", "r")
responseList = []
for line in responseFile:
    responseList.append(line.strip())

@client.event
async def on_ready():
    print('Bot is ready.')
    
hay = hayes()

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return 
    for str in shameful_words:
        if str in message.content.lower():
            response = responseList[random.randint(0,len(responseList)-1)]
            await message.channel.send(response)

@client.command()
async def hayes(ctx):
    await ctx.send(hay.newFood())
    await ctx.message.delete()

@client.command()
async def message(ctx):
    await ctx.message.delete()
    off = True
    while off:
        text = input()
        if text == "terminate":
            off = False
        elif text == ".hayes":
            await ctx.send(hay.newFood())
        else:
            await ctx.send(text)

#client.run( insert Token Here)
