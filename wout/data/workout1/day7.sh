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
echo 'Welcome to Day 7!'
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
echo '15x knees to elbows'
press
echo '30x high knees'
press
echo '20x hip raises'
press
echo '15x diamond pushups'
press
echo '2.30 mins downward dog'
sleep 150
bell
echo 'done'
press
echo '45x biceps curls'
press
clear
echo 'ROUND II'
echo '15x isolated crunches left right'
press
echo '15x spartan pushups'
press
echo '20x knee kicks'
press
echo '15x crunch and punch'
press
echo '15x bauch raus rein'
press
echo '45 biceps curls'
press
clear
echo 'ROUND III'
echo '2.30 fast punches'
sleep 150
bell
echo 'done'
press
echo '30x bicycle crunches'
press
echo '20x mountain climbers'
press
echo '2.30 mins front rack stretch'
sleep 150
bell
echo 'done'
press
echo '10x jumping lunges'
press
echo '45x biceps curls'
press
clear
echo 'ROUND IV'
echo '2.30 mins shadow boxing'
sleep 150
bell
echo 'done'
press
echo '15x hollow rocks'
press
echo '15x hip touches'
press
echo '20x hip raises'
press
echo '15x sprawls'
press
echo '45x biceps curls'
press
clear
echo 'ROUND V'
echo '15x leg raises'
press
echo '15x prisoner squats'
press
echo '15x diamond pushups'
press
echo '15x pushups'
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
echo "day 6/21 complete" >| $data/progress.txt
echo "Done! Saved file to /data/progress.txt" 
