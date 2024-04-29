#!/usr/bin/env python3

import os
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
base_path = Path(os.path.dirname(os.path.realpath(__file__)))
light_path = base_path.joinpath('white')
dark_path = base_path.joinpath('black')


def getThemePathFromTime():
    # Select light or dark theme from hour of the day
    return dark_path


def __main__():
    theme_path = getThemePathFromTime()
    if not theme_path.is_dir():
        print("ERROR: Path to given theme doesn't exist!")
        exit(1)

    # Use wallpaper
    wp_path = theme_path / 'wallpaper.jpg'
    theme_cfg = theme_path / 'config'
    base_cfg = base_path / 'config'
    home_cfg = Path.home() / '.config'

    if os.environ["XDG_SESSION_TYPE"] == "wayland" \
            and shutil.which("swaybg"):
        theme_utils.runsilent(["swaybg", str(wp_path)])
    elif os.environ["XDG_SESSION_TYPE"] != "wayland" \
            and shutil.which("feh"):
        theme_utils.runsilent(['feh', '--bg-scale', str(wp_path)])

    # Link environment path
    theme_utils.theme_link(base_cfg / 'environment.d',
                           home_cfg / 'environment.d')
    print('Systemd user environment linked!')

    # Unlink original kitty path and link new one
    theme_utils.theme_link(
        base_cfg / 'kitty', home_cfg / 'kitty')
    theme_utils.theme_link(theme_cfg / 'kitty' / 'theme.conf',
                           home_cfg / 'kitty' / 'theme.conf')
    print("Kitty linked!")

    theme_utils.theme_link(base_path / 'wlinitrc',
                           Path.home() / '.wlinitrc')
    print("Wayland Init RC linked!")

    theme_utils.theme_link(base_cfg / 'zshrc', Path.home() / '.zshrc')
    theme_utils.theme_link(base_cfg / 'oh-my-zsh',
                           Path.home() / '.oh-my-zsh')
    theme_utils.theme_link(base_cfg / 'omz-custom',
                           Path.home() / '.omz-custom')
    print("ZSH / oh-my-zsh linked!")

    # Link and reload Xresources
    theme_utils.theme_link(theme_path / '.Xresources',
                           Path.home() / '.Xresources')
    theme_utils.runsilent(["xrdb", str(Path.home() / '.Xresources')])
    print("Xresources linked!")

    # Reload polybar if exists
    theme_utils.theme_link(base_cfg / 'polybar', home_cfg / 'polybar')
    if theme_utils.has_pid("polybar"):
        theme_utils.runsilent(["pkill", "-SIGKILL", "polybar"])
        theme_utils.run_async(["polybar", "-r", "-q", "unikBar"])
    print("Polybar linked!")

    # Link and reload dunst
    t_dunst_path = theme_cfg / 'dunst'
    a_dunst_path = home_cfg / 'dunst'
    theme_utils.theme_link(t_dunst_path, a_dunst_path)
    if theme_utils.has_pid("dunst"):
        theme_utils.runsilent(["pkill", "-SIGKILL", "dunst"])
        theme_utils.run_async(["dunst"])
    print("Dunst linked!")

    # Symlink iroh theme config
    theme_utils.theme_link(base_cfg / 'rofi', home_cfg / 'rofi')
    theme_utils.theme_link(theme_cfg / 'rofi' / 'iroh.rasi',
                           home_cfg / 'rofi' / 'iroh.rasi')
    print("Rofi linked!")

    # i3 configuration
    theme_utils.theme_link(theme_cfg / 'i3' / 'config',
                           home_cfg / 'i3' / 'config')
    print("i3 linked!")

    # Sway configuration
    theme_utils.theme_link(theme_cfg / 'sway', home_cfg / 'sway')
    print("Sway linked!")
    theme_utils.theme_link(theme_cfg / 'waybar', home_cfg / 'waybar')
    print("Waybar linked!")

    # Zathura config
    theme_utils.theme_link(theme_cfg / 'zathura', home_cfg / 'zathura')
    print("Zathura linked!")

    # GTK Themes config
    theme_utils.theme_link(base_cfg / 'gtk-themes', Path.home() / '.themes')
    print('GTK Theme Linked!')

    # NCMPCPP config
    theme_utils.theme_link(theme_cfg / 'ncmpcpp', Path.home() / '.ncmpcpp')
    print('NCMPCPP linked!')

    # Mopidy config
    theme_utils.theme_link(base_cfg / 'mopidy', home_cfg / 'mopidy')
    print('Mopidy Linked!')

    # Gtk settings
    theme_utils.theme_link(theme_cfg / 'gtk-3.0', home_cfg / 'gtk-3.0')
    print("Gtk settings Linked!")

    # XBindKeysRC config
    theme_utils.theme_link(base_cfg / 'xbindkeysrc',
                           Path.home() / '.xbindkeysrc')
    print("XBindkeysRC linked!")

    # Link Scripts
    theme_utils.theme_link(base_path / 'scripts',
                           Path.home() / 'scripts')
    print('Scripts linked!')


__main__()
