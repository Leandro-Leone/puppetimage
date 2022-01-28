import time
import os
from colorama import *

os.system("clear")

def run():
 photos = int(input("How many pictures do you want to upload? 1/100 "))

 if photos < 101:
  pass
 else:
  os.system("clear")
  exit(Fore.RED+"MAX uploads is 100")

 for i in range(photos):
   os.system("wget https://www.thispersondoesnotexist.com/image")

def main():
 run()

if __name__ == '__main__':
 main()
