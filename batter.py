n = int(input())

i = 1



while i <= n:
    
    set, days = input().split()

    set = int(set)
    days = int(days)
    candles = 0

    j = 0

    for j in range(0, days + 1):
        candles += j
        j += 1

    candles += days

    print(set, candles)

    i += 1
