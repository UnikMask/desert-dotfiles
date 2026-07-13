#! /bin/sh

# === === === === === === === === === === ===
# Bitwarden password selector for Rofi (rbw)
# Creator: UnikMask
# Email: <visorunik@gmail.com>
# === === === === === === === === === === ===


rbw unlock

# Compute a vertical offset equal to 10% of the focused output's height,
# so the window sits 10% above screen center (rofi's yoffset is in pixels).
# swaymsg lists each output as an object whose rect.height appears before
# its "focused" flag, so we capture the first height of the focused object.
yoffset=0
if command -v swaymsg >/dev/null 2>&1; then
	h=$(swaymsg -t get_outputs 2>/dev/null | awk '
		/^  \{/ { curh="" }
		curh=="" && /"height": *[0-9]/ {
			h=$0; sub(/.*"height": */,"",h); sub(/[^0-9].*/,"",h); curh=h
		}
		/"focused": *true/ { print curh; exit }
	')
	[ -n "$h" ] && yoffset=$(( -(h / 10) ))
fi

# Rofi command using the iroh-themed bw.rasi
rofi_cmd="rofi -theme bw.rasi -dmenu -i -p 'Password' -yoffset $yoffset"

# Make sure the local Bitwarden database is unlocked before listing.
if ! rbw unlocked >/dev/null 2>&1; then
	# Prompt for the master password through rofi, pipe to rbw unlock.
	master="$(printf '' | $rofi_cmd -password -p 'Unlock Bitwarden')"
	[ -z "$master" ] && exit 1
	printf '%s\n' "$master" | rbw unlock 2>/dev/null
fi

# List all entries and let the user pick one.
entry="$(rbw list | sort | $rofi_cmd)"

# Exit gracefully on cancellation.
[ -z "$entry" ] && exit 0

# Fetch the password and copy it to the Wayland clipboard.
rbw get "$entry" | wl-copy
