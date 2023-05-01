import random, bot

log = []
kys =   '⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠄⠄⠄⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n'\
        '⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⢀⣀⣀⣀⡀⠄⢀⣠⡔⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n' \
        '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣰⢿⣿⣿⣿⣿⣿⣿⣷⡆⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n' \
        '⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣻⣟⣿⣿⡿⣟⣛⣿⡃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n' \
        '⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣾⣿⣷⣿⣷⣿⣿⣿⣷⣽⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿\n' \
        '⣿⣿⣿⣿⣿⣿⣿⣿⡟⣟⣿⣿⠺⣟⣻⣿⣿⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n' \
        '⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡝⠻⠵⠿⠿⢿⣿⣿⢳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n' \
        '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣧⠈⣛⣛⣿⣿⡿⣡⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n' \
        '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠄⠙⠛⠛⢁⣴⣿⣿⣷⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿\n' \
        '⣿⣿⣿⣿⣿⣿⡿⠟⠉⠄⠄⢠⠄⣀⣠⣾⣿⣿⡿⠟⠁⠄⠈⠛⢿⣿⣿⣿⣿⣿\n' \
        '⣿⣿⣿⣿⡟⠉⠄⠄⢀⠠⠐⠒⠐⠾⠿⢟⠋⠁⠄⢀⣀⠠⠐⠄⠂⠈⠻⢿⣿⣿\n' \
        '⣿⣿⣿⠋⠁⠄⢀⡈⠄⠄⠄⠄⠄⠄⠄⠄⠁⠒⠉⠄⢠⣶⠄⠄⠄⠄⠄⠈⠫⢿\n' \
        '⣿⣿⡟⠄⢔⠆⡀⠄⠈⢀⠄⠄⠄⠄⠄⠄⠄⢄⡀⠄⠈⡐⢠⠒⠄⠄⠄⠄⢀⣂\n' \
        '⣿⣿⠁⡀⠄⠄⢇⠄⠄⢈⠆⠄⠄⢀⠔⠉⠁⠉⠉⠣⣖⠉⡂⡔⠂⠄⢀⠔⠁⠄\n' \
        '⣿⡿⠄⠄⠄⠄⢰⠹⣗⣺⠤⠄⠰⡎⠄⠄⠄⠄⠄⠄⠘⢯⡶⢟⡠⠰⠄⠄⠄⠄' \

def saveAdmins(toSave):
    toLog = ''
    for admin in toSave:
        toLog += admin + ','
    newLog = ''
    for admin in toLog.split(','):
        if admin != '':
            newLog += admin + ','
    with open('.log Files/Admins.log', 'w') as fh:
        fh.write(newLog[:len(newLog) - 1])


def handle_response(message, username, guild, userID, isBot) -> str:
    with open('.log Files/Admins.log', 'r') as fh:
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
                with open('.log Files/LoggedMSGs.csv', 'r') as fh:
                    toWrite = fh.read() + '\n' + logHandle
                with open('.log Files/LoggedMSGs.csv', 'w') as fh:
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
                               "\n  - !amiabot >> It tells you if your a bot"
                    case '!lowtiergod':
                        return 'you should kys NOW\n' + kys
                    case '!giveroll':
                        return 'WORK IN PROGRESS'
                    case '!amiabot':
                        if isBot or username == 'clcskylands#1674':
                            return 'You are a bot! Beep Boop?'
                        else:
                            return 'You are indeed not a bot'
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
                                with open('.log Files/Channels.log', 'w') as fh:
                                    newLog = ''
                                    toLog = str(bot.channels).replace(']', '').replace('[', '').replace('"', '').replace("'",'').replace(', ', ',').replace(' ', '>>>')
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
                                    except:
                                        return 'THIS CHANNEL WAS ALREADY REMOVED'
                                    with open('.log Files/Channels.log', 'w') as fh:
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

        except UnicodeEncodeError:
            return None
    except Exception as e:
        return "THERE HAS BEEN A CRITICAL ERROR" \
               "\nPLEASE DM @WhaleYogurt AND SEND HIM THE FOLLOWING ERROR CODE" \
               "\n" + str(e)