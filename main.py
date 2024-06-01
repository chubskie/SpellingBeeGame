import os
import random
import sys
import time

# What each library is being used for:
#   os       : used to clear the screen
#   random   : used to shuffle the words
#   sys      : used to exit the program on various breakpoints
#   time     : used to track the time elapsed per game

# ANSI Codes used for text formatting:
#   BLACK = "\033[0;30m"
#   RED = "\033[0;31m"
#   GREEN = "\033[0;32m"
#   BROWN = "\033[0;33m"
#   BLUE = "\033[0;34m"
#   PURPLE = "\033[0;35m"
#   CYAN = "\033[0;36m"
#   LIGHT_GRAY = "\033[0;37m"
#   DARK_GRAY = "\033[1;30m"
#   YELLOW = "\033[1;33m"
#   BOLD = "\033[1m"
#   ITALIC = "\033[3m"
#   UNDERLINE = "\033[4m"
#   RESET = "\033[0m"


# Define console clear function
def cls():
  # Checks Operating System to use appropriate keyword
  os.system('cls' if os.name == 'nt' else 'clear')


# ================ TITLES ==================
# Function to print the title and main menu.
def print_title():
  title = """\033[1;33m
  ||   ____  _  _  ____  ____  __  __    __    ___  ____  ____  ____   ||
  ||  (_  _)( \/ )(  _ \( ___)(  \/  )  /__\  / __)(_  _)( ___)(  _ \  ||
  ||    )(   \  /  )___/ )__)  )    (  /(__)\ \__ \  )(   )__)  )   /  ||
  ||   (__)  (__) (__)  (____)(_/\/\_)(__)(__)(___/ (__) (____)(_)\_)  ||
  \033[0m
  """

  cls()
  print(title)
  print("\033[1m\033[1;33mMAIN MENU\033[0m")
  print()
  print("\033[1;33m[1]\033[0m Start Game")
  print("\033[1;33m[2]\033[0m Leaderboards")
  print("\033[1;33m[3]\033[0m Exit")
  print()


# Function to print the game mode title.
def print_second_title():
  cls()
  title = """\033[1;33m
      _____ ___    __  ___ ____  __  ___ ____   ___   ____
     / ___// _ |  /  |/  // __/ /  |/  // __ \ / _ \ / __/
    / (_ // __ | / /|_/ // _/  / /|_/ // /_/ // // // _/  
    \___//_/ |_|/_/  /_//___/ /_/  /_/ \____//____//___/           
  \033[0m"""
  print(title)
  print()
  print("\033[1m\033[1;33mChoose Game Mode:\033[0m")
  print()
  print("\033[1;33m[1]\033[0m Classic Words")
  print("\033[1;33m[2]\033[0m Slang Words")
  print("\033[1;33m[3]\033[0m Back to Main Menu")
  print()


# ============ RULES ==============
# Print game rules for classic game mode.
def print_game_one_rules():
  cls()
  print("\033[1;33m======= RULES ========\033[0m")
  print("1.) You will be given 21 random words of varying lengths.")
  print("2.) Earned points will vary based on the length of the word.")
  print(
      "3.) After each game, you will be able to see the words you've misspelled."
  )
  print(
      "4.) Your ranking will be based first on your score, and then on your time."
  )
  print("\033[1;33m======================\033[0m")
  print()
  print("\033[1;33m======= SCORE ========\033[0m")
  print("3-letter Words = 2 pts.")
  print("4-letter Words = 5 pts.")
  print("5-letter Words = 7 pts.")
  print("\033[1;33m======================\033[0m")
  print()


# Print game rules for slang game mode.
def print_game_two_rules():
  cls()
  print("\033[1;33m======= RULES ========\033[0m")
  print("1.) You will be given 10 random slang words.")
  print("2.) Earned correctly spelled word gives you 5 pts.")
  print(
      "3.) After each game, you will be able to see the words you've misspelled."
  )
  print(
      "4.) Your ranking will be based first on your score, and then on your time."
  )
  print("\033[1;33m======================\033[0m")
  print()


# ============ INITIALIZATION ==============
# A function to randomize word list with prescribed size
def choose_random(word_list, size):
  # Checks if the size of the word list is less than the prescribed size
  if len(word_list) < size:
    return random.sample(word_list, len(word_list))
  else:
    return random.sample(word_list, size)


# A function to load words based on game mode.
def load_words(mode):
  # Initialize word list
  word_list = []

  # Check game mode if classic (1) or slang (2)
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
    # Breakpoint. User input should NOT reach this.
    sys.exit("INVALID MODE. PLEASE DEBUG.")

  # Return randomized word list
  return choose_random(word_list, len(word_list))


# ========== LEADERBOARD LOGIC ==============
# A function to load leaderboard file based on game mode.
def load_leaderboard(mode):
  # Initialize leaderboard list
  leaderboard = []

  # Check game mode if classic (1) or slang (2)
  if mode == "1":
    # Open classic leaderboard text file
    leaderboard_file = open("rankings/leaderboard_one.txt", "r")

    # Append leaderboard file contents to leaderboard list per line
    for line in leaderboard_file:
      name, total_time, score = line.strip().split(",")
      leaderboard.append((name, float(total_time), int(score)))

    # Close classic leaderboard text file
    leaderboard_file.close()
  elif mode == "2":
    # Open slang leaderboard text file
    leaderboard_file = open("rankings/leaderboard_two.txt", "r")

    # Append leaderboard file contents to leaderboard list per line
    for line in leaderboard_file:
      name, total_time, score = line.strip().split(",")
      leaderboard.append((name, float(total_time), int(score)))

    # Close slang leaderboard text file
    leaderboard_file.close()

  # Return leaderboard list
  return leaderboard


# A function to display the leaderboard based on game mode.
def display_leaderboard(mode):
  cls()
  leaderboard = load_leaderboard(mode)
  title = ""
  if mode == "1":
    title = """\033[1;33m
                _____ __    ___    ____ ____ ____ _____
               / ___// /   / _ |  / __// __//  _// ___/
              / /__ / /__ / __ | _\ \ _\ \ _/ / / /__  
              \___//____//_/ |_|/___//___//___/ \___/  
              
    ======================= LEADERBOARD =======================
    \033[0m"""
  elif mode == "2":
    title = """\033[1;33m
                    ____ __    ___    _  __ _____
                   / __// /   / _ |  / |/ // ___/
                  _\ \ / /__ / __ | /    // (_ / 
                 /___//____//_/ |_|/_/|_/ \___/  
                 
    ======================= LEADERBOARD =======================
    \033[0m"""
  else:
    sys.exit("INVALID MODE. PLEASE DEBUG.")

  print(title)
  print("    RANK          NAME         TIME          SCORE")
  print("    ---------------------------------------------------------")

  # Initialize rank counter as 1
  rank = 1
  for entry in leaderboard:

    # entry[0]  : name
    # entry[1]  : total time
    # entry[2]  : score

    print(f"    #{rank:<13}{entry[0]:<13}{entry[1]:<14.2f}{entry[2]:<14}")

    # Increment rank counter
    rank += 1

  print()
  input("Press ENTER to exit...")


# A function to update the leaderboard based on game mode.
def save_leaderboard(mode, leaderboard):
  # entry[0]  : name
  # entry[1]  : total time
  # entry[2]  : score

  # Check game mode if classic (1) or slang (2)
  if mode == "1":
    leaderboard_file = open("rankings/leaderboard_one.txt", "w")

    for entry in leaderboard:
      leaderboard_file.write(f"{entry[0]},{entry[1]},{entry[2]}\n")

    leaderboard_file.close()
  elif mode == "2":
    leaderboard_file = open("rankings/leaderboard_two.txt", "w")

    for entry in leaderboard:
      leaderboard_file.write(f"{entry[0]},{entry[1]},{entry[2]}\n")

    leaderboard_file.close()
  else:
    sys.exit("INVALID MODE. PLEASE DEBUG.")


def refresh_leaderboard(leaderboard):
  # Sort leaderboard
  for i in range(len(leaderboard)):
    for j in range(i + 1, len(leaderboard)):
      # Check if score is less than the next score
      # or if score is equal and total time is greater
      if leaderboard[i][2] < leaderboard[j][2] or leaderboard[i][2] == leaderboard[j][2] and leaderboard[i][1] > leaderboard[j][1]:
        # Swap positions
        leaderboard[i], leaderboard[j] = leaderboard[j], leaderboard[i]
  # Get only the top 10
  leaderboard = leaderboard[:10]

  return leaderboard


# ========== GAME LOGIC =============
# A function to determine points in classic game mode
def add_point(word):
  if len(word) == 3:
    return 2
  elif len(word) == 4:
    return 5
  elif len(word) == 5:
    return 7
  else:
    # Breakpoint. User input should NOT reach this.
    sys.exit("INVALID LENGTH. PLEASE DEBUG.")


# Game logic for Classic Game Mode
def play_game_one(word_list):

  # Initialize the following:
  #   - Score
  #   - Correct Item Counter
  #   - Index Counter
  #   - Misspelled Words List

  score = 0
  correct_words_count = 0
  index = 1
  misspelled_words = []

  # Get start timestamp
  start_time = time.time()

  # Iterate through word list
  for word in word_list:
    # Clear console
    cls()

    # Print given item
    print(f"\n[{index}/21] \033[1;33m{word}\033[0m\n")

    # Ask for user input
    user_input = input("Answer: ")

    # Check if user input is correct
    if user_input == word:
      # Add score depending on given word length
      score += add_point(word)
      correct_words_count += 1
    else:
      # If incorrect, add given word to mispelled words list together with user input
      misspelled_words.append([word, user_input])

    # Increment item number
    index += 1

  # Once all items are answered, get end timestamp
  end_time = time.time()

  # Calculate total time
  total_time = end_time - start_time

  # Print game results
  cls()
  print("\033[1;33m=========== RESULTS ===========\033[0m")
  print(f"Number of Correct Words: \033[1;33m{correct_words_count}/21\033[0m")
  print(f"Total Time: \033[1;33m{total_time:.2f} seconds\033[0m")
  print(f"Score: \033[1;33m{score} pts.\033[0m")
  print()

  # Check if all items are answered correctly
  if correct_words_count == 21:
    print("YOU GOT A PERFECT SCORE!")
  else:
    # If score is not perfect, list down all mispelled words and show user input
    print("\033[0;31m===== MISSPELLED WORDS ======\033[0m")
    for word in misspelled_words:
      print(f"{word[0]} (You typed \"\033[0;31m{word[1]}\033[0m\")")
  print()

  # Get name for leaderboard information
  # Will continuously ask until user inputs name
  while True:
    name = input("Enter your name: ")
    if len(name) != 0:
      break
    else:
      print("Please enter a name.\n")

  # Return the name, score, and the total time
  return name, total_time, score


# Game logic for Slang Game Mode
def play_game_two(word_list):

  # Initialize the following:
  #   - Score
  #   - Correct Item Counter
  #   - Index Counter
  #   - Misspelled Words List

  score = 0
  correct_words_count = 0
  index = 1
  misspelled_words = []

  # Get start timestamp
  start_time = time.time()

  # Iterate through word list
  for word in word_list:
    # Clear console
    cls()

    # Print given item
    print(f"\n[{index}/10] \033[1;33m{word}\033[0m\n")

    # Ask for user input
    user_input = input("Answer: ")

    # Check if user input is correct
    if user_input == word:
      # If correct, add 5 points to score
      score += 5
      correct_words_count += 1
    else:
      # If incorrect, add given word to mispelled words list together with user input
      misspelled_words.append([word, user_input])

    # Increment item number
    index += 1

  # Once done answering, get end timestamp
  end_time = time.time()

  # Calculate total time
  total_time = end_time - start_time

  # Print game results
  cls()
  print("\033[1;33m=========== RESULTS ===========\033[0m")
  print(f"Number of Correct Words: \033[1;33m{correct_words_count}/10\033[0m")
  print(f"Total Time: \033[1;33m{total_time:.2f} seconds\033[0m")
  print(f"Score: \033[1;33m{score} pts.\033[0m")
  print()

  # Check if all items are answered correctly
  if correct_words_count == 10:
    print("YOU GOT A PERFECT SCORE!")
  else:
    # If score is not perfect, list down all mispelled words and show user input
    print("\033[0;31m===== MISSPELLED WORDS ======\033[0m")
    for word in misspelled_words:
      print(f"{word[0]} (You typed \"\033[0;31m{word[1]}\033[0m\")")
  print()

  # Get name for leaderboard information
  # Will continuously ask until user inputs name
  while True:
    name = input("Enter your name: ")
    if len(name) != 0:
      break
    else:
      print("Please enter a name.\n")

  # Return the name, score, and the total time
  return name, total_time, score


# Main Program
def main():

  # Main Menu
  while True:

    print_title()

    # Ask user input
    choice = input("Enter your choice: ")

    # [1] START GAME
    if choice == "1":
      # Game Mode Menu
      while True:
        print_second_title()
        # Ask user input
        game_mode_choice = input("Enter your choice: ")

        # [1] CLASSIC GAME MODE
        if game_mode_choice == "1":
          # Show rules
          print_game_one_rules()
          input("Press ENTER to start...")

          # Initialize word list
          words = load_words(game_mode_choice)

          # Run game logic
          name, total_time, score = play_game_one(words)

          # Add entry to leaderboard
          leaderboard = load_leaderboard(game_mode_choice)
          leaderboard.append([name, total_time, score])
          leaderboard = refresh_leaderboard(leaderboard)
          save_leaderboard(game_mode_choice, leaderboard)

          print()

          # Show leaderboard
          display_leaderboard(game_mode_choice)

          # Back to Main Menu
          break
        # [2] SLANG GAME MODE
        elif game_mode_choice == "2":
          # Show rules
          print_game_two_rules()
          input("Press ENTER to start...")

          # Initialize word list
          words = load_words(game_mode_choice)

          # Run game logic
          name, total_time, score = play_game_two(words)

          # Add entry to leaderboard
          leaderboard = load_leaderboard(game_mode_choice)
          leaderboard.append([name, total_time, score])
          leaderboard = refresh_leaderboard(leaderboard)
          save_leaderboard(game_mode_choice, leaderboard)

          print()

          # Show leaderboard
          display_leaderboard(game_mode_choice)

          # Back to Main Menu
          break
        # [3] BACK TO MAIN MENU
        elif game_mode_choice == "3":
          break
        else:
          input("Invalid option. Press ENTER to try again.")
    # [2] VIEW LEADERBOARD
    elif choice == "2":
      while True:
        # Clear console
        cls()

        # Show leaderboard menu
        title = """\033[1;33m
         ___   ___    _  __ __ __ ____ _  __ _____
        / _ \ / _ |  / |/ // //_//  _// |/ // ___/
       / , _// __ | /    // ,<  _/ / /    // (_ / 
      /_/|_|/_/ |_|/_/|_//_/|_|/___//_/|_/ \___/  
        \033[0m"""
        print(title)
        print()
        print("\033[1;33mWhich leaderboard do you want to see?\033[0m")
        print()
        print("[1] Classic Mode")
        print("[2] Slang Mode")
        print("[3] Back to Main Menu")
        print()

        # Ask user input
        leaderboard_choice = input("Enter your choice: ")

        # Check if user input is classic (1) or slang (2)
        if leaderboard_choice == "1" or leaderboard_choice == "2":
          display_leaderboard(leaderboard_choice)
        # Back to Main Menu
        elif leaderboard_choice == "3":
          break
        # Validation
        else:
          print("Invalid choice. Press ENTER to try again.")
          input()

    # [3] EXIT PROGRAM
    elif choice == "3":
      print("\nThanks for playing!")
      sys.exit()
    else:
      input("Invalid option. Press ENTER to try again.")


# Run
main()
