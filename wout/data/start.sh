#!/bin/bash

# start.sh, first try in listing workouts, no timer so far, so it's repetition based or you need to use an external clock to measure the time, it will be included in the final version hower.

data="/home/jan/git/scripts/wout/data/workout1"
wout="/home/jan/git/scripts/wout/"
# THIS is the block for ROUND ONE
# ROUND ONE
start=$MINUTES
PS3="choose your day or view progress"
select opt in progress day1 day2 day3 day4 day5 day6 day7 day8 day9 day10 day11 day12 day13 day14 day15 day16 day17 day18 day19 day20 day21 close; do

case $opt in

	progress)
		clear
		cat $data/progress.txt
		;;
	day1)
		clear
		sh $data/day1.sh
		;; 
	day2)
		sh $data/day2.sh
		;; 
	day3)
		sh $data/day3.sh
		;; 
	day4)
		sh $data/day4.sh
		;; 
	day5)
		sh $data/day5.sh
		;; 
	day6)
		sh $data/day6.sh
		;; 
	day7)
		sh $data/day7.sh
		;; 
	day8)
		sh $data/day8.sh
		;; 
	day9)
		sh $data/day9.sh
		;; 
	day10)
		sh $data/day10.sh
		;; 
	day11)
		sh $data/day11.sh
		;; 
	day12)
		sh $data/day12.sh
		;; 
	day13)
		sh $data/day13.sh
		;; 
	day14)
		sh $data/day14.sh
		;; 
	day15)
		sh $data/day15.sh
		;; 
	day16)
		sh $data/day16.sh
		;; 
	day17)
		sh $data/day17.sh
		;; 
	day18)
		sh $data/day18.sh
		;; 
	day19)
		sh $data/day19.sh
		;; 
	day20)
		sh $data/day20.sh
		;; 
	day21)
		sh $data/day21.sh
		;; 
esac
done

# CONCLUSION
clear
cat $data/conclusion.txt
duration=$(( MINUTES - start ))
echo 'Congratulations, youre done for today!'
echo "the workout took you $duration minutes"
