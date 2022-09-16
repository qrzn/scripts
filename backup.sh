#!/bin/bash
clear
echo "running backup script...yay"
cp -rv ~/.dosbox ~/git/.fls/
cp -rv ~/.vimrc ~/git/.fls/
cp -rv ~/.muttrc ~/git/.fls/
cp -rv ~/.bashrc ~/git/.fls/
read -p 'do you want to upload the files to git? (y/n)' yn
if [ $yn == 'y' ];
then
cd ~/git/.fls;
git add . 
git commit -m 'changed stuff';
git push;
echo 'backup complete!';
elif [ $yn == 'n' ];
then 
  echo 'okay, no commit to git, see ya! :)'
fi
