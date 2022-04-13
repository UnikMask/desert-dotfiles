#!/usr/bin/env python3

import datetime
import shutil
import theme_utils
from pathlib import Path


# Config times for light theme switch on and off times
switch_off_time = 9
switch_on_time = 17


def getHour():
    return datetime.datetime.now().time().hour


# Paths to light and dark theme
base_path = Path.home().joinpath('dotboy/saves/desert')
light_path = base_path.joinpath('white')
dark_path = base_path.joinpath('black')


def getThemePathFromTime():
    # Select light or dark theme from hour of the day
    if getHour() >= switch_off_time and getHour() < switch_on_time:
        return light_path
    else:
        return dark_path


def __main__():
    theme_path = getThemePathFromTime()
    if theme_path.is_dir():
        # Use wallpaper
        wp_path = theme_path / 'wallpaper.jpg'
        if shutil.which("feh"):
            theme_utils.runsilent(['feh', '--bg-scale', str(wp_path)])

        t_xrdb_path = theme_path / '.Xresources'
        a_xrdb_path = Path.home() / '.Xresources'
        t_kitty_path = theme_path / '.config' / 'kitty' / 'theme.conf'
        a_kitty_path = Path.home() / '.config' / 'kitty' / 'theme.conf'

        # Unlink original kitty path and link new one
        theme_utils.theme_link(t_kitty_path, a_kitty_path)
        print("Kitty linked!")

        # Link and reload Xresources
        theme_utils.theme_link(t_xrdb_path, a_xrdb_path)
        theme_utils.runsilent(["xrdb", str(t_xrdb_path)])
        print("Xresources linked!")

        # Reload polybar if exists
        if theme_utils.has_pid("polybar"):
            theme_utils.runsilent(["pkill", "-SIGKILL", "polybar"])
            theme_utils.run_async(["polybar", "-r", "-q", "unikBar"])
        print("Polybar linked!")

        # Link and reload dunst
        t_dunst_path = theme_path / '.config' / 'dunst' / 'dunstrc'
        a_dunst_path = Path.home() / '.config' / 'dunst' / 'dunstrc'
        theme_utils.theme_link(t_dunst_path, a_dunst_path)
        if theme_utils.has_pid("dunst"):
            theme_utils.runsilent(["pkill", "-SIGKILL", "dunst"])
            theme_utils.run_async(["dunst"])
        print("Dunst linked!")

        # Symlink the vim theme config
        t_vim_path = theme_path / '.config' / 'theme.vim'
        a_vim_path = Path.home() / '.config' / 'nvim' / 'theme.vim'
        theme_utils.theme_link(t_vim_path, a_vim_path)
        print("Vim linked!")

        # Symlink iroh theme config
        t_rofi_path = theme_path / '.config' / 'rofi' / 'iroh.rasi'
        a_rofi_path = Path.home() / '.config' / 'rofi' / 'iroh.rasi'
        theme_utils.theme_link(t_rofi_path, a_rofi_path)
        print("Rofi linked!")

        # Symlink userChrome.css
        t_chromep = theme_path / '.config' / 'userChrome.css'
        a_chromep = Path.home() / '.mozilla' / 'firefox'
        a_chromep = a_chromep.joinpath('ce5vez5l.default-release')
        a_chromep = a_chromep.joinpath('chrome/userChrome.css')
        theme_utils.theme_link(t_chromep, a_chromep)
        print("Firefox linked!")

        # i3 configuration
        t_i3 = theme_path / '.config' / 'i3' / 'config'
        a_i3 = Path.home() / '.config' / 'i3' / 'config'
        theme_utils.theme_link(t_i3, a_i3)
        print("i3 linked!")

    else:
        print("ERROR: Path to given theme doesn't exist!")
        exit(1)


__main__()
