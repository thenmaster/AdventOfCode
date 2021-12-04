player_one = []
player_two = []
with open("input.txt", "r") as f:
	f.readline()
	card = f.readline()

	while card.strip() != "":
		player_one += [int(card)]
		card = f.readline()

	f.readline()
	card = f.readline()

	while card.strip() != "":
		player_two += [int(card)]
		card = f.readline()

print(player_one)
print(player_two)

count = 0
while len(player_one) != 0 and len(player_two) != 0:
	count +=1
	card_one = player_one.pop(0)
	card_two = player_two.pop(0)

	print("Round " + str(count))
	if card_one > card_two:
		print("One wins!")
		player_one += [card_one, card_two]
	else:
		print("Two wins!")
		player_two += [card_two, card_one]

print("Game over at round " + str(count))

if player_one:
	print("Player one wins the game")
	winner_deck = player_one
else:
	print("Player two wins the game")
	winner_deck = player_two

winner_deck = winner_deck[::-1]
print(winner_deck)

score = 0
for i in range(len(winner_deck)):
	score += winner_deck[i] * (i+1)

print(score)