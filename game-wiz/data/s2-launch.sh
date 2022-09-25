#!/bin/bash

# game launcher, easy to choose games and make my zshrc a bit smaller
clear
cat /home/jan/git/scripts/game-wiz/menus/s2.txt
read -p 'pick your choice and press ENTER (1-6): ' pick
if [ $pick == '1' ];
then clear && echo 'starting: Die Siedler ][ - Gold Edition' && dosbox -conf ~/.dosbox/s2.conf
elif [ $pick == '2' ];
then clear && echo 'starting: Die Siedler ][ - Mapeditor' && dosbox -conf ~/.dosbox/s2edit.conf
elif [ $pick == '3' ];
then clear && echo 'starting: Die Siedler ][ - Setup' && dosbox '/home/jan/Spiele/s2/SETUP.EXE'
elif [ $pick == '4' ];
then clear && echo 'starting: Return to the Roots' && sh '/home/jan/Spiele/s2/rttr/bin/rttr.sh'
elif [ $pick == '5' ];
then clear && echo 'starting: Return to the Roots - Mapeditor'sh '/home/jan/Spiele/s2/rttr/bin/editor'
elif [ $pick == '6' ];
then clear && sh ./games.sh 
else
read -p 'wrong input, one more try (1-4):' pick
fi
