#!/bin/sh
VERSION="6.17.3"
RENPY="renpy-"$VERSION"-sdk"
BASEDIR=`pwd`
GAME_NAME="esofteacher"

PACKAGE_LIST="libstdc++6:i386 libgcc1:i386 zlib1g:i386 libncurses5:i386 libsdl1.2debian:i386 python-wxgtk2.8 python-tk"

for pak in $PACKAGE_LIST ; do
  if ! dpkg -s $pak > /dev/null; then
      sudo apt-get install $pak
  fi  
done

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
