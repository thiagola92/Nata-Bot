from bot_info import BOT
from bot_info import TOKEN

# Bot commands
import bot_default
import bot_list
import bot_random

@BOT.event
async def on_ready():
    print("======================================")
    print("Bot is ready")
    
    for channel in BOT.get_all_channels():
        print(str(channel))
    
@BOT.event
async def on_message_delete(message):
    print("======================================")
    print("Message deleted")
    
    print("Channel: " + message.channel.name)
    print("Author: " + message.author.name)
    print("Content: " + message.content)

@BOT.command()
async def hello():
    print("======================================")
    print("Command hello")
    
    await BOT.say("Hello World!")
    

BOT.run(TOKEN)