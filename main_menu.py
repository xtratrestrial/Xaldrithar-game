import os

from utils import fmt

def display_ascii_art():

  ascii_art_path = "assets/ascii_splash.txt"
  
  print("Attempting to display ASCII art...")
  
  try:
    with open(ascii_art_path, "r") as file:
#      print("File opened successfully.")
      art = file.read()
#      print("File read successfully.")
      fmt.yellow(art)

  except FileNotFoundError:
    print(f"Error: Could not find '{ascii_art_path}'.")

  except PermissionError:
    print(f"Error: No permission to read '{ascii_art_path}'.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")


def main_menu():

  display_ascii_art()
  fmt.red("The Sands of Xaldrithar thirst for blood. Will it be yours?")

  fmt.white("\n\n1. New  Game")
  fmt.green("2. Load Game")
  fmt.br_yellow("3. Settings")
  fmt.cyan("4. Quit\n")


if __name__ == "__main__":
    main_menu()
