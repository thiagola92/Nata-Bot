from info import BOT
from info import USERNAME
from info import TOKEN

# Bot commands
import bot_default
import bot_list
import bot_random
import bot_overwatch
import bot_player

# Others
import time

@BOT.event
async def on_ready():
    print("======================================")
    print("Bot is ready")
    
@BOT.event
async def on_message(message):
    print("======================================")
    print("Message received")
    
    user = str(message.author)
    content = message.content.lower()
    
    if user == USERNAME:
        pass
    elif find_quote(content, ["13"]):
        await BOT.send_message(message.channel, "É 13 MEMO CARAIO")
    elif find_quote(content, ["amor"]):
        await BOT.send_message(message.channel, "Só só só só amor faz o mundo andar")
    elif find_quote(content, ["enfia no cu", "enfiar no cu"]):
        await BOT.send_message(message.channel, "Isso meu garoto")
        
    await BOT.process_commands(message)
    
def find_quote(message, quotes):

    for quote in quotes:
        if message.find(quote) != -1:
            return True
            
    return False

@BOT.event
async def on_message_delete(message):
    print("======================================")
    print("Message deleted")
    
    try:
        file_name = "historic//" + time.strftime("%Y %m %d")
        file = open(file_name, "a")
        
        file.write("Server: " + message.server.name + "\n")
        file.write("Channel: " + message.channel.name + "\n")
        file.write("Attachments: " + str(message.attachments) + "\n")
        file.write("Author: " + message.author.name + "\n")
        file.write("Content: " + message.content + "\n")
        file.write("======================================\n")
        
    except Exception as e:
        await BOT.say("```{}``` \n Hey newbie! Use **!help COMMAND** to learn more about it".format(e))

@BOT.command()
async def hello():
    print("======================================")
    print("Command hello")
    
    await BOT.say("Hello World!")



BOT.run(TOKEN)