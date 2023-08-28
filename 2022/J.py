n_rounds = int(input())
joao_cards = [int(x) for x in input().split(" ")]
maria_cards = [int(x) for x in input().split(" ")]
table_cards = [int(x) for x in input().split(" ")]

cards_values = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 10, 12: 10, 13: 10}
cards_in_game = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}

for cards in joao_cards + maria_cards + table_cards:
    cards_in_game[cards] += 1

maria_cards = [cards_values[x] for x in maria_cards]
joao_cards = [cards_values[x] for x in joao_cards]
table_cards = [cards_values[x] for x in table_cards]

sum_table = sum(table_cards)
sum_maria = sum(maria_cards) + sum_table
sum_joao = sum(joao_cards) + sum_table

if sum_joao > sum_maria:
    burst = 24 - sum_joao
    while burst <= 13:
        if cards_in_game[burst] == 4:
            burst += 1
        else:
            break
    if burst > 10 or sum_maria + cards_values[burst] >= 24:
        print(-1)
    else:
        print(burst)
else:
    victory = 23 - sum_maria
    if victory > 10 or cards_in_game[victory] == 4:
        print(-1)
    else:
        print(victory)
