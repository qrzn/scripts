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
echo 'Welcome to Day 2!'
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
press
clear
# ROUND I
echo 'ROUND I'
echo '1.40min plank'
sleep 100
bell
press
echo '2.30 fast punches'
sleep 150
bell
press
echo '15x spartan pushups'
press
echo '50sec wall sit'
sleep 50
bell
press
echo '15x spring ups'
press
echo '45x biceps curls'
press
clear
# ROUND II
echo 'ROUND II'
echo '15x spiderman pushups'
press
echo '15x knees to elbows'
press
echo '15x plank to pushup'
press
echo '15x knee pushups'
press
echo '30x jumping jacks'
press
echo '45x biceps curls'
press
clear
echo 'ROUND III'
echo '20x mountain climbers'
press
echo '15x burpess and hill climbers'
press
echo '15x hollow rocks'
press
echo '15x spiderman pushups'
press
echo '15x burpees'
press
echo '45x biceps curls'
press
clear
echo 'ROUND IV'
echo '15x pushup jumps'
press
echo '15x shin touches'
press
echo '15x hip touches'
press
echo '15x burpees'
press
echo '30x jumping jacks'
press
echo '45x biceps curls'
press
clear
echo 'ROUND V'
echo '2.30mins shadow boxing'
sleep 150
echo 'done'
bell
press
echo '30x bicycle crunches'
press
echo '15x cross legged seated raises'
press
echo '15x spring ups'
press
echo '45x biceps crunches'
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
echo "day 2/21 complete" >| $data/progress.txt
echo "Done! Saved file to /data/progress.txt" 
