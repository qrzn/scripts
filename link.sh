#!/bin/bash
# script to automatically link dotfiles to thy home folder
# deleting existing dotfiles...
echo "deleting existing dotfiles..." 
rm -v $HOME/.bashrc
rm -v $HOME/.dosbox/
rm -v $HOME/.muttrc
rm -v $HOME/.startpage
rm -v $HOME/.vimrc
rm -v $HOME/.zshrc
echo "done, creating links now..."
# creating links
ln -s $HOME/git/.fls/.bashrc $HOME/.bashrc
ln -s $HOME/git/.fls/.dosbox/ $HOME/
ln -s $HOME/git/.fls/.muttrc $HOME/.muttrc
ln -s $HOME/git/.fls/.startpage/ $HOME/
ln -s $HOME/git/.fls/.vimrc $HOME/.vimrc
ln -s $HOME/git/.fls/.zshrc $HOME/.zshrc
echo "done!"

