from info import BOT

@BOT.command()
async def shutdown():
    print("======================================")
    print("Command close")
    
    await BOT.say("Fudeu.. A privada quebrou") 
    await BOT.close() 
    
@BOT.command()
async def math(*expression):
    print("======================================")
    print("Command math")
    
    expression_string = ""
    
    for x in expression:
        expression_string += str(x)
    
    try:
        expression = eval(expression_string)
        await BOT.say(str(expression))
    except Exception as e:
        await BOT.say("```{}``` \n Hey newbie! Use **!help COMMAND** to learn more about it".format(e))