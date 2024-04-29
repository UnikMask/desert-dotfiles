#!/bin/env sh

DISCORD_ADDS="--enable-features=UseOzonePlatform --ozone-platform=wayland --enable-accelerated-mjpeg-decode --enable-accelerated-video --ignore-gpu-blacklist --enable-native-gpu-memory- buffers --enable-gpu-rasterization --enable-gpu --enable-features=WebRTCPipeWireCapturer"
if [[ $XDG_SESSION_TYPE == "wayland" ]]; then
    discord $DISCORD_ADDS
else
    discord
fi
