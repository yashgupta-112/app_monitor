str(apps) = list(input("please enter all apps with ").split())
print("these apps need check",apps)
apps = str(apps)

with open('appllist.txt', '+w') as f:
    f.write(apps)
    f.close()