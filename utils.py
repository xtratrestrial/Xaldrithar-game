from colorama import init, Fore, Back, Style

# ensures that after printing colored text, the style automatically resets
init(autoreset=True)

class Formatter:

  def red(self,text):
    print(f"{Fore.RED}{text}{Style.RESET_ALL}")

  def green(self,text):
    print(f"{Fore.GREEN}{text}{Style.RESET_ALL}")

  def yellow(self,text):
    print(f"{Fore.YELLOW}{text}{Style.RESET_ALL}")

  def cyan(self,text):
    print(f"{Fore.CYAN}{text}{Style.RESET_ALL}")

  def magenta(self,text):
    print(f"{Fore.MAGENTA}{text}{Style.RESET_ALL}")

  def white(self,text):
    print(f"{Fore.WHITE}{text}{Style.RESET_ALL}")

  def dim(self,text):
    print(f"{Style.DIM}{text}{Style.RESET_ALL}")

  def bright(self,text):
    print(f"{Style.BRIGHT}{text}{Style.RESET_ALL}")

  def normal(self,text):
    print(f"{Style.NORMAL}{text}{Style.RESET_ALL}")

  def br_yellow(self,text):
    print(f"{Fore.YELLOW}{Style.BRIGHT}{text}{Style.RESET_ALL}")

  def br_red(self,text):
    print(f"{Fore.RED}{Style.BRIGHT}{text}{Style.RESET_ALL}")


# If colored backgrounds are wanted later, just use Back.RED etc.

fmt = Formatter()
