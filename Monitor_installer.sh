#!/bin/bash

printf "\033[0;31mDisclaimer: This Script is unofficial and Ultra.cc staff will not support any issues with it will monitor your applications and restart them if application are not running it\033[0m\n"
read -rp "Type confirm if you wish to continue: " input
if [ ! "$input" = "confirm" ]; then
  exit
fi

if [ ! -d "$HOME/script" ]; then
  mkdir -p "$HOME/script/app_monitor"
fi



wget -P $HOME/script/app_monitor/ https://raw.githubusercontent.com/yashgupta-112/app_monitor/master/App_status_check.py

clear

croncmd="/usr/bin/python3 $HOME/script/app_monitor/App_status_check.py"
cronjob="5 * * * * $croncmd"
(
    crontab -l 2>/dev/null | grep -v -F "$croncmd" || :
    echo "$cronjob"
) | crontab -

/usr/bin/python3 $HOME/script/app_monitor/App_status_check.py