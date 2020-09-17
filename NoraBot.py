import discord
from googlesearch import search


TOKEN = open("token.txt", "r").read()

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    word_list = message.content.lower().split()

    if 'luna' in word_list:
        response = 'nora~'
        await message.channel.send(response)
    #if message.content.lower().find('luna') != -1:
    #    response = 'nora~'
    #    await message.channel.send(response)

    if message.content.lower() == 'hi':
        response = 'nora'
        await message.channel.send(response)

    if message.content.lower() == 'na':
        response = 'nora~'
        await message.channel.send(response)

    if message.content.lower() == 'hi norabot':
        response = 'hi nora'
        await message.channel.send(response)

    if message.content.lower() == 'let it be':
        response = 'wallaby~'
        await message.channel.send(response)

    if message.content.lower() == 'google':
        response = 'guguru'
        await message.channel.send(response)

    if message.content.lower() == 'poke':
        response = 'Nnnaaaaaaa'
        await message.channel.send(response)

    if message.content.startswith('!vtuber'):

        if len(message.content.split()) == 1:
            response = "Luna wakaranai noraaaaa~"
            await message.channel.send('Nnnaaaaaaa~')
            await message.channel.send(response)

        else:
            words = []
            #print(message.content.split())
            for word in message.content.split()[1:]:
                print(word)
                words.append(word)

            query = ' '.join(words)
            for webpage in search('vtuber ' + query, tld='com', num=1, stop=1, pause=1):
                await message.channel.send(webpage)
                await message.channel.send('nora~')

    if message.content.startswith('!kc'):

        if len(message.content.split()) == 1:
            response = "Luna wakaranai noraaaaa~"
            await message.channel.send('Nnnaaaaaaa~')
            await message.channel.send(response)

        else:
            words = []

            for word in message.content.split()[1:]:
                words.append(word)

            query = ' '.join(words)
            for webpage in search('kancolle ' + query, tld='com', num=1, stop=1, pause=1):
                await message.channel.send(webpage)
                await message.channel.send('nora~')


    if message.content.startswith('!yt'):

        if len(message.content.split()) == 1:
            response = "Luna wakaranai noraaaaa~"
            await message.channel.send('Nnnaaaaaaa~')
            await message.channel.send(response)

        else:
            words = []

            for word in message.content.split()[1:]:
                words.append(word)

            query = ' '.join(words)


            for webpage in search('youtube ' + query, tld='com', num=1, stop=1, pause=1):
                await message.channel.send(webpage)
                await message.channel.send('nora~')


client.run(TOKEN)
