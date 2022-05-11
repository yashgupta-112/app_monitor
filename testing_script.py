t = []

with open('test.txt', 'r') as f:
    s = f.readlines()
t = content_list = [x.strip() for x in s]
for i in t:
    print(i)
