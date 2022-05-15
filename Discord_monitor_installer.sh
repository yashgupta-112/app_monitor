#!/bin/bash

if [ ! -d "$HOME/scripts" ]; then
  mkdir -p "$HOME/scripts/app_monitor"
fi



wget -P $HOME/scripts/app_monitor/ https://raw.githubusercontent.com/yashgupta-112/app_monitor/master/Discord_Notfication_monitory.py

clear

croncmd="/usr/bin/python3 $HOME/scripts/app_monitor/Discord_Notfication_monitory.py"
cronjob="*/5 * * * * $croncmd"
(
    crontab -l 2>/dev/null | grep -v -F "$croncmd" || :
    echo "$cronjob"
) | crontab -


/usr/bin/python3 $HOME/scripts/app_monitor/Discord_Notfication_monitory.py

