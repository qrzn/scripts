#!/bin/bash

data='/home/jan/git/scripts/wout/data/workout1/'
anykey="read -rsp $'Press any key to continue...\n' -n1 key"
start=$MINUTES
clear
echo 'Welcome to Day 1!'
read -rsp $'Press any key to continue...\n' -n1 key

# ROUND ONE
# first excercise
echo 'WARMUP'
echo '30sec high knees'
sleep 30
echo '30sec mountain climbers'
sleep 30
echo '30 sec crab walk'
sleep 30
read -rsp $'Press any key to continue...\n' -n1 key
clear
echo 'ROUND I'
echo '20x hip raises'
read -rsp $'Press any key to continue...\n' -n1 key
echo '2.30min shadow boxing'
sleep 150
echo 'done'
read -rsp $'Press any key to continue...\n' -n1 key
echo '15x leg raises'
read -rsp $'Press any key to continue...\n' -n1 key
echo '15x isolated crunches left/right'
read -rsp $'Press any key to continue...\n' -n1 key
echo '20x knee kicks'
read -rsp $'Press any key to continue...\n' -n1 key
echo '45x biceps curls'
echo 'Round 1 complete!'
read -rsp $'Press any key to continue...\n' -n1 key
clear
echo 'ROUND II'
echo '15x spiderman pushups'
read -rsp $'Press any key to continue...\n' -n1 key
echo '15x skater jumps'
read -rsp $'Press any key to continue...\n' -n1 key
echo '15x crunches'
read -rsp $'Press any key to continue...\n' -n1 key
echo '15x toe touches'
read -rsp $'Press any key to continue...\n' -n1 key
echo '2.30mins front rack stretch'
sleep 150
echo 'done'
read -rsp $'Press any key to continue...\n' -n1 key
echo '45x biceps curls'
read -rsp $'Press any key to continue...\n' -n1 key
echo 'round 2 complete!'
read -rsp $'Press any key to continue...\n' -n1 key
clear
echo 'ROUND III'
echo '20x jump squats'
read -rsp $'Press any key to continue...\n' -n1 key
echo '15x lunges'
read -rsp $'Press any key to continue...\n' -n1 key
echo '15x knees to elbows'
read -rsp $'Press any key to continue...\n' -n1 key
echo '10 dive bombers'
read -rsp $'Press any key to continue...\n' -n1 key
echo '15 pushup jumps'
read -rsp $'Press any key to continue...\n' -n1 key
echo '45 biceps curls'
read -rsp $'Press any key to continue...\n' -n1 key
echo 'ROUND III complete!'
read -rsp $'Press any key to continue...\n' -n1 key
clear
echo 'ROUND IV'
echo '15x diamond pushups'
read -rsp $'Press any key to continue...\n' -n1 key
echo '15x pushups'
read -rsp $'Press any key to continue...\n' -n1 key
echo '15x hollow rocks'
read -rsp $'Press any key to continue...\n' -n1 key
echo '15 spartan pushups'
read -rsp $'Press any key to continue...\n' -n1 key
echo '45 biceps curls'
read -rsp $'Press any key to continue...\n' -n1 key
echo 'ROUND IV complete!'
read -rsp $'Press any key to continue...\n' -n1 key
clear
echo 'ROUND V'
echo '15x crab walk'
read -rsp $'Press any key to continue...\n' -n1 key
echo '30x high knees'
read -rsp $'Press any key to continue...\n' -n1 key
echo '20x lunges'
read -rsp $'Press any key to continue...\n' -n1 key
echo '15x leg raises'
read -rsp $'Press any key to continue...\n' -n1 key
echo '30x biceps curls'
read -rsp $'Press any key to continue...\n' -n1 key
clear

#timer
duration=$(( MINUTES - start ))
echo "SUMMARY"
echo "Your workout took $MINUTES minutes"