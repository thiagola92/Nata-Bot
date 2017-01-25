from bot import BOT
from bot import TOKEN

# Bot commands
from bot_default import close
from bot_list import call_list
from bot_list import add_list
from bot_list import remove_list

@BOT.event
async def on_ready():
    print("======================================")
    print("Bot is ready")
    
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