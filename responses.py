import random, bot, os, pytubeDownloader

log = []
RPS = ['R', 'P', 'S']
userData = []
reactionsSave = [[], []]

def saveAdmins(toSave):
    toLog = ''
    for admin in toSave:
        toLog += admin + ','
    newLog = ''
    for admin in toLog.split(','):
        if admin != '':
            newLog += admin + ','
    with open('logFiles/Admins.log', 'w', encoding='cp1252') as fh:
        fh.write(newLog[:len(newLog) - 1])

def newReaction(name, url):
    with open('logFiles/reactions.log', 'r') as fh:
        previous = fh.read()
    reactions = previous.split("\n")
    Found = False
    for reaction in reactions:
        if reaction != '':
            reactionsSave[0].append(reaction.split(': ')[0])
            reactionsSave[1].append(reaction.split(': ')[1])
            if reaction.split(': ')[0] == name:
                Found = True
    if not Found:
        with open('logFiles/reactions.log', 'w') as fh:
            fh.write(previous + f'\n{name}: {url}')

def loadReactions():
    reactionsSave = [[], []]
    with open('logFiles/reactions.log', 'r') as fh:
        raw = fh.read()
    reactions = raw.split('\n')
    for reaction in reactions:
        if reaction != '':
            reactionsSave[0].append(reaction.split(': ')[0])
            reactionsSave[1].append(reaction.split(': ')[1])
    return reactionsSave

loadReactions()

def handle_response(message, username, guild, userID, isBot, messageHandle) -> str:
    with open('logFiles/Admins.log', 'r', encoding='cp1252') as fh:
        admins = fh.read().replace("'", "").split(',')
    isLogging = 'TRUE'
    isAdmin = False
    for admin in admins:
        if username == admin:
            isAdmin = True

    # Tells the user that they are not an admin if they attempt to use and admin command without permission
    if message[0] == '>' and isAdmin is False and len(message) > 1:
        return 'YOU ARE NOT AN ADMIN'
    try:
        try:
            logHandle = f'{message}, {username}'
            log.append(logHandle)
            p_message = message.lower()
            if isLogging == 'TRUE':
                with open('logFiles/LoggedMSGs.csv', 'r', encoding='cp1252') as fh:
                    toWrite = fh.read() + '\n' + logHandle
                with open('logFiles/LoggedMSGs.csv', 'w', encoding='cp1252') as fh:
                    fh.write(toWrite)
            chunks = p_message.split(' ')
            if message[0] == '!':
                match chunks[0]:
                    case '!hello':
                        return f'Hello <@{userID}> !'
                    case '!roll':
                        if len(chunks) > 1:
                            return f"You Rolled [{str(random.randint(1, int(chunks[1])))}] :game_die:"
                        else:
                            return f"You Rolled [{str(random.randint(1, 6))}] :game_die:"
                    case '!rick':
                        return "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                    case "!help":
                        return "COMMANDS:" \
                               "\n  - !hello >> Just says hello back" \
                               "\n  - !roll {max number} >> Gives a random number from 1 to your other input" \
                               "\n  - !help >> Just gives you the current commands" \
                               "\n  - !rick >> ..." \
                               "\n  - !amiabot >> It tells you if your a bot" \
                               "\n  - !rps >> starts a game of rock, paper, scissors" \
                               "\n  - !whale >> returns my logo!" \
                               "\n  - !whaleyogurt >> returns my logo!" \
                               "\n  - !test >> returns my logo!"
                    case '!lowtiergod':
                        return 'You serve no purpose!\n' + open('BrailArt/lowtiergod.brail', 'r', encoding='utf-8').read()
                    case '!giveroll':
                        return 'WORK IN PROGRESS'
                    case '!amiabot':
                        if isBot or username == 'clcskylands#1674':
                            return 'You are a bot! Beep Boop?'
                        else:
                            return 'You are indeed not a bot'
                    case '!rps':
                        if not bot.rpsModeOn:
                            bot.rpsModeOn = True
                            bot.rpsPlayer = username
                            return 'So you wanna play? You bet! Just respond with !R, !P, or !S.'
                    case '!r':
                        if bot.rpsModeOn and username == bot.rpsPlayer:
                            RPSresponse = RPS[random.randint(0, 2)].lower()
                            bot.rpsModeOn = False
                            bot.rpsPlayer = ''
                            if RPSresponse == 'r':
                                return ':rock:Tie! Try again!:rock:'
                            elif RPSresponse == 'p':
                                return ':scroll:I win! It seems like you have a skill issue.:scroll:'
                            elif RPSresponse == 's':
                                return ':scissors:I lose... Too bad:scissors:'
                    case '!p':
                        if bot.rpsModeOn and username == bot.rpsPlayer:
                            RPSresponse = RPS[random.randint(0, 2)].lower()
                            bot.rpsModeOn = False
                            bot.rpsPlayer = ''
                            if RPSresponse == 'r':
                                return ':rock:I lose... Too bad:rock:'
                            elif RPSresponse == 'p':
                                return ':scroll:Tie! Try again!:scroll:'
                            elif RPSresponse == 's':
                                return ':scissors:I win! It seems like you have a skill issue.:scissors:'
                    case '!s':
                        if bot.rpsModeOn and username == bot.rpsPlayer:
                            bot.rpsModeOn = False
                            bot.rpsPlayer = ''
                            RPSresponse = RPS[random.randint(0, 2)].lower()
                            if RPSresponse == 'r':
                                return ':rock:I win! It seems like you have a skill issue.:rock:'
                            elif RPSresponse == 'p':
                                return ':scroll:I lose... Too bad:scroll:'
                            elif RPSresponse == 's':
                                return ':scissors:Tie! Try again!:scissors:'
                            username, bot.rpsModeOn = '', False
                    case '!whale':
                        with open('BrailArt/WhaleYogurt.brail', 'r', encoding='utf-8') as fh:
                            return fh.read()
                    case '!whaleyogurt':
                        with open('BrailArt/WhaleYogurt.brail', 'r', encoding='utf-8') as fh:
                            return fh.read()
                    case '!test':
                        with open('BrailArt/WhaleYogurt.brail', 'r', encoding='utf-8') as fh:
                            return fh.read()
                    case _:
                        return None
            elif message[0] == '>':
                if isAdmin:
                    match chunks[0]:
                        case '>help':
                            return "ADMIN COMMANDS:" \
                                       "\n  - >aList >> returns the current list of admins" \
                                       "\n  - >newAdmin {Username#1111} >> makes a new admin" \
                                       "\n  - >channels >> returns channels that bot can interact with" \
                                       "\n  - >newChannel {channelName} >> adds a channel that the bot can listen and use" \
                                       "\n  - >removeChannel {channelName} >> removes a channel that the bot can listen and use"
                        case '>newadmin':
                            if len(chunks) > 1:
                                for admin in admins:
                                    if admin == message.split(' ')[1]:
                                        return 'THIS USER IS ALREADY AN ADMIN'
                                if len(message.split(' ')[1].split("#")) == 2 and len(
                                        message.split(' ')[1].split("#")) == 4:
                                    admins.append(message.split(' ')[1])
                                else:
                                    return 'PLEASE ADD THE FULL USERNAME\nEX: Username#1010'
                                saveAdmins(admins)
                                return 'NEW ADMIN: ' + message.split(' ')[1]
                            else:
                                return 'ERROR: PLEASE USE A SPACE TO MAKE A NEW ADMIN\n' \
                                       'EX: >newAdmin exampleUser#1010'
                        case '>channels':
                            return str(bot.channels).replace(']', '').replace('[', '').replace('"', '').replace("'", '')
                        case '>alist':
                            return str(admins).replace(']', '').replace('[', '').replace('"', '').replace("'", '')
                        case '>newchannel':
                            if len(chunks) > 1:
                                bot.channels.append(message.split(" ")[1].lower())
                                with open('logFiles/Channels.log', 'w', encoding='cp1252') as fh:
                                    newLog = ''
                                    toLog = str(bot.channels).replace(']', '').replace('[', '').replace('"', '').replace("'", '').replace(', ', ',').replace(' ', '>>>')
                                    for admin in toLog.split(','):
                                        if admin != '':
                                            newLog += admin + ','
                                    newLog = 'channels: ' + newLog
                                    fh.write(newLog[:len(newLog) - 1])
                                return 'NEW CHANNEL: ' + message.split(" ")[1]
                            else:
                                return 'PLEASE ENTER THE CHANNEL WHICH YOU WOULD LIKE TO ADD'
                        case '>removechannel':
                            if isAdmin:
                                if len(chunks) > 1:
                                    try:
                                        bot.channels.remove(chunks[1])
                                    except ValueError:
                                        return 'THIS CHANNEL WAS ALREADY REMOVED'
                                    with open('logFiles/Channels.log', 'w', encoding='cp1252') as fh:
                                        newLog = ''
                                        toLog = str(bot.channels).replace(']', '').replace('[', '').replace('"',
                                                                                                            '').replace("'",
                                                                                                                        '').replace(
                                            ', ', ',').replace(' ', '>>>')
                                        for admin in toLog.split(','):
                                            if admin != '':
                                                newLog += admin + ','
                                        newLog = 'channels: ' + newLog
                                        fh.write(newLog[:len(newLog) - 1])
                                    return 'REMOVED CHANNEL: ' + chunks[1]
                                else:
                                    return 'PLEASE ENTER THE CHANNEL WHICH YOU WOULD LIKE TO REMOVE'
                        case '>>removeadmin':
                            if username == 'WhaleYogurt#1896':
                                newAdmins = []
                                for admin in admins:
                                    if admin != message.split(' ')[1]:
                                        newAdmins.append(admin)
                                saveAdmins(newAdmins)
                                return 'ADMIN REMOVED: ' + message.split(' ')[1]
                            else:
                                return None
                        case _:
                            return None
            elif message[0] == '#':
                match chunks[0]:
                    case '#help':
                        return 'COMMANDS: ' \
                               '\n  - #help >> returns current command list' \
                               "\n  - #taunt >> returns a funni gif of Italy's national bird" \
                               "\n  - #ballin >> returns a picture of Luigi dunkin on u" \
                               "\n  - #yea >> YEAAAAAAAAAAAAAAAAAAAAAAH" \
                               "\n  - #reactions >> gives list of custom reactions" \
                               "\n  - #newReaction [types: url, youtube] [nameOfReaction] {if using youtube enter audioOnly, videoOnly, or both} [reactionUrl] >> Creates a custom reaction!" \
                               "\n  - #reaction or #react [reactionName] >> reaction image"
                    case '#taunt':
                        return 'SEND FILE: Images/Taunt.gif'
                    case '#ballin':
                        return 'SEND FILE: Images/ballin.jpg'
                    case '#counter':
                        return 'SEND FILE: Images/counter.jpg'
                    case '#yea':
                        return 'https://tenor.com/view/kermit-frog-panic-frantic-yay-gif-16814992'
                    case '#newreaction':
                        chunks[3] = message.split(' ')[3]
                        if len(chunks) > 3:
                            if chunks[1] == 'url' and len(chunks) == 4:
                                newReaction(chunks[2], chunks[3])
                                return 'NEW REACTION: ' + chunks[2] + '\n URL >> ' + chunks[3]
                            elif chunks[1] == 'yt' or chunks[1] == 'youtube':
                                name = chunks[2]
                                type = chunks[3]
                                ytLink = chunks[4]
                                match type:
                                    case 'audioonly':
                                        pytubeDownloader.DownloadOnlyAudio(ytLink, name+'.mp4')
                                        newReaction(name, f'SEND FILE: Downloads/{name}.mp4')
                                    case 'videoonly':
                                        pytubeDownloader.DownloadOnlyVideo(ytLink, name+'.mp4')
                                        newReaction(name, f'SEND FILE: Downloads/{name}.mp4')
                                    case 'both':
                                        pytubeDownloader.DownloadVidAndAudio(ytLink, name+'.mp4')
                                        newReaction(name, f'SEND FILE: Downloads/{name}.mp4')
                                return f'SEND FILE: Downloads/{name}.mp4'
                            else:
                                return f'FORMATTING ERROR USE #help\n{chunks}'
                    case '#reaction':
                        reactionsSave = loadReactions()
                        if len(chunks) > 1:
                            i = 0
                            for name in reactionsSave[0]:
                                if chunks[1] == name:
                                    return reactionsSave[1][i]
                                i += 1
                            return 'REACTION NOT FOUND'
                    case '#react':
                        reactionsSave = loadReactions()
                        if len(chunks) > 1:
                            i = 0
                            for name in reactionsSave[0]:
                                if chunks[1] == name:
                                    return reactionsSave[1][i]
                                i += 1
                            return 'REACTION NOT FOUND'
                    case '#reactions':
                        reactionsSave = loadReactions()
                        toReturn = ''
                        i = 0
                        for name in reactionsSave[0]:
                            toReturn += name + ': ' + reactionsSave[1][i] + '\n'
                            i += 1
                        return toReturn
                    case _:
                        reactionsSave = loadReactions()
                        i = 0
                        for name in reactionsSave[0]:
                            if chunks[0] == "#"+name:
                                return reactionsSave[1][i]
                            i += 1
                        return 'THIS COMMANDD DOES NOT EXIST PLEASE USE #help'
        except UnicodeEncodeError:
            return None
    except Exception as e:
        return "THERE HAS BEEN A CRITICAL ERROR" \
               "\nPLEASE DM @WhaleYogurt AND SEND HIM THE FOLLOWING ERROR CODE" \
               "\n" + str(e)
