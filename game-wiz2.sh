#/bin/bash
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

select opt in "Albion" "Arcanum" "Augustus" "Daggerfall" "Daggerfall Unity" "Emperor" "Factorio" "Fallout 2" "Fallout New Vegas" "Morrowind" "Master of Orion" "Master of Orion II" "Die Siedler II" close; do

case $opt in
	"Albion")
		clear
		echo "starting: albion" 
		dosbox -conf $dosbox/albion.conf
		exit
		;;
	"Arcanum")
		clear
		echo "starting: arcanum"
		wine $game/arcanum/arcanum.exe
		exit
		;;
	"Augustus")
		clear
		echo "starting: Augustus"
		augustus-game
		exit
		;;
	"Daggerfall")
		clear
		echo "starting: daggerfall"
		dosbox -conf $dosbox/daggerfall.conf
		exit
		;;
	"Daggerfall Unity")
		clear
		echo "starting: daggerfall"
		cd $game/dfu/
		./DaggerfallUnity.x86_64
		exit
		;;
	"Emperor")
		clear
		echo "starting emperor"
		wine $game/arcanum/emperor.exe
		exit
		;;
	"Factorio")
		clear
		echo "starting Factorio"
		cd $game/factorio/bin/x64
		./factorio
		exit
		;;
	"Fallout 2")
		clear
		echo "starting fallout2"
		wine $game/fallout2/fallout2.exe
		exit
		;;
	"Fallout New Vegas")
		clear
		echo "starting falloutnv"
		cd $game/fnv
		wine nvse_loader.exe
		exit
		;;
	"Master of Orion")
		clear
		echo "starting moo"
		dosbox -conf $dosbox/moo.conf
		exit
		;;
	"Master of Orion II")
		clear
		echo "starting Master of Orion II"
		tclsh $game/mastori2/launcher/install-linux
		dosbox -conf $dosbox/moo.conf
		exit
		;;
	"Morrowind")
		clear
		echo "starting Morrowind"
		openmw
		exit
		;;
	"Die Siedler II")
		clear
		echo "starting Die Siedler II"
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

