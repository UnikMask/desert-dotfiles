# !/bin/env bash

PIC_PATH="$HOME/Pictures/screens/"
SUFFIX=`date +"+%Y-%m-%d-%H-%M"`
IMAGE="$PIC_PATH-$SUFFIX.png"

touch $IMAGE
scrot $IMAGE
