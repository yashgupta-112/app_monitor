import os 


status = os.popen("ps aux | grep -i sonarr")

print(status)