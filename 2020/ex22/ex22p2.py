import copy
def play(player_one, player_two, history):

	if(player_one, player_two) in history:
		print("Repeat round. Player one wins")
		return (1, player_one)

	history += [(player_one, player_two)]

	count = 0
	while len(player_one) != 0 and len(player_two) != 0:
		count +=1
		card_one = player_one.pop(0)
		card_two = player_two.pop(0)

		print("Round " + str(count))

		if len(player_one) == card_one and len(player_two) == card_two:
			print("Entering subgame")
			new_one = copy.deepcopy(player_one) 
			new_two = copy.deepcopy(player_two) 

			result = play(new_one,new_two,history)

			if result[0] == 1:
				print("One wins!")
				player_one += [card_one, card_two]
			elif result[0] == 2:
				print("Two wins!")
				player_two += [card_two, card_one]

			continue

		if card_one > card_two:
			print("One wins!")
			player_one += [card_one, card_two]
		else:
			print("Two wins!")
			player_two += [card_two, card_one]

	print("Game over at round " + str(count))

	if player_one:
		print("Player one wins the game")
		return (1,player_one)
	else:
		print("Player two wins the game")
		return (2, player_two)


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

winner_deck = play(player_one, player_two, [])

winner_deck = winner_deck[::-1]
print(winner_deck)

score = 0
for i in range(len(winner_deck)):
	score += winner_deck[i] * (i+1)

print(score)