#!/bin/bash
# game wizard, minimal version
# a cli based game launcher
# written by qrzn

# more variables means less code
game="$HOME/Spiele"
txt="$HOME/git/scripts/game-wiz/menus"
data="$HOME/git/scripts/game-wiz/data"
dosbox="$HOME/.dosbox"

# clear terminal
clear
cat $txt/gamewiz.txt
# launch options prompt
PS3="choose game and press ENTER: "

select opt in albion arcanum daggerfall daggerfall-unity emperor fallout falloutnv morrowind moo s2 close; do

case $opt in
	albion)
		clear
		echo "starting: albion" 
		dosbox -conf $dosbox/albion.conf
		exit
		;;
	arcanum)
		clear
		echo "starting: arcanum"
		wine $game/arcanum/arcanum.exe
		exit
		;;
	daggerfall)
		clear
		echo "starting: daggerfall"
		dosbox -conf $dosbox/daggerfall.conf 
		exit
		;;
	daggerfall-unity)
		clear
		echo "starting: daggerfall unity"
		cd $game/dfu/
		./DaggerfallUnity.x86_64
		exit
		;;
	emperor)
		clear
		echo "starting emperor"
		wine $game/arcanum/emperor.exe
		exit
		;;
	fallout2)
		clear
		echo "starting fallout2"
		wine $game/fallout2/fallout2.exe
		exit
		;;
	falloutnv)
		clear
		echo "starting falloutnv"
		wine $game/fnv/FalloutNVLauncher.exe
		exit
		;;
	moo)
		clear
		echo "starting moo"
		dosbox -conf $dosbox/moo.conf
		exit
		;;
	openmw)
		clear
		echo "starting openmw"
		openmw
		exit
		;;
	s2)
		clear
		echo "starting s2"
		dosbox -conf $dosbox/s2.conf
		exit
		;;
	close)
		clear
		echo "the wizard says: goodbye, young apprentice!"
		exit
		;;
	*)
		echo "Invalid option $REPLY"
		;;
esac
done

