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
echo 'Welcome to Day 4!'
press
# WARMUP
echo 'WARMUP'
echo '30sec high knees'
sleep 30
bell 
echo '30sec mountain climbers'
sleep 30
bell
echo '30sec crab walk'
sleep 30
bell
echo 'warmup done'
press
clear
# ROUND I
echo 'ROUND I'
echo '15x lunges'
press
echo '20x mountain climbers'
press
echo '20x jump squats'
press
echo '15x leg raises'
press
echo '15x v ups'
press
echo '34x biceps curls'
press
clear
echo 'ROUND II'
echo '15x hollow rocks'
press
echo '15x knee pushups'
press
echo '2.30mins fast punches'
sleep 150
bell
echo 'done'
press
echo '2.30 downward dog'
sleep 150
bell
echo 'done'
press
echo '15x bauch rein raus'
press
echo '45x biceps curls'
press
clear
echo 'ROUND III'
echo '15x crunches'
press
echo '15x tuck jumps'
press
echo '15x pushups'
press
echo '1.40mins plank'
sleep 100
echo 'done'
press
echo '15x knees to elbow'
press
echo '45x biceps curls'
press
clear
echo 'ROUND IV'
echo '50 sec wall sit'
sleep 50
bell
press
echo '15x toe touches'
press
echo '15x diamond pushups'
press
echo '15x spiderman pushups'
press
echo '2.30 mins straddle stretch'
sleep 150
bell
echo 'done'
press
echo '45x biceps curls'
press
clear
echo 'ROUND V'
echo '15x plank to pushup'
press
echo '20x knee kicks'
press
echo '2.30 mins front rack stretch'
sleep 150
bell
echo 'done'
press
echo '15x knees to elbows'
press
echo '15x isolated crunches left right'
press
echo '45x biceps curls'
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
press
clear
echo "Well done! You completed the workout for today. See you tomorrow!"
#timer
duration=$(( MINUTES - start ))
echo "SUMMARY"
echo "Your workout took $MINUTES minutes"
echo "You burned $(( $MINUTES * 11 )) calories."
echo "writing progress file..."
echo "day 4/21 complete" >| $data/progress.txt
echo "Done! Saved file to /data/progress.txt" 
