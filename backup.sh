#!/bin/bash
# backup tool for dotfiles
clear
echo "running backup script...yay"
cp -rv ~/.dosbox ~/git/.fls/
cp -rv ~/.vimrc ~/git/.fls/
cp -rv ~/.muttrc ~/git/.fls/
cp -rv ~/.bashrc ~/git/.fls/
cd ~/git/.fls;
git add . 
git commit -m 'changed stuff';
git push;
echo 'backup complete!';
