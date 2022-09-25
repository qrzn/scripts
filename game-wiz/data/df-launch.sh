#!/bin/bash

# game launcher, easy to choose games and make my zshrc a bit smaller
clear
cat /home/jan/git/scripts/game-wiz/menus/df.txt
read -p 'pick your choice and press ENTER (1-4): ' pick
if [ $pick == '1' ];
then clear && echo 'starting: Daggerfall' && dosbox -conf ~/.dosbox/daggerfall.conf
elif [ $pick == '2' ];
then clear && echo 'starting: Daggerfall Unity' && ./Spiele/dfu/DaggerfallUnity.x86_64
elif [ $pick == '3' ];
then dosbox '~/Spiele/daggerfall/DAGHEX.EXE'
elif [ $pick == '4' ];
then clear && sh ./games.sh 
else
read -p 'wrong input, one more try (1-4):' pick
fi
