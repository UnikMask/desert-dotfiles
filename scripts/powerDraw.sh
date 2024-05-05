#!/bin/sh

for i in /sys/class/power_supply/BAT*; do
    awk "BEGIN { m_wattage = $(( $(cat $i/current_now) * $(cat $i/voltage_now))); printf \"%.1f\", m_wattage / 1000000000000}"; echo " W "
done
