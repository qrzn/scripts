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

select opt in "Arena" "Daggerfall" "Master of Orion" "Master of Orion II" "Die Siedler II" "exit"; do

case $opt in
	"Albion")
		clear
		echo "now playing - Albion" 
		dosbox -conf $dosbox/albion.conf
		exit
		;;
	"Arena")
		clear
		echo "now playing - Arena"
		dosbox -conf $dosbox/arena.conf
		exit
		;;
	"Daggerfall")
		clear
		echo "now playing - Daggerfall, old boys version"
		dosbox -conf $dosbox/daggerfall.conf
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

