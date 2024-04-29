#!/bin/env bash

STATE=$(acpi | awk '{print $3}')
while true; do
	NEW_STATE=$(acpi | awk '{print $3}')
	if ! [[ $STATE == $NEW_STATE ]]; then
		# echo "True!"
		# /home/alexa/scripts/pcMode.sh
		if [ $STATE = "Charging"]; then
			/home/alexa/scripts/pcDock.sh docked
		else
			/home/alexa/scripts/pcDock.sh undocked
		fi
	fi
	STATE=$NEW_STATE
	sleep 1
done
