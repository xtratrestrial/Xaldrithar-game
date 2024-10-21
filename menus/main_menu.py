import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.utils import fmt, clear
from settings import settings
from chargen import character_creation
def display_ascii_art():

  ascii_art_path = "assets/ascii_splash.txt"

  print("Attempting to display ASCII art...")

  try:
    with open(ascii_art_path, "r") as file:
#      print("File opened successfully.")
      art = file.read()
#      print("File read successfully.")
      print(fmt.yellow(art))

  except FileNotFoundError:
    print(f"Error: Could not find '{ascii_art_path}'.")

  except PermissionError:
    print(f"Error: No permission to read '{ascii_art_path}'.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

def new_game():
  clear()
  character_creation()

def load_game():
  clear()
  print(fmt.dim_green("Loading saved game..."))

def quit_game():
  clear()
  print(fmt.red("You cannot escape your destiny.  You shall return..."))
  exit()

def main_menu():

  clear()

  display_ascii_art()

  print(fmt.red("The Sands of Xaldrithar thirst for blood. Will it be yours?"))

  print(fmt.white("\n\n1. New  Game"))
  print(fmt.green("2. Load Game"))
  print(fmt.br_yellow("3. Settings"))
  print(fmt.cyan("4. Quit\n"))

  actions = {
      "1": new_game,
      "2": load_game,
      "3": settings,
      "4": quit_game
  }


  choice = input(fmt.br_red("\nEnter your choice: "))

  action = actions.get(choice)
  if action:
      action()

  else:
     print(fmt.red("Invalid choice.  Please try again"))
     main_menu()




# keep at end
if __name__ == "__main__":
    main_menu()
