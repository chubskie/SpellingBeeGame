import random, sys, os, time


# Define console clear function
def cls():
  os.system('cls' if os.name == 'nt' else 'clear')


# ================ TITLES ==================
def print_title():
  title = """
  ||====================================================||
  ||====================================================||
  ||   ________  ___  ___       ________  _________     ||
  ||  |\   __  \|\  \|\  \     |\   __  \|\___   ___\   ||
  ||  \ \  \|\ /\ \  \ \  \    \ \  \|\  \|___ \  \_|   ||
  ||   \ \   __  \ \  \ \  \    \ \   __  \   \ \  \    ||
  ||    \ \  \|\  \ \  \ \  \____\ \  \ \  \   \ \  \   ||
  ||     \ \_______\ \__\ \_______\ \__\ \__\   \ \__\  ||
  ||      \|_______|\|__|\|_______|\|__|\|__|    \|__|  ||
  ||====================================================||
  ||====================================================||
  """
  cls()
  print(title)
  print("\033[1mMAIN MENU\033[0m")
  print("[1] Start Game")
  print("[2] Leaderboards")
  print("[3] Exit")
  print()


def print_second_title():
  cls()
  print("Choose Game Mode:")
  print("=================")
  print("[1] Classic Words")
  print("[2] Slang Words")
  print("[3] Back to Main Menu")
  print()


# ============ INITIALIZATION ==============
def choose_random(word_list, size):
  return word_list[:size]


def load_words(mode):
  word_list = []

  if mode == "1":
    three_letter_words = open("words/three_letter_words.txt", "r")
    four_letter_words = open("words/four_letter_words.txt", "r")
    five_letter_words = open("words/five_letter_words.txt", "r")

    word_list = choose_random(
        three_letter_words.read().split(), 7) + choose_random(
            four_letter_words.read().split(), 7) + choose_random(
                five_letter_words.read().split(), 7)

    three_letter_words.close()
    four_letter_words.close()
    five_letter_words.close()

  elif mode == "2":
    slang_words = open("words/slang_words.txt", "r")

    word_list = choose_random(slang_words.read().split(), 10)

    slang_words.close()

  else:
    sys.exit("INVALID MODE. PLEASE DEBUG.")

  return word_list

def DEBUG_list_words(word_list):
  for word in word_list:
    print(word)

def main_menu():
  while True:
    print_title()
    choice = input("Enter your choice: ")

    if choice == "1":
      while True:
        print_second_title()
        game_mode_choice = input("Enter your choice: ")

        if game_mode_choice == "1":
          print("Game One")
          words = load_words(game_mode_choice)
          DEBUG_list_words(words)
          input()
          break
        elif game_mode_choice == "2":
          print("Game Two")
          words = load_words(game_mode_choice)
          DEBUG_list_words(words)
          input()
          break
        elif game_mode_choice == "3":
          break
        else:
          input("Invalid option. Press ENTER to try again.")

    elif choice == "2":
      print("Leaderboards")
      input()
    elif choice == "3":
      print("\nThanks for playing!")
      sys.exit()
    else:
      input("Invalid option. Press ENTER to try again.")

# Run
main_menu()