#!/bin/bash
# automated github repository update script
# what does it do, though?
# well it checks all your repos for new files, commits & uploads them
echo '##############################'
echo '# gitinator v0.1 by qrzn     #'
echo '##############################'
read -p 'u wanna proceed?' yn
if [ $yn == 'y' ];
then
# dotfiles
cd ~/git/.fls
git add .
git commit -m 'automated commit message (git.sh)'
git push

# scripts
cd ~/git/scripts
git add .
git commit -m 'automated commit message (git.sh)'
git push

# poetry
cd ~/git/ptry
git add .
git commit -m 'automated commit message (git.sh)'
git push

else
read 'okay, bye'
fi