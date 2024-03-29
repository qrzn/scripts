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
echo 'This is a rest day, enjoy your free time!'
press
clear
echo "Well done! You completed the workout for today. See you tomorrow!"
#timer
duration=$(( MINUTES - start ))
echo "SUMMARY"
echo "Your workout took $MINUTES minutes"
echo "You burned $(( $MINUTES * 11 )) calories."
echo "writing progress file..."
echo "day 5/21 complete" >| $data/progress.txt
echo "Done! Saved file to /data/progress.txt" 
