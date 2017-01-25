from bot import BOT

@BOT.command()
async def close():
    print("======================================")
    print("Command close")
    
    await BOT.close() 