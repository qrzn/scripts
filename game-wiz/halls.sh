#!/bin/bash

# game wizard, v0.3
# a cli based game launcher
# written by qrzn

# variables, less text
dao='/home/jan/git/scripts/game-wiz/'
game='/home/jan/Spiele/'

# clear the terminal for the display of the glorious menu
# print menu with cat
clear
cat $dao/menus/darkcastle.txt
# launch options prompt
read -p 'Dost thou really wish entering the Dark Keep of Gaming? (y/n) ' yn 
if [ $yn == 'y' ];
then clear && cat $dao/menus/halls.txt
elif [ $yn == 'n'];
then sh $dao/games.sh
else
echo 'I understand, this is not a place for the Faint of Heart.'
fi
read -p 'Dost thou wish to read the parchment? (y/n) ' ny
if [ $ny == 'y' ];
then clear && cat $dao/menus/main.txt
elif [ $ny == 'n' ];
then sh $dao/games.sh
else
echo 'Thou art a Fool! Have at Thee!'
fi
# launch options prompt
read -p 'Pick thy game most vigilantly my Lord (1-9): ' pick

# selector
#just copy one of those lines, add a numer and continue the list, don't forget to change main.txt accordingly, though
# idea: automate the process of menu editing in the future?

# Albion
if [ $pick == '1' ];
then clear && echo 'starting: Albion' && dosbox -conf ~/.dosbox/albion.conf
# Arcanum
elif [ $pick == '2' ];
then clear && echo 'starting: Arcanum' && cd $game/arcanum && wine Arcanum.exe
# Daggerfall
elif [ $pick == '3' ];
then sh pts/game-wiz/data/df-launch.sh  
# Emperor - Rise of the Middle Kingdom
elif [ $pick == '4' ];
then clear && echo 'starting: Emperor' && wine $game/emperor/Emperor.exe
# OpenMW
elif [ $pick == '5' ];
then clear && echo 'starting: OpenMW' && openmw-launcher
# Master of Orion
elif [ $pick == '6' ];
then clear && echo 'starting: Master of Orion' && dosbox -conf ~/.dosbox/moo.conf
# The Settlers 2 & Return to the Roots
elif [ $pick == '7' ];
then sh $dao/data/s2-launch.sh  
# Fallout - New Vegas
elif [ $pick == '8' ];
then clear && echo 'starting: Fallout - New Vegas' && wine $game/fnv/FalloutNV.exe 
# goodbye message
elif [ $pick == '9' ];
then clear && echo 'the wizard says: goodbye, apprentice..'
else
# will be printed if wrong output is given the first time, closes the script the second time
read -p 'wrong input, one more try (1-9):' pick
fi
