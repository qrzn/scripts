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
echo 'Welcome to Day 3!'
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
