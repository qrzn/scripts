#!/bin/bash

# ddj - a random daodejing chapter explorer
files='*.txt'
clear
echo 'Wise Words from the DaoDeJing:'

cat < find ./data/*.txt | shuf -n 10

read -p 'press ENTER  to continue: ' 
