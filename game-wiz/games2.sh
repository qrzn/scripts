#!/bin/bash

# game wizard, minimal version
# a cli based game launcher
# written by qrzn
# more variables means less code
game='/home/jan/spiele/'
txt='/home/jan/git/scripts/game-wiz/menus/'
data='/home/jan/git/scripts/game-wiz/data/'

clear
cat $txt/darkcastle.txt
read -p 'Dost thou really wish entering the Dark Keep of Gaming? (y/n) ' yn 
if [ $yn == 'y' ];
	then clear && cat $txt/main2.txt
elif [ $yn == 'n' ];
	then $wizard
else
	echo 'I understand, this is not a place for the Faint of Heart.'
fi
PS3="choose thy game: "

# launch options prompt
select opt in albion arcanum daggerfall emperor fallout morrowind moo close; do

case $opt in
	albion)
		clear
		echo 'starting: albion' 
		dosbox -conf ~/.dosbox/albion.conf
		;;
	arcanum)
		clear
		echo 'starting: arcanum'
		wine $game/arcanum/arcanum.exe
		;;
	daggerfall)
		clear
		echo 'starting: daggerfall'
		sh $data/df-launch.sh
		;;
	emperor)
		clear
		echo 'starting emperor'
		wine $game/arcanum/emperor.exe
		;;
	fallout)
		clear
		sh $data/fallout.sh
		;;
	moo)
		clear
		echo 'starting moo'
		dosbox -conf ~/.dosbox/moo.conf
		;;
	openmw)
		clear
		echo 'starting openmw'
		openmw
		;;
	s2)
		clear
		sh $data/s2-launch.sh
		;;
	close)
		exit
		;;
	*)
	echo "Invalid option $REPLY"
	;;
esac
done

