import subprocess
from subprocess import Popen


def runsilent(args):
    subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def run_async(args):
    Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def is_on(taskname):
    try:
        subprocess.check_output(["pidof", taskname])
    except subprocess.CalledProcessError:
        return False
    return True
