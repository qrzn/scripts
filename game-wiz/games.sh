#!/bin/bash

# game wizard, v0.3
# a cli based game launcher
# written by qrzn

# more variables means less code
game='/home/jan/Spiele/'
wizard='sh /home/jan/git/scripts/game-wiz/games.sh'
txt='/home/jan/git/scripts/game-wiz/menus/'
data='/home/jan/git/scripts/game-wiz/data/'

# clear the terminal for the display of the glorious menu with cat, meow!
clear
cat $txt/darkcastle.txt
# launch options prompt
read -p 'Dost thou really wish entering the Dark Keep of Gaming? (y/n) ' yn 
if [ $yn == 'y' ];
then clear && cat $txt/main.txt
elif [ $yn == 'n' ];
then $wizard
else
echo 'I understand, this is not a place for the Faint of Heart.'
fi

# launch options prompt
read -p 'pick your game and press ENTER (1-9): ' pick

# selector
# Albion
if [ $pick == '1' ];
then clear && echo 'starting: Albion' && dosbox -conf ~/.dosbox/albion.conf
# Arcanum
elif [ $pick == '2' ];
then clear && echo 'starting: Arcanum' && wine $game/arcanum/Arcanum.exe
# Daggerfall
elif [ $pick == '3' ];
then sh $data/df-launch.sh  
# Emperor - Rise of the Middle Kingdom
elif [ $pick == '4' ];
then clear && echo 'starting: Emperor' && wine $game/emperor/Emperor.exe
# OpenMW
elif [ $pick == '5' ];
then clear && echo 'starting: Master of Orion' && dosbox -conf ~./dosbox/moo.conf
# Master of Orion
elif [ $pick == '6' ];
then clear && echo 'starting: OpenMW' && openmw-launcher
# The Settlers 2 & Return to the Roots
elif [ $pick == '7' ];
then sh $data/s2-launch.sh  
# Fallout 
elif [ $pick == '8' ];
then sh $data/fallout.sh
# goodbye message
elif [ $pick == '9' ];
then clear && echo 'the wizard says: goodbye, apprentice..'
else $wizard
fi
