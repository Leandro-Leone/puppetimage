#!/usr/bin/python3
#
# puppet.py - Download png files automatically 
#
# Made by: leandro.sh
# Manutention: leandro.sh
#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# This program was made to OSINT purpose. I was making a sock puppet to gathe users informations, but I would need to crete more than 10 puppets, and I 
# automated the part of download of the fake person to use it. At the beginning I was getinng the fake person from 
# https://www.thispersondoesnotexist.com/image.
#
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#
# History:
#
#  v1.0 leandro.sh:
#    - Created the Script
#  v1.1 17-07-2022, leandro.sh:
#    - Adding comments
#    - Making the script a program
#    - Organazing the code
#
#
# License: GNU GENERAL PUBLIC LICENSE
#
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#
#                     /|      __
#*             +      / |   ,-~ /             +
#     .              Y :|  //  /                .         *
#         .          | jj /( .^     *
#               *    >-"~"-v"              .        *        .
#*                  /       Y
#   .     .        jo  o    |     .            +
#                 ( ~T~     j                     +     .
#      +           >._-' _./         +
#               /| ;-"~ _  l
#  .           / l/ ,-"~    \     +
#              \//\/      .- \
#       +       Y        /    Y
#               l       I     !
#               ]\      _\    /"\
#              (" ~----( ~   Y.  )
#          ~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#               Se nada coletou nada analisará - Bruno Fraga - If nothing has collected nothing will analyze     
#
#

#importing Modules

import os
from colorama import *

os.system("clear")

########################################################################
# Defining the "Run" Function where the user will choose the quantity  #
# of images to download and then execute the command to get it from:   #
#  - https://www.thispersondoesnotexist.com/image                      #
#                                                                      #
#########################################################################

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
