#!/bin/bash

echo '################################'
echo '#DOSBox Game Launcher v0.1     #'
echo '################################'
echo '#1) Albion                     #'
echo '#2) Master of Orion            #'
echo '#3) Die Siedler II             #'
echo '################################'
echo '#4) exit                       #'
echo '################################'
read -p 'pick your game: ' pick
if [ $pick == '1' ];
then dosbox -conf ~/.dosbox/albion.conf
elif [ $pick == '2' ];
then dosbox -conf ~/.dosbox/moo.conf
elif [ $pick == '3' ];
then dosbox -conf ~/.dosbox/s2.conf
elif [ $pick == '4' ];
then exit
else
echo 'ok, bye!'
fi
