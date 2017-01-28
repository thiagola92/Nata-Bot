from bot_info import BOT

from random import randint

@BOT.command()
async def dice(max_value):
    print("======================================")
    print("Command dice")

    try:
        number = randint(1,int(max_value))
        await BOT.say(str(number))
    except Exception as e:
        await BOT.say("```" + str(e) + "```")
        await BOT.say("Hey newbie! Use **!help COMMAND** to learn more about it")