  #!/bin/bash

# variables
data='/home/jan/git/scripts/wout/data/workout1'

# functions
press (){ 
	read -rsp $'Press any key to continue...\n' -n1 key
}
bell () {
	printf '\a'
}
press
start=$MINUTES
clear
echo 'Welcome to Day 1!'
press
# WARMUP
echo 'WARMUP'
echo '30sec high knees'
sleep 30
bell 
echo '30sec mountain climbers'
sleep 30
bell
echo '30 sec crab walk'
sleep 30
bell
press
clear
# ROUND I
echo 'ROUND I'
echo '20x hip raises'
press
echo '2.30min shadow boxing'
sleep 150
bell
echo 'done'
press
echo '15x leg raises'
press
echo '15x isolated crunches left/right'
press
echo '20x knee kicks'
press
echo '45x biceps curls'
echo 'Round 1 complete!'
press
clear
# ROUND II
echo 'ROUND II'
echo '15x spiderman pushups'
press
echo '15x skater jumps'
press
echo '15x crunches'
press
echo '15x toe touches'
press
echo '2.30mins front rack stretch'
sleep 150
bell
echo 'done'
press
echo '45x biceps curls'
press
echo 'round 2 complete!'
press
clear
# ROUND III
echo 'ROUND III'
echo '20x jump squats'
press
echo '15x lunges'
press
echo '15x knees to elbows'
press
echo '10 dive bombers'
press
echo '15 pushup jumps'
press
echo '45 biceps curls'
press
echo 'ROUND III complete!'
press
clear
# ROUND IV
echo 'ROUND IV'
echo '15x diamond pushups'
press
echo '15x pushups'
press
echo '15x hollow rocks'
press
echo '15 spartan pushups'
press
echo '45 biceps curls'
press
echo 'ROUND IV complete!'
press
clear
# ROUND V
echo 'ROUND V'
echo '15x crab walk'
press
echo '30x high knees'
press
echo '20x lunges'
press
echo '15x leg raises'
press
echo '30x biceps curls'
press
clear
echo 'STRETCHING'
press
echo ' 30 sec straddle stretch'
sleep 30
bell
echo '30 sec front rack stretch'
sleep 30
bell
echo ' 30 sec straddle stretch'
sleep 30
bell
echo '30 sec front rack stretch'
sleep 30
bell
echo "Well done! You completed the workout for today. See you tomorrow!"
press
clear

#timer
duration=$(( MINUTES - start ))
echo "SUMMARY"
echo "Your workout took $MINUTES minutes"
echo "You burned $(( $MINUTES * 11 )) calories."
echo "writing progress file..."
echo "day 1/21 complete" >| $data/progress.txt
echo "Done! Saved file to /data/progress.txt" 
