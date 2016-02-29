hangmanWord = ""

while len(hangmanWord) < 3 or len(hangmanWord) > 20 or not hangmanWord.isalpha():
	hangmanWord = raw_input("Which word will your friend try to find? >>> ").lower()
	print ""
	if len(hangmanWord) < 3:
		print "ERROR: Please enter a word at least 3 letters long."
	if len(hangmanWord) > 20:
		print "ERROR: Please enter a word at most 20 letters long."
	if not hangmanWord.isalpha():
		print "ERROR: Please only use letters in your word."

triesLeft = 0

while not (triesLeft > 4 and triesLeft < 15):
	try:
		triesLeft = int(raw_input("How many incorrect letters can your friend try? (Recommended: 8-12) >>> "))
	except ValueError:
		triesLeft = 0
	print ""
	print "ERROR: Please insert a number between 5-15"

letters = []
corrects = []
incorrects = []

for x in range(len(hangmanWord)):
	letters.append(hangmanWord[x:x+1])
	corrects.append("_")

for x in range(50):
	print ""

guessedLetter = ""

while not letters == corrects:
	underscore = ""
	for x in range(len(hangmanWord)):
		if corrects[x] == letters[x]:
			underscore = underscore + corrects[x] + " "
		else:
			underscore = underscore + "_ "
	print underscore
	print ""
	guessedLetter = raw_input("Guess a letter! >>> ").lower()
	guessedLetter.lower()
	print ""
	print ""
	if not len(guessedLetter) == 1 or not guessedLetter.isalpha():
		print "Please input only a letter!"
	elif guessedLetter in incorrects:
		print "You already guessed this letter!"
	elif guessedLetter in letters:
		incorrects.append(guessedLetter)
		print "That's a correct letter!"
		for x in range(len(hangmanWord)):
			if letters[x] == guessedLetter:
				corrects[x] = (guessedLetter)
	elif triesLeft > 1:
		triesLeft -= 1
		incorrects.append(guessedLetter)
		if triesLeft == 1:
			print "That is an incorrect letter! You have " + str(triesLeft) + " try left!"
		else:
			print "That is an incorrect letter! You have " + str(triesLeft) + " tries left!"
	else:
		print ""
		print "You lost! The word was " + hangmanWord
		exit()
	print "Letters you tried so far: " + str(incorrects)

print ""
print "You have found the word! The word was " + hangmanWord
