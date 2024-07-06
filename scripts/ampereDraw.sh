#!/bin/bash

for bat in /sys/class/power_supply/BAT*; do
    awk "BEGIN {printf \"%.1f\", $(( $(cat $bat/current_now))) / 1000 }"; echo " mA "
done
