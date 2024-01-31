import random
from PROJECTS.hangstages import HANGMANPICS

word_list = ["mouse", "crate", "church", "apple"]
# get a random choice from the word-list
random_word = random.choice(word_list)
print(random_word)
# get the length of the random word chosen
rnd_length = len(random_word)
live = 7
# A list to store the blank spaces
blank = []

# appending a blank line to the end of a list 
for _ in range(rnd_length):
	blank.append("_")
	
print(blank)

end_of_game = False
while not end_of_game:
	guess = input("Enter a letter: ").lower()
	#check if the letter guessed is in the hidden word
	for char in range(rnd_length):
		if guess == random_word[char]:
			blank[char] = guess # fill the blank spaces in the missing word
			
	# ending the game if won
	if "_" not in blank:
		end_of_game = True
		print("you won")
		
	# ending the game, if total live is used up		
	if guess not in random_word:
		live -= 1
		print(HANGMANPICS[live])
		if live == 0:  # ends the game if the total chances to play is exhausted
			end_of_game = True
			print("You lost the game!!!!")
print(blank)