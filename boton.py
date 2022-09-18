from discord.ext import commands
# various imports ^

client = commands.Bot(command_prefix=">") # defining the bot's prefix

@client.event #on_ready event --> printing "The bot is online" when the bot goes online
async def on_ready():
    print("The bot is online")

@client.command() # telling to the client that this is a command
async def ping(ctx): # defining the commmand's name and its parameters
    await ctx.send("Pong!") # sending the reply

@client.command()
async def annuncio(ctx, *, testo: str):
    await ctx.send(testo)

    client.run("")
