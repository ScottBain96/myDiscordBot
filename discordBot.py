import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = '?')



#startbot
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


#member joins server event
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

#member leaves server
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')


######Commands####################################
##################################################
   
#check ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping is {round (client.latency * 1000)} ms')
    

#8ball with alias. Using 4 random answers
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['yes', 'no', 'maybe', 'u wish']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#clear messages
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

#Kick user
@client.command()
async def kick(ctx, member : discord.Member, *, reason =None):
    await member.kick(reason=reason)

#ban user
@client.command()
async def ban(ctx, member : discord.Member, *, reason =None):
    await member.ban(reason=reason)


##################################################
##################################################

    
#client token here
client.run('MYTOKEN HERE')

