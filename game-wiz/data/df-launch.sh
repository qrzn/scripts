#!/bin/bash

# game launcher, easy to choose games and make my zshrc a bit smaller
clear
cat /home/jan/git/scripts/game-wiz/menus/df.txt
read -p 'pick your choice and press ENTER (1-5): ' pick
if [ $pick == '1' ];
then clear && echo 'starting: Daggerfall' && dosbox -conf ~/.dosbox/daggerfall.conf
elif [ $pick == '2' ];
then clear && echo 'starting: Daggerfall SETUP.EXE' && dosbox '~/Spiele/daggerfall/SETUP.EXE'  && sh '/home/jan/git/scripts/game-wiz/data/df-launcher.sh'
elif [ $pick == '3' ];
then dosbox '~/Spiele/daggerfall/DAGHEX.EXE'
elif [ $pick == '4' ];
then clear && echo 'starting: Daggerfall Unity' && cd /home/jan/Spiele/dfu/ && ./DaggerfallUnity.x86_64 && sh '/home/jan/git/scripts/game-wiz/data/exit.sh'
elif [ $pick == '5' ];
then clear && sh ./games.sh 
else
read -p 'By the Hoarfather! one more try (1-5):' pick
fi
