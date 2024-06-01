import random

# Read text files containing words
with open('words/threes.txt') as three_letters:
  three_letters = three_letters.read()

with open('words/fours.txt') as four_letters:
  four_letters = four_letters.read()

with open('words/fives.txt') as five_letters:
  five_letters = five_letters.read()

# Read text file containing leaderboard
with open('leaderboard.txt') as leaderboard:
  leaderboard = leaderboard.read()

words = three_letters.split() + four_letters.split() + five_letters.split()
words_length = len(words)

for i in range(words_length - 1):
  index = random.randint(0, words_length - 1)
  print(words[index])