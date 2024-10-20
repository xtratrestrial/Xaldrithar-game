import os

def display_ascii_art():

  ascii_art_path = "assets/ascii_splash.txt"
  
  print("Attempting to display ASCII art...")
  
  try:
    with open(ascii_art_path, "r") as file:
      print("File opened successfully.")
      art = file.read()
      print("File read successfully.")
      print(art)

  except FileNotFoundError:
    print(f"Error: Could not find '{ascii_art_path}'.")

  except PermissionError:
    print(f"Error: No permission to read '{ascii_art_path}'.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")


def main_menu():

  display_ascii_art()
  print("\n\033[31mThe Sands of Xaldrithar thirst for blood. Will it be yours?")
  print("1. New  Game")
  print("2. Load Game")
  print("3. Settings")
  print("4. Quit")


if __name__ == "__main__":
    main_menu()
