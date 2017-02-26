from info import BOT
from difflib import get_close_matches

@BOT.command(aliases = ["oh"], help = "Fale o nome de um heroi do overwatch e o Bot vai passar o link para a Wikia desse heroi")
async def overwatch_hero(*hero):
    print("======================================")
    print("Command overwatch_hero")
    
    wikia = "http://overwatch.wikia.com/wiki/"
    all_heroes = ["Ana", "Bastion", "D.Va", "Genji", "Hanzo", "Junkrat", "Lucio", "McCree", "Mei", "Mercy", "Pharah", "Reaper", "Reinhardt", "Roadhog", "Soldier: 76", "Sombra", "Symmetra", "Torbjorn", "Tracer", "Widomaker", "Winston", "Zarya", "Zenyatta"]
    
    words_fusion = ""
    for words in hero:
        words_fusion += words
    hero = words_fusion
    
    try:
        hero = get_close_matches(hero, all_heroes, 1, 0.3)
        await BOT.say(wikia + hero[0])
    except Exception as e:
        await BOT.say("```{}``` \n Hey newbie! Use **!help COMMAND** to learn more about it".format(e))