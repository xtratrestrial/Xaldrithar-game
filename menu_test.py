asci_art_path = "assets/ascii_splash.txt"

open(ascii_art_path,"r") as file:
  art = file.read()
  print(art)
