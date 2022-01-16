import os

os.system("clear")
photos = int(input("How many pictures do you want to upload? 1/100 "))

while photos < 100:
  os.system("wget https://www.thispersondoesnotexist.com/image")
  photos = photos - 1
  if photos == 0:
   print('hey') 
   break
  #else:
   #continue

