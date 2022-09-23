#!/bin/bash

# game launcher, easy to choose games and make my zshrc a bit smaller
clear
echo '################################'
echo '#  daggerfall launcher         #'
echo '#                    ~ by qrzn #'
echo '################################'
echo '#  1) DOS Version              #' 
echo '#  2) Unity                    #'
echo '#  3) daghex                   #'
echo '################################'
echo '#  4) exit                     #'
echo '################################'
echo '                                '
echo 'Welcome, young adventurer'
read -p 'pick your choice and press ENTER (1-4): ' pick
if [ $pick == '1' ];
then dosbox -conf ~/.dosbox/daggerfall.conf
elif [ $pick == '2' ];
then cd ~/Spiele/dfu/ && ./DaggerfallUnity.x86_64
elif [ $pick == '3' ];
then dosbox '~/Spiele/daggerfall/DAGHEX.EXE'
elif [ $pick == '4' ];
then clear && sh ./games.sh 
else
read -p 'wrong input, one more try (1-4):' pick
fi
