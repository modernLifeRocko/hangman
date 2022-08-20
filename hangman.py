import random

# choose a word list
from words import word_list

dict = word_list
#choose a word to be guessed / game setup
dict_size = len(dict)

def get_valid_word(words):
  word = random.choice(words)
  while ' ' in word or '-' in word:
    word = random.choice(words)

  return word

word_to_guess = get_valid_word(dict)

max_wrongs = 10

length = len(word_to_guess)

def show_set(word, discovered = None, wrongs = 0):
  word_length = len(word)
  if discovered is None:
    discovered = "_ "*word_length
  print(discovered)
  print(f"{wrongs} / {max_wrongs}")

def get_valid_input(taboo):
  guess = input("Guess a letter: ").lower()
  while guess.isnumeric() or len(guess)>1:
    guess = input("Not a valid guess. Try again: ").lower()
  return guess

def game (word):
  to_guess_letters = set(word)
  guessed_letters = set()
  wrongs = 0
  show_set(word)
  discovered_pattern = ['-']*len(word)
  while wrongs < max_wrongs and len(to_guess_letters)>0:
    user_letter = get_valid_input(guessed_letters)
    if user_letter not in guessed_letters:
      guessed_letters.add(user_letter)
      if user_letter in to_guess_letters:
        to_guess_letters.remove(user_letter)
        ix = [i for i, v in enumerate(word) if v == user_letter]
        for i in ix:
          discovered_pattern[i] = user_letter
      else:
        wrongs += 1
    
    discovered = " ".join(discovered_pattern)
    show_set(word, discovered, wrongs)
  
  if len(to_guess_letters) == 0:
    print("You won!")
  elif wrongs >= max_wrongs:
    print(f"You lost! The answer was {word}")


game(word_to_guess)
        




