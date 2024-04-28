#! /bin/sh

# === === === === === === === ===
# Creator: UnikMask
# Email: <visorunik@gmail.com>
# === === === === === === === ===

# Command for rofi
rofi_cmd="rofi -theme powermenu.rasi"

# Options
shutdown="⏻"
reboot=""
lock="󰌾"
suspendtram=""
suspendtdisk="󰋊"
logoutuser="󰗽"

# Values given to rofi
options="$shutdown\n$reboot\n$lock\n$suspendtram\n$suspendtdisk\n$logoutuser"

fcmd="$(echo -e $options | $rofi_cmd -dmenu -selected-row 1)"

if [[ $XDG_SESSION_TYPE == "wayland" ]]; then
    case $fcmd in
        $shutdown) 
            poweroff -i;;
        $reboot) 
            reboot -i;;
        $lock) 
            swaylock;;
        $suspendtram) 
            systemctl suspend ;;
        $suspendtdisk)
            systemctl hibernate ;;
        $logoutuser) 
            swaymsg exit;;
    esac
else
    case $fcmd in
        $shutdown) 
            poweroff -i;;
        $reboot) 
            reboot -i;;
        $lock) 
            slock;;
        $suspendtram) 
            systemctl suspend ;;
        $suspendtdisk)
            systemctl hibernate ;;
        $logoutuser) 
            i3-msg exit;;
    esac
fi

