import os
import time
from datetime import datetime
"""
Data and time for logs to store time app restart time
"""
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
"""
Variable for location of file below
"""
work_dir = os.getcwd()
apps_file= '{}/bin/app_monitor/apps.txt'.format(work_dir)
monitor_app_list = []
rtorrent_log_file = '{}/bin/app_monitor/rtorrent.txt'.format(work_dir)
docker_log_file = '{}/bin/app_monitor/docker_apps.txt'.format(work_dir)


"""
Function are defined below
"""
class app_monitor():
    def rtorrent_monitor(self):
        Pid = os.system('pgrep rtorrent')
        Pid = int(Pid)

        if Pid == 256: # Pid is 256 when os.system doesn't give O/P for Linux
            os.system("app-rtorrent restart") #  restart app
            with open(rtorrent_log_file, "a") as f:
                f.write("\n\nTIME: "+current_time+"\n")
                f.write('rTorrent was down and has been RESTARTED')
        else:
            pass
        time.sleep(2)


        Pid2 = os.system('pgrep rtorrent')
        Pid2 = int(Pid2)

        if Pid2 == 256: # no effect of restart so time to repair
            os.system("app-rtorrent repair")
            with open(rtorrent_log_file, "a") as f:
                f.write("\nTIME:"+current_time+"\n")
                f.write('Restart failed so trying to REPAIR now')

        else:
            pass
        time.sleep(2)

        final_pid = os.system('pgrep rtorrent')

        if final_pid == 256: # restart or repair comands doesn't work
            with open(rtorrent_log_file, "a") as f:
                f.write("\nTIME:"+current_time+"\n")
                f.write("\nScript is unable to FIX your rTorrent so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php\n")

        else:
            pass
    
    
    
    
    def docker_app(self,apps):
        #status = os.popen("ps aux | grep -i sonarr").read()
        #print(len(status.splitlines()))
        for i in apps:
            print("checking status for {}".format(i))
            status = os.popen("ps aux | grep -i {}".format(i)).read()
            count = len(status.splitlines())
            if count <=2:
                os.system("app-{} upgrade".format(i))
                with open(docker_log_file, "a") as f:
                    f.write("\n\nTIME: "+current_time+"\n")
                    f.write('{i} was down and has been RESTARTED'.format(i))
            else:
                pass
   
    def create_app_list(self):
        os.system("mkdir {}/bin/app_monitor".format(work_dir))
        app_list = input("Please enter all applications you want to monitor with a single space in between(for example sonarr radarr lidarr):").split()
        with open(apps_file,'+w') as f:
            for i in app_list:
                f.write(i + '\n')
        f.close()
            
    def read_list(self):
        with open(apps_file,'r') as f:
            s = f.readlines()
        monitor_app_list = [x.strip() for x in s]
        return monitor_app_list
        




monitor = app_monitor()
if __name__ == '__main__':
    check = os.path.exists(apps_file)
    if check == False:
        monitor.create_app_list()
    else:
        monitor_app_list = monitor.read_list()
        if 'rtorrent' in monitor_app_list:
            monitor.rtorrent_monitor()
            monitor_app_list.remove('rtorrent')
            monitor.docker_app(monitor_app_list)
        else:
            monitor.docker_app(monitor_app_list)