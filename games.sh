#!/bin/bash

# game launcher, easy to choose games and make my zshrc a bit smaller
clear
echo '################################'
echo '#   game launcher v0.1         #'
echo '#   by qrzn                    #'
echo '################################'
echo '#   1) Albion                  #'
echo '#   2) Arcanum                 #'
echo '#   3) Daggerfall              #'
echo '#   4) Emperor                 #'
echo '#   5) Morrowind               #'
echo '#   6) Master of Orion         #'
echo '#   7) Die Siedler II          #'
echo '#   8) Return to the Roots     #'
echo '################################'
echo '#   8) exit                    #'
echo '################################'
read -p 'pick your game: ' pick
if [ $pick == '1' ];
then dosbox -conf ~/.dosbox/albion.conf
elif [ $pick == '2' ];
then cd ~/Spiele/arcanum && wine Arcanum.exe
elif [ $pick == '3' ];
then cd ~/Spiele/dfu/ && ./DaggerfallUnity.x86_64
elif [ $pick == '4' ];
then cd ~/Spiele/emperor/ && wine Emperor.exe
elif [ $pick == '5' ];
then openmw-launcher
elif [ $pick == '6' ];
then dosbox -conf ~/.dosbox/moo.conf
elif [ $pick == '7' ];
then dosbox -conf ~/.dosbox/s2.conf
elif [ $pick == '8' ];
then cd ~/Spiele/s2/rttr/bin && ./rttr.sh
elif [ $pick == '9' ];
then exit
else
read -p 'wrong input, try again'
fi
