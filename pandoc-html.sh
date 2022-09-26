#!/bin/bash

#usage - put an filename.md -o filename.html at the end of the command
#
pandoc --standalone --template /home/jan/git/scripts/template.html 
break 
echo '~conversion successful~'
