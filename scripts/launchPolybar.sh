#!/bin/env bash

if [ $(ps -C polybar -o 'pid=' | xargs)="" ]; then
    polybar -rq unikBar > /tmp/polybar.log 2> /tmp/polybar.log & disown
fi
