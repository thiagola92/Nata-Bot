from bot_info import BOT

from random import randint

@BOT.command()
async def dice(max_value = 100):
    print("======================================")
    print("Command dice")

    try:
        number = randint(1,int(max_value))
        await BOT.say(str(number))
    except Exception as e:
        await BOT.say("```" + str(e) + "```")
        await BOT.say("Hey newbie! Use **!help COMMAND** to learn more about it")

@BOT.command()
async def choose(*options):
    print("======================================")
    print("Command choose")
    
    try:
        number = randint(0, len(options) - 1)
        await BOT.say(options[number])
    except Exception as e:
        await BOT.say("```" + str(e) + "```")
        await BOT.say("Hey newbie! Use **!help COMMAND** to learn more about it")
    