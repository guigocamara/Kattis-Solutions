s = input()

i = 0

while i < len(s):
    if s[i] == 'a':
        print(s[i:len(s)])
        break
    i += 1