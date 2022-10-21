#!/bin/bash
# backup tool for dotfiles
# ATTENTION if the files don't exist in your home directory they'll get deleted in the repository
clear
echo "running backup script...yay"
cd ~/git/.fls
cp -rv ~/.dosbox ~/git/.fls/
cp -rv ~/.vimrc ~/git/.fls/
cp -rv ~/.zshrc ~/git/.fls/
cp -rv ~/.muttrc ~/git/.fls/
cp -rv ~/.bashrc ~/git/.fls/
cp -rv ~/.startpage ~/git/.fls/

git add -all 
git commit -m 'automated backup script message'
git push -u 
echo 'backup complete!'
