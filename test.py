import os
import time
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#check PID of rtorrent
Pid = os.system('pgrep rtorrent')
Pid = int(Pid)

if Pid == 256: # Pid is 256 when os.system doesn't give O/P for Linux
    os.system("app-rtorrent restart") #  restart app
    with open("scripts/rtorrentRestart.log", "a") as f:
        f.write("\n\nTIME: "+current_time+"\n")
        f.write('rTorrent was down and has been RESTARTED')
else:
    pass
time.sleep(2)


Pid2 = os.system('pgrep rtorrent')
Pid2 = int(Pid2)

if Pid2 == 256: # no effect of restart so time to repair
    os.system("app-rtorrent repair")
    with open("scripts/rtorrentRestart.log", "a") as f:
        f.write("\nTIME:"+current_time+"\n")
        f.write('Restart failed so trying to REPAIR now')

else:
    pass
time.sleep(2)

final_pid = os.system('pgrep rtorrent')

if final_pid == 256: # restart or repair comands doesn't work
    with open("scripts/rtorrentRestart.log", "a") as f:
        f.write("\nTIME:"+current_time+"\n")
        f.write("\nScript is unable to FIX your rTorrent so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php\n")

else:
    pass