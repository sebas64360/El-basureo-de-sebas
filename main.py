import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$Que es la contaminacion?'):
        await message.channel.send("La contaminacion es cuando ciertas sustancias peligrosas, dañan el medio ambiente")
    elif message.content.startswith('$Como evitarlo?'):
        await message.channel.send("Usar el transporte publico, Recyclar, Reducir el consumo de evitarlos")
    elif message.content.startswith('$Cuales son los quimicos que son usados para la contaminacion'):
        await message.channel.send("Pesticiadas, Talio, Cianuro, Carbonatos, Organofosforado")
    elif message.content.startswith('$Desde cuando los humanos contaminan la tierra'):
        await message.channel.send("Desde 5.600 años")
    else:
        await message.channel.send(message.content)

client.run("TOKEN AQUI")