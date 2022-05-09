import os 


status = os.popen("ps aux | grep -i sonarr").read()

print(status)