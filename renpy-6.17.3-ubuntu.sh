#!/bin/sh
VERSION="6.17.3"
RENPY="renpy-"$VERSION"-sdk"
BASEDIR=`pwd`
GAME_NAME="esofteacher"

# Tests if wxpython exists before attempting to install.
if ! dpkg -s python-wxgtk2.8 > /dev/null; then
    sudo apt-get install python-wxgtk2.8
fi

# Tests if python-tk exists before attempting to install.
if ! dpkg -s python-tk > /dev/null; then
    sudo apt-get install python-tk
fi

# Tests if renpy exists before attempting to download and extract.
if [ ! -d ../$RENPY ]
then
    wget -c http://www.renpy.org/dl/$VERSION/$RENPY.tar.bz2
    tar -C .. -jxvf $RENPY.tar.bz2
fi

# Changing to $RENPY directory
cd ../$RENPY

# Remove and Create a symlink to the GAME
ln -sf $BASEDIR/$GAME_NAME .

# Run renpy!
./renpy.sh
