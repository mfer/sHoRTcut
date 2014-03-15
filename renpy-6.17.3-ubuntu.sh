#!/bin/sh
VERSION="6.17.3"
RENPY="renpy-"$VERSION"-sdk"
BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
GAME_NAME="game_test"

# Tests if wxpython exists before attempting to install.
if ! dpkg -s python-wxgtk2.8 > /dev/null; then
    sudo apt-get install python-wxgtk2.8
fi
# Tests if python-tk exists before attempting to install.
if ! dpkg -s python-tk > /dev/null; then
    sudo apt-get install python-tk
fi
# Changing to $HOME directory
cd
# Tests if renpy exists before attempting to download and extract.
if [ ! -d $HOME/$RENPY ]
then
    wget -c http://www.renpy.org/dl/$VERSION/$RENPY.tar.bz2
    tar -jxvf $RENPY.tar.bz2
fi
# Changing to $RENPY directory
cd $RENPY
# Remove and Create a symlink to the GAME
rm -f $GAME_NAME
ln -s $BASEDIR/$GAME_NAME .
# Run renpy!
./renpy.sh
