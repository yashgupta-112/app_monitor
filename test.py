def Discord_Notifications():
        with open('discord.txt','r') as f:
            return f.read()
            
        
    
    
s = Discord_Notifications()
print(s)