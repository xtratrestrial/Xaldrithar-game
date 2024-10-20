from utils import fmt, clear
import time


def settings():
  clear()
  print(fmt.br_red("\nSettings Menu\n"))
  print(fmt.yellow("1. Audio"))
  print(fmt.yellow("2. Display"))
  print(fmt.yellow("3. Key Bindings"))
  print(fmt.yellow("4. Back to Main Menu"))

  actions = {
      "1": adjust_audio,
      "2": adjust_display,
      "3": adjust_key_bindings,
      "4": return_to_main_menu
  }

  choice = input(fmt.white("Enter your choice: "))
  action = actions.get(choice)

  if action:
      action()
  else:
      print(fmt.red("Invalid choice. Please try again."))
      time.sleep(2)
      clear()
      settings()

def adjust_audio():
  print(fmt.br_red("Need to add Audio Settings Menu."))
  time.sleep(2)
  settings()

def adjust_display():
  print(fmt.red("Need to add Display Settings"))
  time.sleep(2)
  settings()

def adjust_key_bindings():
  print(fmt.red("Need to add Adjusting key bindings..."))
  time.sleep(2)
  settings()

def return_to_main_menu():
  print("Returning to main menu...")
  from menus.main_menu import main_menu
  main_menu()
  print("Back to main menu executed.")


