#!/bin/bash

# siedler 2 starter
clear
cat /home/jan/git/scripts/game-wiz/menus/s2.txt
read -p 'Mal wieder Lust auf eine Runde Siedler? (1-3): ' auswahl
if [ $auswahl == '1' ];
then clear && echo 'starte s2.exe via dosbox..' && dosbox -conf ~/.dosbox/s2.conf
elif [ $auswahl == '2' ];
then clear && echo 'starte Karteneditor' && dosbox -conf ~/.dosbox/s2edit.conf
elif [ $auswahl == '3' ];
then clear && echo 'starte Setup' && dosbox '/home/jan/Spiele/s2/SETUP.EXE'
else
exit
fi
