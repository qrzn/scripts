#!/bin/bash

# start.sh, first try in listing workouts, no timer so far, so it's repetition based or you need to use an external clock to measure the time, it will be included in the final version hower.


# THIS is the block for ROUND ONE
# ROUND ONE
clear
cat 'data/round1.txt'
read -p 'Enter 1 to continue, 2 to abort: ' pick
if [ $pick == '1' ];
then cat 'data/round2.txt' 
elif [ $pick == '2' ];
then sh './wout.sh' 
else
read -p 'wrong input, one more try (1-2):' pick
fi

# this is a block for round 2-semifinal round, just copy it until round 5
# ROUND TWO
clear
cat 'data/round2.txt'
read -p 'Enter 1 to continue, 2 to abort: ' pick
if [ $pick == '1' ];
then cat 'data/round3.txt' 
elif [ $pick == '2' ];
then sh './wout.sh' 
else
read -p 'wrong input, one more try (1-2):' pick
fi

# this is a block for a round, just copy it until round 5
# ROUND THREE
clear
cat 'data/round3.txt'
read -p 'Enter 1 to continue, 2 to abort: ' pick
if [ $pick == '1' ];
then cat 'data/round3.txt' 
elif [ $pick == '2' ];
then sh './wout.sh' 
else
read -p 'wrong input, one more try (1-2):' pick
fi

# this is a block for a round, just copy it until round 5
# ROUND FOUR
clear
cat 'data/round4.txt'
read -p 'Enter 1 to continue, 2 to abort: ' pick
if [ $pick == '1' ];
then cat 'data/round5.txt' 
elif [ $pick == '2' ];
then sh './wout.sh' 
else
read -p 'wrong input, one more try (1-2):' pick
fi

# this is a block for a round, just copy it until round 5
# ROUND FIVE
clear
cat 'data/round5.txt'
read -p 'Enter 1 to continue, 2 to abort: ' pick
if [ $pick == '1' ];
then cat 'data/conclusion.txt' 
elif [ $pick == '2' ];
then echo 'aborting, you lazy son of a bitch...' && sh './wout.sh' 
else
read -p 'wrong input, one more try (1-2):' pick
fi

# CONCLUSION
clear
cat 'data/conclusion.txt'
read -p 'Enter 1 for main menu, 2 back to DOS :D ' pick
if [ $pick == '1' ];
then sh './wout.sh' 
elif [ $pick == '2' ];
then exit
else
sh './wout.sh'
fi

# FAILED EXPERIMENTS
# this is a block for a round, just copy it until round 5
# ROUND FIVE - LAST ROUND
#read -p 'CONGRATULATIONS! You have finished the workout, press 1 to go to the main menu or 2 to exit: ' pick
#if [ $pick == '1' ];
#then sh './wout.sh' 
#elif [ $pick == '2' ];
#then exit 
#else
#read -p 'wrong input, one more try (1-2):' pick
#fi
