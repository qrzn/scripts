#!/bin/bash
# backup tool for dotfiles
clear
echo "running backup script...yay"
cd ~/git/.fls
rm -rfv ~/git/.fls/.dosbox && cp -rv ~/.dosbox ~/git/.fls/
rm -rfv ~/git/.fls/.vimrc && cp -rv ~/.vimrc ~/git/.fls/
rm -rfv ~/git/.fls/.muttrc && cp -rv ~/.muttrc ~/git/.fls/
rm -rfv ~/git/.fls/.bashrc && cp -rv ~/.bashrc ~/git/.fls/
rm -rfv ~/git/.fls/.startpage && cp -rv ~/.startpage ~/git/.fls

cd ~/git/.fls
git add . 
git commit -m 'automated backup script message'
git push
echo 'backup complete!'
