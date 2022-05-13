import requests

#Webhook of my channel. Click on edit channel --> Webhooks --> Creates webhook
mUrl = "https://discord.com/api/webhooks/974625937863897088/bc1NpcXvtCPEud6e36bS85Z3U-PnV5ut_20AVQyYsCFK7zCiHtvu1qC95Zp-oEA4oLaj"

i = "sonarr"
data = {"content": f'{i} your application was down has been restarted :)'}
response = requests.post(mUrl, json=data)

