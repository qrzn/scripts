#!/bin/bash

# more variables means less code
game='/home/jan/Spiele/'
wizard='sh /home/jan/git/scripts/game-wiz/games.sh'
txt='/home/jan/git/scripts/game-wiz/menus'
data='/home/jan/git/scripts/game-wiz/data'
# game launcher, easy to choose games and make my zshrc a bit smaller

clear
cat $txt/fallout.txt
read -p 'pick your choice and press ENTER (1-): ' pick
if [ $pick == '1' ];
then clear && echo 'starting fallout 2' && cd $game/fallout2/ && wine fallout2.exe && $wizard
elif [ $pick == '2' ];
then clear && echo 'starting falloutnv' && cd $game/fnv/ && wine FalloutNVLauncher.exe && sh $wizard
elif [ $pick == '3' ];
then clear && sh $wizard 
else
read -p 'By the Hoarfather! one more try (1-3):' pick
fi
