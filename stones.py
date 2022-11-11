n = input()

n = int(n)

count = n

i = 1

while i <= n:

    if n == 1:
        print('Alice')
        break
    if count % 2 == 0:
        count -= 1
    elif count % 2 != 0:
        count -= 2

    i += 1

if count == 1:
    print('Alice')
else:
    print('Bob')
