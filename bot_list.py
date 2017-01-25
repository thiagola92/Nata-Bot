from bot import BOT

@BOT.command()
async def call_list(subject = None):
    print("======================================")
    print("Command call_list")
    
    try:
        subject_list = "list\\" + subject
        file = open(subject_list, 'r')
        
        message = ""
        
        for line in file:
            message = message + line
            
        file.close()
        await BOT.say(message)
    except Exception as e:
        await BOT.say("```" + str(e) + "```")
        await BOT.say("Hey newbie! Use **!help COMMAND** to learn more about it")
    
@BOT.command()
async def add_list(subject = None, item = None):
    print("======================================")
    print("Command add_list")
    
    try:
        subject_list = "list\\" + subject
        file = open(subject_list, 'a')
        
        file.write("\n" + item)
        file.close()
    except Exception as e:
        await BOT.say("```" + str(e) + "```")
        await BOT.say("Hey newbie! Use **!help COMMAND** to learn more about it")

@BOT.command()
async def create_list(subject = None):
    print("======================================")
    print("Command create_list")
    
    try:
        subject_list = "list\\" + subject
        file = open(subject_list, 'w')
        
        file.close()
    except Exception as e:
        await BOT.say("```" + str(e) + "```")
        await BOT.say("Hey newbie! Use **!help COMMAND** to learn more about it")
    
@BOT.command()
async def remove_list(subject = None, item = None):
    print("======================================")
    print("Command remove_list")
    
    try:
        subject_list = "list\\" + subject
        file = open(subject_list, 'r')
        
        new_list = ""
        
        for line in file:
            new_list = new_list + line
        new_list = new_list.split()
        
        file.close()
        file = open(subject_list, 'w')
        
        for line in new_list:
            if(line == item):
                continue
            file.write(line + "\n")
            
        file.close()
    except Exception as e:
        await BOT.say("```" + str(e) + "```")
        await BOT.say("Hey newbie! Use **!help COMMAND** to learn more about it")