#!/bin/env sh

MONITORS_ON=$(xrandr | grep " connected " | awk '{print $1}')
MONITORS_OFF=$(xrandr | grep " disconnected " | awk '{print $1}')

j=""
for i in $MONITORS_ON; do
	xrandr --output $i --auto $j
	j="--right-of $i"
done
for i in $MONITORS_OFF; do
	xrandr --output $i --off
done
