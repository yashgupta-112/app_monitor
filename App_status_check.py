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

"""
Function are defined below
"""
class app_monitor():
    def rtorrent_monitor(self):
        status = os.popen("pgrep rtorrent").read()
        if status == "":
            os.system("app-rtorrent restart")
        else:
            pass
    def docker_app(self):
        #status = os.popen("ps aux | grep -i sonarr").read()
        #print(len(status.splitlines()))
        with open(apps_file,'r') as f:
            s = f.readlines()
        monitor_app_list = [x.strip() for x in s]
        print(monitor_app_list)
   
    def create_app_list(self):
        os.system("mkdir {}/bin/app_monitor".format(work_dir))
        app_list = input("Please enter all applications you want to monitor with a single space in between(for example sonarr radarr lidarr):").split()
        with open(apps_file,'+w') as f:
            for i in app_list:
                f.write(i + '\n')
        f.close()
            
    




monitor = app_monitor()
if __name__ == '__main__':
    check = os.path.exists(apps_file)
    if check == False:
        monitor.create_app_list()
    else:
        print("file already exist")