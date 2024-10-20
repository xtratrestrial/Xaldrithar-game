from colorama import init, Fore, Back, Style

# ensures that after printing colored text, the style automatically resets
init(autoreset=True)

class Formatter:

  def red(self,text):
    return f"{Fore.RED}{text}{Style.RESET_ALL}"

  def green(self,text):
    return f"{Fore.GREEN}{text}{Style.RESET_ALL}"

  def yellow(self,text):
    return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"

  def cyan(self,text):
    return f"{Fore.CYAN}{text}{Style.RESET_ALL}"

  def magenta(self,text):
    return f"{Fore.MAGENTA}{text}{Style.RESET_ALL}"

  def white(self,text):
    return f"{Fore.WHITE}{text}{Style.RESET_ALL}"

  def normal(self,text):
    return f"{Style.NORMAL}{text}{Style.RESET_ALL}"

# Brights

  def bright(self,text):
    return f"{Style.BRIGHT}{text}{Style.RESET_ALL}"

  def br_yellow(self,text):
    return f"{Fore.YELLOW}{Style.BRIGHT}{text}{Style.RESET_ALL}"

  def br_red(self,text):
    return f"{Fore.RED}{Style.BRIGHT}{text}{Style.RESET_ALL}"

# Dims

  def dim(self,text):
    return f"{Style.DIM}{text}{Style.RESET_ALL}"

  def dim_green(self,text):
    return f"{Fore.GREEN}{Style.DIM}{text}{Style.RESET_ALL}"


# If colored backgrounds are wanted later, just use Back.RED etc.

fmt = Formatter()

# clear screen

# import only system from os
from os import system, name

# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


