face_ranks = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

total = 0
for _ in range(6):
    card = input()
    if card in face_ranks:
        total += face_ranks[card]
    else:
        total += int(card)

print(total / 6)
