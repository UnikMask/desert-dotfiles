#!/usr/bin/env python3

import subprocess
from subprocess import Popen


def runsilent(args):
    subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def run_async(args):
    Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


# Check if a taskname has a PID
def has_pid(taskname):
    try:
        subprocess.check_output(["pidof", taskname])
    except subprocess.CalledProcessError:
        return False
    return True


# Link a theme file to a given path
def theme_link(themed_path, link_path):
    if link_path.is_symlink():
        link_path.unlink()
    if not link_path.is_file():
        link_path.symlink_to(themed_path)
    else:
        print("Error: " + link_path + " is not a symbolic link.")
