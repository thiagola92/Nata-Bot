import discord.voice_client
from bot_info import BOT

@BOT.command(aliases=["yp"], pass_context=True)
async def youtube_play(context, url=""):
    print("======================================")
    print("Command youtube_play")
    
    '''
        Acredito que BOT.join_voice_channel() já verifique se opus library foi carregada.
        Mas caso algum dia descubra que não, use
            discord.opus.is_loaded(); para ver que foi carregada
            discord.opus.load_opus(); para carregar (caso precise de parametro tente passar "opus")
    '''
    
    try:
        voice = BOT.voice_client_in(context.message.server)
        
        if voice is None:
            channel = context.message.author.voice.voice_channel
            voice = await BOT.join_voice_channel(channel)
        
        player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=nYCOA2jQ-XA')
        player.start()
        
    except Exception as e:
        await BOT.say("```{}``` \n Hey newbie! Use **!help COMMAND** to learn more about it".format(e))