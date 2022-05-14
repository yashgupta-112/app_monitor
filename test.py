import os


status = os.popen("ps aux | grep -i nginx")

count = len(status.readlines())
print(count)