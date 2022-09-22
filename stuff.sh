#!/bin/bash

# game launcher, easy to choose games and make my zshrc a bit smaller
clear
echo '################################'
echo '#  game wizard                 #'
echo '#                    ~ by qrzn #'
echo '################################'
echo '#  1) albion           ,    _  #'
echo '#  2) arcanum         /|   | | #'
echo '#  3) daggerfall    _/_\_  >_< #'
echo '#  4) emperor      .-\-/.   |  #'
echo '#  5) openmw      /  | | \_ |  #'
echo '#  6) moo         \ \| |\__(|  #'
echo '#  7) s2          /\`---/   |  #'
echo '#  8) dfu         / /   \   |  #'
echo '################################'
echo '#  9) exit                     #'
echo '################################'
echo '                                '
echo 'Welcome, young apprentice'
read -p 'pick your game and press ENTER (1-9): ' pick
if [ $pick == '1' ];
then dosbox -conf ~/.dosbox/albion.conf
elif [ $pick == '2' ];
then cd ~/Spiele/arcanum && wine Arcanum.exe
elif [ $pick == '3' ];
then dosbox -conf ~/.dosbox/daggerfall.conf
elif [ $pick == '4' ];
then cd ~/Spiele/emperor/ && wine Emperor.exe
elif [ $pick == '5' ];
then openmw-launcher
elif [ $pick == '6' ];
then dosbox -conf ~/.dosbox/moo.conf
elif [ $pick == '7' ];
then dosbox -conf ~/.dosbox/s2.conf
elif [ $pick == '8' ];
then cd ~/Spiele/dfu/ && ./DaggerfallUnity.x86_64
elif [ $pick == '9' ];
then clear && echo 'the wizard says: goodbye, apprentice..'
else
read -p 'wrong input, one more try (1-9):' pick
fi
