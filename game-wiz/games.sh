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

select opt in "Albion" "Caster of Magic" "Commander Keen" "Darklands" "Daggerfall" "Daggerfall - Unity" "Emperor" "Exult" "Die Siedler II" "Ultima Underworld II" "Widelands" "exit"; do

case $opt in
	"Albion")
		clear
		echo "now playing - Albion" 
		dosbox -conf $dosbox/albion.conf
		exit
		;;
	"Caster of Magic")
		clear
		echo "now playing - Caster of Magic"
		dosbox -conf $dosbox/com.conf
		exit
		;;
	"Commander Keen")
		clear
		echo "now playing - Commander Keen"
		dosbox -conf $dosbox/keen.conf
		exit
		;;
	"Daggerfall")
		clear
		echo "now playing - Daggerfall, old boys version"
		dosbox -conf $dosbox/fall.conf
		exit
		;;
	"Daggerfall - Unity")
		clear
		echo "now playing - Daggerfall - Unity"
		$game/dfu/DaggerfallUnity.x86_64
		exit
		;;
	"Emperor")
		clear
		echo "now playing - emperor"
		wine $game/emperor/Emperor.exe
		exit
		;;
	"Exult")
		clear
		echo "now playing - exult"
		exult
		exit
		;;
	"Die Siedler II")
		clear
		echo "now playing - Die Siedler II - Gold Edition"
		dosbox -conf $dosbox/s2.conf
		exit
		;;
	"Widelands")
		clear
		echo "now playing - Widelands"
		widelands
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

