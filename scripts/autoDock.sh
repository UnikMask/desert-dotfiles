#!/bin/env bash

STATE="undocked"
while true; do
    DOCKED=$(lsusb | grep "(RTS5411)|(Genesys)")
	if ! [[ $DOCKED = "" ]] && [[ $STATE == "undocked" ]]; then
		/home/alexa/scripts/pcDock.sh docked
		STATE="docked"
	elif [[ $DOCKED = "" ]] && [[ $STATE = "docked" ]]; then
		/home/alexa/scripts/pcDock.sh undocked
		STATE="undocked"
	fi
done

