import os
import time
from datetime import datetime
import requests
# Modules import 

"""
Data and time to store restart time of application
"""
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
"""
Variable for location log files 
"""
work_dir = os.getcwd()
apps_file = '{}/script/app_monitor/apps.txt'.format(work_dir)
monitor_app_list = []
rtorrent_log_file = '{}/script/app_monitor/rtorrent.txt'.format(work_dir)
docker_log_file = '{}/script/app_monitor/docker_apps.txt'.format(work_dir)
Discord_WebHook_File = '{}/script/app_monitor/discord.txt'.format(work_dir)
Web_Hook_URL = ""
torrent_client_list = ['deluge','transmission','qbittorrent','rtorrent']

"""
Main function is defined below
"""
class app_monitor():
    def rtorrent_monitor(self,Web_Hook_URL):
        Pid = os.system('pgrep rtorrent')
        Pid = int(Pid)

        if Pid == 256:  # Pid is 256 when os.system doesn't give O/P for Linux
            os.system("app-rtorrent restart")  # restart app
            data = {"content": f'rtorrent application was down and has been restarted by script:)'}
            response = requests.post(Web_Hook_URL, json=data)
        else:
            pass
        time.sleep(2)
        Pid2 = os.system('pgrep rtorrent')
        Pid2 = int(Pid2)

        if Pid2 == 256:  # no effect of restart so time to repair
            os.system("app-rtorrent repair")
            data = {"content": f'rtorrent application was down and has been repair by script:)'}
            response = requests.post(Web_Hook_URL, json=data)

        else:
            pass
        time.sleep(2)

        final_pid = os.system('pgrep rtorrent')

        if final_pid == 256:  # restart or repair comands doesn't work
            data = {"content": f'Script is unable to FIX your rTorrent so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php'}
            response = requests.post(Web_Hook_URL, json=data)
        else:
            pass

    def docker_app(self, apps,Web_Hook_URL):
        for i in apps:
            status = os.popen("ps aux | grep -i {}".format(i)).read()
            count = len(status.splitlines())
            if count <= 2:
                os.system("app-{} upgrade".format(i))
                data = {"content": f'Your {i} application was down and has been restarted by script:)'}
                response = requests.post(Web_Hook_URL, json=data)
            else:
                pass
            time.sleep(3)
            status = os.popen("ps aux | grep -i {}".format(i)).read()
            count = len(status.splitlines())
            if count <= 2:
                data = {"content": f"\nScript is unable to FIX your {i} so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php\n"}
                response = requests.post(Web_Hook_URL, json=data)
                        

    def create_app_list(self):
        app_list = input(
            "Please enter all applications you want to monitor with a single space in between(for example sonarr radarr lidarr):").split()
        with open(apps_file, '+w') as f:
            for i in app_list:
                f.write(i + '\n')
        f.close()
        
    def Discord_Notifications_Accepter(self):
        Web_Url = input("Please enter your Discord Web Hook Url Here:")
        with open(Discord_WebHook_File,'+w') as f:
            f.write(Web_Url)
    
    def Discord_WebHook_Reader(self):
        with open(Discord_WebHook_File,'r') as f:
            return f.read()
       

    def read_list(self):
        with open(apps_file, 'r') as f:
            s = f.readlines()
        monitor_app_list = [x.strip() for x in s]
        return monitor_app_list
    
    def torrent_client_checker(self,list1,list2):
        list1 = set(list1)
        list2 = set(list2)
        list3 = list1.intersection(list2)
        return list(list3)
    
    def torrent_client_fixing(self,list1,Web_Hook_URL):
        for i in list1:
            status = os.popen("ps aux | grep -i {}".format(i)).read()
            count = len(status.splitlines())
            if count <= 2:
                os.system("app-deluge restart")
                data = {"content": f'Your {i} application was down and has been restarted by script:)'}
                response = requests.post(Web_Hook_URL, json=data)
            else:
                pass
            time.sleep(3)
            status = os.popen("ps aux | grep -i {}".format(i)).read()
            count = len(status.splitlines())
            if count <= 2:
                os.system("app-deluge repair")
                data = {"content": f'Your {i} application was down and has been restarted by script:)'}
                response = requests.post(Web_Hook_URL, json=data)
            time.sleep(3)
            status = os.popen("ps aux | grep -i {}".format(i)).read()
            count = len(status.splitlines())
            if count <= 2:
                data = {"content": f"\nScript is unable to FIX your {i} so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php\n"}
                response = requests.post(Web_Hook_URL, json=data)


monitor = app_monitor()
if __name__ == '__main__':
    check = os.path.exists(apps_file)
    if check == False:
        monitor.create_app_list()
        Web_Hook_URL = monitor.Discord_Notifications_Accepter()
        print('Logs will be saved, now run', '\033[91m' + '"cat ~/script/app_monitor/docker_apps.txt  & cat ~/script/app_monitor/rtorrent.txt"' + '\033[0m', 'to print them!')
        time.sleep(5)
        os.system("clear")
    elif 'rtorrent' in monitor_app_list:
        Web_Hook_URL = monitor.Discord_WebHook_Reader()
        monitor.rtorrent_monitor(Web_Hook_URL)
        monitor_app_list.remove('rtorrent')
        monitor.docker_app(monitor_app_list,Web_Hook_URL)
    
    else:
        monitor_app_list = monitor.read_list()
        Web_Hook_URL = monitor.Discord_WebHook_Reader()
        s = monitor.torrent_client_checker(monitor_app_list,torrent_client_list)
        monitor.torrent_client_fixing(s,Web_Hook_URL)
        [monitor_app_list.remove(y) for y in s]
        monitor.docker_app(monitor_app_list,Web_Hook_URL)
        
