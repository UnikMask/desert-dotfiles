#!/bin/sh

if [[ $XDG_SESSION_TYPE == "wayland" ]]; then
    export MOZ_ENABLE_WAYLAND="1"
    export TERM="kitty"
    export QT_QPA_PLATFORM=wayland
fi

