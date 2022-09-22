#!/bin/bash
# backup tool for dotfiles
# ATTENTION if the files don't exist in your home directory they'll get deleted in the repository
clear
echo "running backup script...yay"
cd ~/git/.fls
rm -rv ~/git/.fls/.dosbox && cp -rv ~/.dosbox ~/git/.fls/
rm -v ~/git/.fls/.vimrc && cp -rv ~/.vimrc ~/git/.fls/
rm -v ~/git/.fls/.zshrc && cp -rv ~/.zshrc ~/git/.fls/
rm -v ~/git/.fls/.muttrc && cp -rv ~/.muttrc ~/git/.fls/
rm -v ~/git/.fls/.bashrc && cp -rv ~/.bashrc ~/git/.fls/
rm -rv ~/git/.fls/.startpage && cp -rv ~/.startpage ~/git/.fls/

cd ~/git/.fls
git add . 
git commit -m 'automated backup script message'
git push
echo 'backup complete!'
