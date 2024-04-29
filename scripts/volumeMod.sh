#!/usr/bin/env bash

MSG_ID=734892

INCR=5
VOL_SWITCH=50

# Get max volume and sink device.
MAX_VOLUME=100
DEVICE=$(pactl get-default-sink)

# Calculate volume, and volume increment.
VOLUME=$(pactl get-sink-volume $DEVICE | awk '{print $5}' | sed 's/%//g')
IS_MUTED=$(pactl get-sink-mute $DEVICE | awk '{print $2}')
UNMUTED="false"



if [ $1 = "mute" ] && [ $IS_MUTED = "no" ]; then
	pactl set-sink-mute $DEVICE true
	dunstify -a "changeVolume" -u low -i audio-volume-muted -r "$MSG_ID" "Volume muted"
else
	pactl set-sink-mute $DEVICE false
	if [ $1 = "mute" ]; then 
		dunstify -a "changeVolume" -u low -i audio-volume-muted -r "$MSG_ID" "Volume unmuted"
		UNMUTED="true"
	fi

	if [ $1 = "up" ]; then
		NEW_VOLUME=$(echo "$VOLUME+$INCR" |bc)
		NEW_VOLUME=$(( $NEW_VOLUME < $MAX_VOLUME ? $NEW_VOLUME : $MAX_VOLUME ))
		pactl set-sink-volume $DEVICE $NEW_VOLUME%
	elif [ $1 = "down" ]; then
		NEW_VOLUME=$(echo "$VOLUME-$INCR" |bc)
		NEW_VOLUME=$(( $NEW_VOLUME > 0 ? $NEW_VOLUME : 0 ))
		pactl set-sink-volume $DEVICE $NEW_VOLUME%
	fi

	if [ $NEW_VOLUME -ne $VOLUME ] && [ "$UNMUTED" = "false" ];then

		# Set new volume percentage and volume icon.
		VOLUME_PERCENT=$(echo $(printf %.$2f $(echo "$NEW_VOLUME/$MAX_VOLUME*100" | bc -l)))
		VOL_ICON=$(( $VOLUME_PERCENT <= $VOL_SWITCH ? audio-volume-low : audio-volume-high ))

		# Set messaging
		dunstify -a "changeVolume" -u low -i $VOL_ICON -r $MSG_ID "Volume: $VOLUME_PERCENT%"
	fi
fi


