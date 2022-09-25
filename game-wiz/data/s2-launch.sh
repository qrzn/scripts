#!/bin/bash

# game launcher, easy to choose games and make my zshrc a bit smaller
clear
echo '################################'
echo '#        Die Siedler ][        #'
echo '#         Gold Edition         #'
echo '################################'
echo '#          DOS Version         #' 
echo '################################'
echo '#  1) game                     #'
echo '#  2) editor                   #'
echo '#  3) setup                    #'
echo '################################'
echo '#     Return to the Roots      #'
echo '################################'
echo '#  4) game                     #'
echo '#  5) editor                   #'
echo '################################'
echo '#  6) exit                     #'
echo '################################'
echo ''
echo 'Welcome, young adventurer'
read -p 'pick your choice and press ENTER (1-4): ' pick
if [ $pick == '1' ];
then dosbox -conf ~/.dosbox/s2.conf
elif [ $pick == '2' ];
then dosbox -conf ~/.dosbox/s2-edit.conf
elif [ $pick == '3' ];
then dosbox '/home/jan/Spiele/s2/SETUP.EXE'
elif [ $pick == '4' ];
then sh '/home/jan/Spiele/s2/rttr/bin/rttr.sh'
elif [ $pick == '5' ];
then sh '/home/jan/Spiele/s2/rttr/bin/editor'
elif [ $pick == '6' ];
then clear && sh ./games.sh 
else
read -p 'wrong input, one more try (1-4):' pick
fi
