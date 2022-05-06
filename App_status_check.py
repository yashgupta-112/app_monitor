import os
import time
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

class app_monitor():
    def rtorrent_monitor(self):
        status = os.popen("pgrep rtorrent").read()
        if status == "":
            os.system("app-rtorrent restart")
        else:
            pass





monitor = app_monitor()
if __name__ == '__main__':
    # s = input('Please enter name of application you want script to monitor(example rtorrent sonarr deluge):')
    monitor.rtorrent_monitor()