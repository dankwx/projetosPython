import discord

client = discord.Client()


@client.event
async def on_ready():
    print("Bot pronto para uso!")
    await client.change_presence(game=discord.Game(name="Criando um bot"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
        await client.send_message(message.channel, "World")

client.run(OTY2NTk0MjU0NDM0NjAzMDQ4.YmEBDA.z39uuSN4yUqkwfK7hZMvwySt7LI)

