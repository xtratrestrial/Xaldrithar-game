import os
import time
import yaml
from utils.utils import fmt, clear

def character_creation():
  clear()
  print(fmt.bright("\n=== Welcome to the World of ") + fmt.yellow("Xaldrithar") + " ===\n")

  characters_dir = "characters"
  if not os.path.exists(characters_dir):
      os.makedirs(characters_dir)

  character_data = {}

  character_name = input(fmt.green("What is your name, Hero?"))
  character_data["name"] = character_name
  character_file = os.path.join(characters_dir,character_name + ".yaml")

  print(fmt.green("\nChoose your class:\n"))
  print(fmt.red("1. Fighter"))
  print(fmt.magenta("2. Mage"))
  print(fmt.dim_blue("3. Rogue"))

  class_choice = input(fmt.dim("\nEnter your choice: "))
  character_class = None

  if class_choice == "1":
      character_class = "Warrior"
  elif class_choice == "2":
      character_class = "Mage"
  elif class_choice == "3":
      character_class = "Rogue"
  else:
      print(fmt.red("Invalid Choice."))
      # break
      # need to restart character_creation to redisplay options - how?

  character_data["class"] = character_class


  with open(character_file, 'w') as file:
      yaml.dump(character_data, file, default_flow_syle=False)

  print(fmt.bright("\nCharacter Creation Summary:"))
  print(fmt.green(f"Name: {character_name}"))
  print(fmt.green(f"Class: {character_class}"))
  print(fmt.green(f"Abilities: {character_data['abilities']}"))
  time.sleep(5)
