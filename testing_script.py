from turtle import clear


t = []

with open('test.txt', 'r') as f:
    s = f.readlines()
t = [x.strip() for x in s]
print("t:",t)
t.remove('rtorrent')
print(t)