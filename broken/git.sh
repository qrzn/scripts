#!/bin/bash
# automated github repository update script
# what does it do, though?
# well it checks all your repos for new files, commits & uploads them
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
echo 'all done!'
