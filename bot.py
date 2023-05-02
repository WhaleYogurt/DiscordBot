import discord
import responses

with open('logFiles/Channels.log', 'r', encoding='cp1252') as fh:
    channels = fh.read().split("\n")[0].replace(' ', '').split(':')[1].replace('>>>', ' ').split(',')

async def send_message(message, is_private, toSendBack):
    try:
        if toSendBack is not None and toSendBack is not Exception:
            await message.author.send(toSendBack) if is_private else await message.channel.send(toSendBack)
    except Exception as e:
        print(e)

def run_discord_bot():
    # Bot settings
    TOKEN = input("ENTER KEY << ")
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # Boot message
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    # Message Event Handler
    @client.event
    async def on_message(message):
        try:
            with open('logFiles/Channels.log', 'r', encoding='cp1252') as fh:
                raw = fh.read()

            if message.author == client.user:
                return

            # Data about message
            username = str(message.author)
            userID = str(message.author.id)
            guild = str(message.guild.name)
            user_message = str(message.content)
            channel = str(message.channel.name)
            isBot = bool(message.author.bot)

            if user_message[0] == '?': # Is this a private message?
                user_message = user_message[1:]
                response = responses.handle_response(message=user_message, username=username, guild=guild, userID=userID, isBot=isBot)
                await send_message(message=message, is_private=True, toSendBack=response)
            else:
                # Am I allowed to use this channel?
                isGoodChannel = False
                for chan in channels:
                    if channel == chan:
                        isGoodChannel = True
                if isGoodChannel:
                    response = responses.handle_response(message=user_message, username=username, guild=guild, userID=userID, isBot=isBot)
                    await send_message(message=message, is_private=False, toSendBack=response)
        except IndexError:
            pass

    client.run(TOKEN)
