#/bin/bash
# game wizard, minimal version
# a cli based game launcher
# written by qrzn

display_center(){
    columns="$(tput cols)"
    while IFS= read -r line; do
        printf "%*s\n" $(( (${#line} + columns) / 2)) "$line"
    done < "$1"
}

# more variables means less code
game="$HOME/Spiele"
txt="$HOME/git/scripts/game-wiz"
dosbox="$HOME/.dosbox"

# clear terminal
clear
display_center "$txt/wiz.txt"
# launch options prompt
PS3="choose game and press ENTER: "

select opt in "Albion" "Arena" "Arcanum" "Augustus" "Daggerfall" "Daggerfall Unity" "Emperor" "Factorio" "Fallout" "Fallout 2" "Fallout New Vegas" "Morrowind" "Master of Orion" "Master of Orion II" "Die Siedler II" "exit"; do

case $opt in
	"Albion")
		clear
		echo "now playing - Albion" 
		dosbox -conf $dosbox/albion.conf
		exit
		;;
	"Arcanum")
		clear
		echo "now playing - Arcanum"
		wine $game/arcanum/arcanum.exe
		exit
		;;
	"Arena")
		clear
		echo "now playing - Arena"
		dosbox -conf $dosbox/arena.conf
		exit
		;;
	"Augustus")
		clear
		echo "now playing - Augustus"
		augustus-game
		exit
		;;
	"Daggerfall")
		clear
		echo "now playing - Daggerfall, old boys version"
		dosbox -conf $dosbox/daggerfall.conf
		exit
		;;
	"Daggerfall Unity")
		clear
		echo "now playing - daggerfall, kiddie version"
		cd $game/dfu/
		./DaggerfallUnity.x86_64
		exit
		;;
	"Emperor")
		clear
		echo "now playing - emperor"
		wine $game/arcanum/emperor.exe
		exit
		;;
	"Factorio")
		clear
		echo "now playing - Factorio"
		cd $game/factorio/bin/x64
		./factorio
		exit
		;;
	"Fallout")
		clear
		echo "now playing - Fallout"
		cd $game/fallout/
		wine falloutw.exe
		exit
		;;
	"Fallout 2")
		clear
		echo "now playing - Fallout 2"
		cd $game/fallout2/
		wine fallout2.exe
		exit
		;;
	"Fallout New Vegas")
		clear
		echo "now playing - Fallout - New Vegas"
		cd $game/fnv
		wine nvse_loader.exe
		exit
		;;
	"Master of Orion")
		clear
		echo "now playing - Master of Orion"
		dosbox -conf $dosbox/moo.conf
		exit
		;;
	"Master of Orion II")
		clear
		echo "now playing - Master of Orion II - Battle at Antares"
		dosbox -conf $dosbox/moo2.conf
		exit
		;;
	"Morrowind")
		clear
		echo "now playing - Morrowind"
		openmw
		exit
		;;
	"Die Siedler II")
		clear
		echo "now playing - Die Siedler II - Gold Edition"
		dosbox -conf $dosbox/s2.conf
		exit
		;;
        "exit")
		clear
		echo "the wizard says: goodbye, young apprentice!"
		exit
		;;
	*)
		echo "Invalid option $REPLY"
		;;
esac
done

