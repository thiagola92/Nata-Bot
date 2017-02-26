from info import BOT

from random import randint

@BOT.command(help = "O Bot vai te dar um número entre 1 e o número que você passou")
async def dice(max_value = 100):
    print("======================================")
    print("Command dice")

    try:
        number = randint(1,int(max_value))
        await BOT.say(str(number))
    except Exception as e:
        await BOT.say("```{}``` \n Hey newbie! Use **!help COMMAND** to learn more about it".format(e))

@BOT.command(help = "Passe varias opções e o Bot vai sortear uma delas")
async def choose(*options):
    print("======================================")
    print("Command choose")
    
    try:
        number = randint(0, len(options) - 1)
        await BOT.say(options[number])
    except Exception as e:
        await BOT.say("```{}``` \n Hey newbie! Use **!help COMMAND** to learn more about it".format(e))
    