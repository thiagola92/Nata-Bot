from bot_info import BOT
import re
import os

@BOT.command()
async def call_list(list_name = None):
    print("======================================")
    print("Command call_list")
    
    try:
        if re.search("\.+", list_name) != None:
            raise Exception("No permisson to use Wildcards")
            
        list_name_path = "list\\" + list_name
        file = open(list_name_path, 'r')
        
        message = ""
        
        for line in file:
            message = message + line
            
        file.close()
        await BOT.say(message)
    except Exception as e:
        await BOT.say("```" + str(e) + "```")
        await BOT.say("Hey newbie! Use **!help COMMAND** to learn more about it")
    
@BOT.command()
async def add_list(list_name = None, item = None):
    print("======================================")
    print("Command add_list")
    
    try:
        if re.search("\.+", list_name) != None:
            raise Exception("No permisson to use Wildcards")
            
        list_name_path = "list\\" + list_name
        file = open(list_name_path, 'a')
        
        file.write(item + "\n")
        file.close()
        await BOT.say("Chamou?")
    except Exception as e:
        await BOT.say("```" + str(e) + "```")
        await BOT.say("Hey newbie! Use **!help COMMAND** to learn more about it")

@BOT.command()
async def create_list(list_name = None):
    print("======================================")
    print("Command create_list")
    
    try:
        if re.search("\.+", list_name) != None:
            raise Exception("No permisson to use Wildcards")
        
        list_name_path = "list\\" + list_name
        file = open(list_name_path, 'w')
        
        file.close()
        await BOT.say("Ta")
    except Exception as e:
        await BOT.say("```" + str(e) + "```")
        await BOT.say("Hey newbie! Use **!help COMMAND** to learn more about it")
    
@BOT.command()
async def remove_list(list_name = None, item = None):
    print("======================================")
    print("Command remove_list")
    
    try:
        if re.search("\.+", list_name) != None:
            raise Exception("No permisson to use Wildcards")
            
        list_name_path = "list\\" + list_name
        file = open(list_name_path, 'r')
        
        new_list = ""
        
        for line in file:
            new_list += line
        new_list = new_list.split("\n")
        
        file.close()
        file = open(list_name_path, 'w')
        
        for line in new_list:
            if(line == item):
                continue
            file.write(line + "\n")
            
        file.close()
        await BOT.say("Filtrou")
    except Exception as e:
        await BOT.say("```" + str(e) + "```")
        await BOT.say("Hey newbie! Use **!help COMMAND** to learn more about it")
        
@BOT.command()
async def delete_list(list_name = None):
    print("======================================")
    print("Command delete_list")
    
    try:
        if re.search("\.+", list_name) != None:
            raise Exception("No permisson to use Wildcards")
            
        list_name_path = "list\\" + list_name
        os.remove(list_name_path)
        await BOT.say("TA PEGANDO FOGO BIXO")
    except Exception as e:
        await BOT.say("```" + str(e) + "```")
        await BOT.say("Hey newbie! Use **!help COMMAND** to learn more about it")