app_list = input("Please enter all applications you want to monitor with a single space in between(for example sonarr radarr lidarr):").split()


with open('test.txt','+w') as f:
    for i in app_list:
       f.write(i + '\n')
    f.close()