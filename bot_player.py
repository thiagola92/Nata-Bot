from info import BOT
import discord.voice_client
import os

player = None

@BOT.command(aliases=["yp"], pass_context=True, help = "Passe um link do youtube para tocar")
async def youtube_play(context, url=""):
    print("======================================")
    print("Command youtube_play")
    
    '''
        Acredito que BOT.join_voice_channel() já verifique se opus library foi carregada.
        Mas caso algum dia descubra que não, use
            discord.opus.is_loaded(); para ver que foi carregada
            discord.opus.load_opus(); para carregar (caso precise de parametro tente passar "opus")
    '''
    
    global player
    try:
        voice = BOT.voice_client_in(context.message.server)
        channel = context.message.author.voice.voice_channel
        
        if voice is None:
            voice = await BOT.join_voice_channel(channel)
        else:
            await voice.move_to(channel)
        
        if player is None or not player.is_playing():
            player = await voice.create_ytdl_player(url)
            player.start()
            await BOT.say("Playing request from {}".format(context.message.author.mention))
        
    except Exception as e:
        await BOT.say("```{}``` \n Hey newbie! Use **!help COMMAND** to learn more about it".format(e))
        
@BOT.command(aliases=["ap"], pass_context=True, help = "Fale o nome do audio que deve tocar")
async def audio_play(context, mp3=""):
    print("======================================")
    print("Command audio_play")
    
    '''
        Acredito que BOT.join_voice_channel() já verifique se opus library foi carregada.
        Mas caso algum dia descubra que não, use
            discord.opus.is_loaded(); para ver que foi carregada
            discord.opus.load_opus(); para carregar (caso precise de parametro tente passar "opus")
    '''
    
    global player
    try:
        if re.search("\.+", mp3) != None:
            raise Exception("No permisson to use Wildcards")
    
        voice = BOT.voice_client_in(context.message.server)
        channel = context.message.author.voice.voice_channel
        
        if voice is None:
            voice = await BOT.join_voice_channel(channel)
        else:
            await voice.move_to(channel)
        
        if player is None or not player.is_playing():
            player = voice.create_ffmpeg_player("audio/" + mp3)
            player.start()
            await BOT.say("Playing request from {}".format(context.message.author.mention))
        
    except Exception as e:
        await BOT.say("```{}``` \n Hey newbie! Use **!help COMMAND** to learn more about it".format(e))
        
        
@BOT.command(aliases = ["sa"], help = "Exibir todos os audios no diretório")
async def show_audios():
    print("======================================")
    print("Command show_audios")
    
    every_file = os.listdir("./audio")
    message = ""
    
    for file in every_file:
        message += file + "\n"
    
    await BOT.say(message)
    
        
        
        