from utils import fmt, clear

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
      "3": main_menu
  }

  choice = input(fmt.white("Enter your choice: "))
  action = actions.get(choice)

  if action:
      action()
  else:
      print(fmt.red("Invalid choice. Please try again."))
      clear()
      settings()

def adjust_audio:
  print(fmt.yellow("Need to add Audio Settings Menu.")
  settings()

def adjust_display:
  print(fmt.yellow("Need to add Display Settings")
  settings()

def adjust_key_bindings():
  print(fmt.yellow("Need to add Adjusting key bindings...")
  settings()

def back_to_main_menu():
  from main_menu import main_menu
  main_menu()


