#!/bin/sh
BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
GAME_NAME=game_test

# Tests if wxpython exists before attempting to install.
if ! dpkg -s python-wxgtk2.8 > /dev/null; then
    sudo apt-get install python-wxgtk2.8
fi

cd

wget -c http://www.renpy.org/dl/6.17.3/renpy-6.17.3-sdk.tar.bz2
tar -jxvf renpy-6.17.3-sdk.tar.bz2

cd renpy-6.17.3-sdk/
rm -f $GAME_NAME
ln -s $BASEDIR/$GAME_NAME .
./renpy.sh
