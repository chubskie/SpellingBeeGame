import random, sys, os, time


# Define console clear function
def cls():
  os.system('cls' if os.name == 'nt' else 'clear')


# ================ TITLES ==================
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
  print("\033[1mMAIN MENU\033[0m")
  print("\033[1;33m[1]\033[0m Start Game")
  print("\033[1;33m[2]\033[0m Leaderboards")
  print("\033[1;33m[3]\033[0m Exit")
  print()


def print_second_title():
  cls()
  print("\033[1mChoose Game Mode:\033[0m")
  print("\033[1;33m[1]\033[0m Classic Words")
  print("\033[1;33m[2]\033[0m Slang Words")
  print("\033[1;33m[3]\033[0m Back to Main Menu")
  print()


# ============ RULES ==============
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


def print_game_two_rules():
  cls()
  print("\033[1;33m======= RULES ========\033[0m")
  print("1.) You will be given 10 random slang words.")
  print("2.) Earned correctly spelled word gives you 5 pts.")
  print(
      "3.) After each game, you will be able to see the words you've misspelled."
  )
  print(
      "[4.] Your ranking will be based first on your score, and then on your time."
  )
  print("\033[1;33m======================\033[0m")
  print()


# ============ INITIALIZATION ==============
def choose_random(word_list, size):
  return random.sample(word_list, size)


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

  word_list = random.sample(word_list, len(word_list))

  return word_list


def DEBUG_list_words(word_list):
  for word in word_list:
    print(word)


def DEBUG_leaderboard_info(name, score, total_time):
  print(f"NAME: {name}")
  print(f"SCORE: {score}")
  print(f"TOTAL TIME: {total_time:.2f}")


# ========== LEADERBOARD LOGIC ==============
def load_leaderboard(mode):
  leaderboard = []
  if mode == "1":
    leaderboard_file = open("rankings/leaderboard_one.txt", "r")

    for line in leaderboard_file:
      name, score, total_time = line.strip().split(",")
      leaderboard.append((name, int(score), float(total_time)))

    leaderboard_file.close()
  elif mode == "2":
    leaderboard_file = open("rankings/leaderboard_two.txt", "r")

    for line in leaderboard_file:
      name, score, total_time = line.strip().split(",")
      leaderboard.append((name, int(score), float(total_time)))

    leaderboard_file.close()

  return leaderboard


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
  rank = 1
  for entry in leaderboard:
    print(f"    #{rank:<13}{entry[0]:<14}{entry[2]:<13.2f}{entry[1]:<14}")
    rank += 1
  print()
  input("Press ENTER to exit...")


def save_leaderboard(mode, leaderboard):
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
      if (leaderboard[i][1] < leaderboard[j][1]
          or leaderboard[i][1] == leaderboard[j][1]
          and leaderboard[i][2] > leaderboard[j][2]):
        leaderboard[i], leaderboard[j] = leaderboard[j], leaderboard[i]

  # Get only the top 10
  leaderboard = leaderboard[:10]

  return leaderboard


# ========== GAME LOGIC =============
def add_point(word):
  if len(word) == 3:
    return 2
  elif len(word) == 4:
    return 5
  elif len(word) == 5:
    return 7
  else:
    sys.exit("INVALID LENGTH. PLEASE DEBUG.")


def play_game_one(word_list):
  score = 0
  correct_words_count = 0
  index = 1
  misspelled_words = []
  start_time = time.time()

  for word in word_list:
    cls()
    print(f"\n[{index}/21] Spell the word: \033[1;33m{word}\033[0m\n")
    user_input = input("Answer: ")

    if user_input == word:
      score += add_point(word)
      correct_words_count += 1
    else:
      misspelled_words.append([word, user_input])

    index += 1
  end_time = time.time()

  total_time = end_time - start_time

  print()
  print("=========== RESULTS ===========")
  print(f"Number of Correct Words: {correct_words_count}/21")
  print(f"Total Time: {total_time:.2f} seconds")
  print(f"Score: {score} pts.")
  print()
  if correct_words_count == 21:
    print("YOU GOT A PERFECT SCORE!")
  else:
    print("===== MISSPELLED WORDS ======")
    for word in misspelled_words:
      print(f"{word[0]} (You typed \"\033[0;31m{word[1]}\033[0m\")")
  print()
  while True:
    name = input("Enter your name: ")
    if len(name) != 0:
      break
    else:
      print("Please enter a name.\n")

  return name, score, total_time


def play_game_two(word_list):
  score = 0
  correct_words_count = 0
  index = 1
  misspelled_words = []
  start_time = time.time()

  for word in word_list:
    cls()
    print(f"\n[{index}/10] Spell the word: \033[1;33m{word}\033[0m\n")
    user_input = input("Answer: ")

    if user_input == word:
      score += 5
      correct_words_count += 1
    else:
      misspelled_words.append([word, user_input])

    index += 1
  end_time = time.time()

  total_time = end_time - start_time

  print()
  print("=========== RESULTS ===========")
  print(f"Number of Correct Words: {correct_words_count}/10")
  print(f"Total Time: {total_time:.2f} seconds")
  print(f"Score: {score} pts.")
  print()
  if correct_words_count == 10:
    print("YOU GOT A PERFECT SCORE!")
  else:
    print("===== MISSPELLED WORDS ======")
    for word in misspelled_words:
      print(f"{word[0]} (You typed \"\033[0;31m{word[1]}\033[0m\")")
  print()
  name = input("Enter your name: ")

  return name, score, total_time


def main_menu():
  while True:
    print_title()
    choice = input("Enter your choice: ")

    if choice == "1":
      while True:
        print_second_title()
        game_mode_choice = input("Enter your choice: ")

        if game_mode_choice == "1":
          print_game_one_rules()
          input("Press ENTER to start...")

          words = load_words(game_mode_choice)
          # DEBUG_list_words(words)
          name, score, total_time = play_game_one(words)

          leaderboard = load_leaderboard(game_mode_choice)
          leaderboard.append([name, score, total_time])
          leaderboard = refresh_leaderboard(leaderboard)
          save_leaderboard(game_mode_choice, leaderboard)

          print()
          input("Press ENTER to view leaderboard...")
          display_leaderboard(game_mode_choice)
          break
        elif game_mode_choice == "2":
          print_game_two_rules()
          input("Press ENTER to start...")

          words = load_words(game_mode_choice)
          # DEBUG_list_words(words)
          name, score, total_time = play_game_two(words)

          leaderboard = load_leaderboard(game_mode_choice)
          leaderboard.append([name, score, total_time])
          leaderboard = refresh_leaderboard(leaderboard)
          save_leaderboard(game_mode_choice, leaderboard)

          print()
          input("Press ENTER to view leaderboard...")
          display_leaderboard(game_mode_choice)
          break
        elif game_mode_choice == "3":
          break
        else:
          input("Invalid option. Press ENTER to try again.")
    elif choice == "2":
      while True:
        cls()
        print("Which leaderboard do you want to see?")
        print("[1] Classic Mode")
        print("[2] Slang Mode")
        print("[3] Back to Main Menu")
        print()
        leaderboard_choice = input("Enter your choice: ")

        if leaderboard_choice == "1" or leaderboard_choice == "2":
          display_leaderboard(leaderboard_choice)
        elif leaderboard_choice == "3":
          break
        else:
          display_leaderboard(leaderboard_choice)
    elif choice == "3":
      print("\nThanks for playing!")
      sys.exit()
    else:
      input("Invalid option. Press ENTER to try again.")


# Run
main_menu()
