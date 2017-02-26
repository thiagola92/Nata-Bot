from info import BOT
import re
import os

@BOT.command(aliases = ["cl"], help = "Lê tudo que esta na lista passada")
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
            message += line
            
        file.close()
        await BOT.say(message)
    except Exception as e:
        await BOT.say("```{}``` \n Hey newbie! Use **!help COMMAND** to learn more about it".format(e))
    
@BOT.command(aliases = ["al"], help = "Adiciona os items passados na lista")
async def add_list(list_name = None, *items):
    print("======================================")
    print("Command add_list")
    
    try:
        if re.search("\.+", list_name) != None:
            raise Exception("No permisson to use Wildcards")
                
        list_name_path = "list\\" + list_name
        file = open(list_name_path, 'a')
            
        for item in items:
            file.write(item + "\n")
            
        file.close()
        await BOT.say("Added")
    except Exception as e:
        await BOT.say("```{}``` \n Hey newbie! Use **!help COMMAND** to learn more about it".format(e))

@BOT.command(aliases = ["nl"], help = "Cria uma lista nova")
async def new_list(list_name = None):
    print("======================================")
    print("Command new_list")
    
    try:
        if re.search("\.+", list_name) != None:
            raise Exception("No permisson to use Wildcards")
        
        list_name_path = "list\\" + list_name
        file = open(list_name_path, 'w')
        
        file.close()
        await BOT.say("List {} created".format(list_name))
    except Exception as e:
        await BOT.say("```{}``` \n Hey newbie! Use **!help COMMAND** to learn more about it".format(e))
    
@BOT.command(aliases = ["rl"], help = "Remove os items passados da lista")
async def remove_list(list_name = None, *items):
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
            if(remove_line(line, items) == True):
                continue
            file.write(line + "\n")
            
        file.close()
        await BOT.say("Removed")
    except Exception as e:
        await BOT.say("```{}``` \n Hey newbie! Use **!help COMMAND** to learn more about it".format(e))
        
def remove_line(line, items):
    for item in items:
        if (line == item):
            return True
            
    return False
        
@BOT.command(aliases = ["dl"], help = "Deleta uma lista")
async def delete_list(list_name = None):
    print("======================================")
    print("Command delete_list")
    
    try:
        if re.search("\.+", list_name) != None:
            raise Exception("No permisson to use Wildcards")
            
        list_name_path = "list\\" + list_name
        os.remove(list_name_path)
        await BOT.say("Deleted")
    except Exception as e:
        await BOT.say("```{}``` \n Hey newbie! Use **!help COMMAND** to learn more about it".format(e))