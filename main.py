import discord
from discord.ext import commands
import os
import keep_alive

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!',intents=intents)

@client.event
async def on_ready():
		await client.change_presence(status=discord.Status.offline)
print("IMMM READY")

@client.command()
async def dm_all(ctx, *, args=None):
	if args != None:
		members = ctx.guild.members
		for member in members:
			try:
				await member.send(args)
			except:
					print("DIDNT WORK YOU DUMBASS")
	else:
		await ctx.send(args)


keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))