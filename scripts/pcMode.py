#!/usr/bin/env python3

# Set computer mode to whether it is in portable mode or desktop mode.

import scripts_utils

portable_cmds = ["xrandr --output DP1 --off"]
desktop_cmds = ["xrandr --output DP1 --auto --right-of eDP1"]


