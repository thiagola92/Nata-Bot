from bot_info import BOT

@BOT.command()
async def close():
    print("======================================")
    print("Command close")
    
    await BOT.say("Fudeu.. A privada quebrou") 
    await BOT.close() 