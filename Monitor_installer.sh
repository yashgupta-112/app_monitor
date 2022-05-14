#!/bin/bash

if [ ! -d "$HOME/script" ]; then
  mkdir -p "$HOME/script/app_monitor"
fi



wget -P $HOME/script/app_monitor/ https://raw.githubusercontent.com/yashgupta-112/app_monitor/master/App_status_check.py

clear

croncmd="/usr/bin/python3 $HOME/script/app_monitor/App_status_check.py"
cronjob="*/5 * * * * $croncmd"
(
    crontab -l 2>/dev/null | grep -v -F "$croncmd" || :
    echo "$cronjob"
) | crontab -

croncmd="rm -rf $HOME/script/app_monitor/docker_apps.txt  rtorrent.txt"
cronjob="0 0 1 * * $croncmd"
(
    crontab -l 2>/dev/null | grep -v -F "$croncmd" || :
    echo "$cronjob"
) | crontab -


/usr/bin/python3 $HOME/script/app_monitor/App_status_check.py