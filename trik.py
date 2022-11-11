s = input()

cup1, cup2, cup3 = 1, 0, 0

curCup = 0

char = ''

hashMap = {}

for char in input:
    hashMap['A'] = 1
    hashMap['B'] = 0
    hashMap['C'] = 0

    if char == 'A':
        curCup = min(cup1, cup2)
    elif char == 'B':
        curCup = min(cup2, cup3)
    elif char == 'C':
        curCup = min(cup3, cup1)
