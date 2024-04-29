#!/usr/bin/env bash

if [ $1 = "docked" ]; then
	xrandr --output DP1 --mode 1920x1080
	xrandr --output DP2-2-1 --mode 1920x1080 --primary --left-of DP1
	xrandr --output eDP1 --off
    touch $DOCKED_FILE
elif [ $1 = "undocked" ]; then
 	xrandr --output eDP1 --mode 1920x1080
 	xrandr --output DP1 --off
	xrandr --output DP2-2-1 --off
    rm $DOCKED_FILE
fi
