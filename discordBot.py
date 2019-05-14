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
    
@client.command()
async def users(ctx):
    id = client.get_guild('Server ID here')
    await ctx.send(f'Number of users: {id.member_count}')


#8ball with alias. Using 4 random answers
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['yes', 'no', 'maybe', 'u wish']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#clear messages
@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

#Kick user
@client.command()
async def kick(ctx, member : discord.Member=None, *, reason =None):
    if not member:
        await ctx.send('Specify a member')
        return
   # await member.kick(reason=reason)
    await ctx.send(f'{member.mention} was kicked')

#ban user
@client.command()
async def ban(ctx, member : discord.Member=None, *, reason =None):
    if not member:
        await ctx.send('Specify a member')
        return
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} was banned')

#mute user
@client.command()
async def mute(ctx, member : discord.Member=None, *, reason =None):
    #Role name and priviledges must be set up in the server.
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    if not member:
        await ctx.send('Specify a member')
        return
    await member.add_roles(role)
    await ctx.send(f'{member.mention} was muted')


#unmute user
@client.command()
async def unmute(ctx, member : discord.Member=None, *, reason =None):
    #Role name and priviledges must be set up in the server.
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    if not member:
        await ctx.send('Specify a member')
        return
    await member.remove_roles(role)
    await ctx.send(f'{member.mention} was unmuted')

    


##################################################
##################################################
#https://discord.gg/rxxspN
    
#client token here
client.run('token here')

