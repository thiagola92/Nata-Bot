from bot_info import BOT
from bot_info import USERNAME
from bot_info import TOKEN

# Bot commands
import bot_default
import bot_list
import bot_random
import bot_overwatch

# Others
import time

@BOT.event
async def on_ready():
    print("======================================")
    print("Bot is ready")
    
    for channel in BOT.get_all_channels():
        print(str(channel))
    
@BOT.event
async def on_message(message):
    print("======================================")
    print("Message received")
    
    user = str(message.author)
    
    if user == USERNAME:
        pass
    elif message.content.find("enfia no cu") != -1:
        await BOT.send_message(message.channel, "Isso meu garoto")
    elif message.content.find("13") != -1:
        await BOT.send_message(message.channel, "É 13 MEMO CARAIO")
        
    await BOT.process_commands(message)

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