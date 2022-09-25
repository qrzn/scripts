#!/bin/bash

# game wizard, v0.3
# a cli based game launcher
# written by qrzn

# clear the terminal for the display of the glorious menu
clear
# print menu with cat
cat /home/jan/git/scripts/game-wiz/menus/main.txt
# launch options prompt
read -p 'pick your game and press ENTER (1-9): ' pick

# selector
#just copy one of those lines, add a numer and continue the list, don't forget to change main.txt accordingly, though
# idea: automate the process of menu editing in the future?

# Albion
if [ $pick == '1' ];
then clear && echo 'starting: Albion' && dosbox -conf ~/.dosbox/albion.conf
# Arcanum
elif [ $pick == '2' ];
then clear && echo 'starting: Arcanum' && cd ~/Spiele/arcanum && wine Arcanum.exe
# Daggerfall
elif [ $pick == '3' ];
then sh /home/jan/git/scripts/game-wiz/data/df-launch.sh  
# Emperor - Rise of the Middle Kingdom
elif [ $pick == '4' ];
then clear && echo 'starting: Emperor - Rise of the Middle Kingdom' && cd ~/Spiele/emperor/ && wine Emperor.exe
# OpenMW
elif [ $pick == '5' ];
then clear && echo 'starting: OpenMW' && openmw-launcher
# Master of Orion
elif [ $pick == '6' ];
then clear && echo 'starting: Master of Orion' && dosbox -conf ~/.dosbox/moo.conf
# The Settlers 2 & Return to the Roots
elif [ $pick == '7' ];
then sh /home/jan/git/scripts/game-wiz/data/s2-launch.sh  
# Fallout - New Vegas
elif [ $pick == '8' ];
then clear && echo 'starting: Fallout - New Vegas' && cd '/home/jan/Spiele/fnv' && wine FalloutNV.exe 
# goodbye message
elif [ $pick == '9' ];
then clear && echo 'the wizard says: goodbye, apprentice..'
else
# will be printed if wrong output is given the first time, closes the script the second time
read -p 'wrong input, one more try (1-9):' pick
fi
