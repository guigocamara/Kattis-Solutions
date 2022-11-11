s = input()

list_of_strings = s.split(' ')


king, queen, rook, bishop, knight, pawn = map(int, list_of_strings)

if king < 1:
    king = 1
elif king > 1:
    king = 1 - king

if queen < 1:
    queen = 1
elif queen > 1:
    queen = 1 - queen

print(king, queen)
