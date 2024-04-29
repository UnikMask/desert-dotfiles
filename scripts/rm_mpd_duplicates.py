#!/usr/bin/python

import subprocess

data = dict()
delpos = list()

p = subprocess.Popen(["/usr/bin/mpc", "-f", "%position% %file%", "playlist"],
                     shell=False, stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
for line in p.stdout:
    line = line.decode("utf-8")
    line = line.rstrip('\n')

    position, filename = line.split(" ", 1)
    data.setdefault(filename, []).append(position)

for key in data:
    poslen = len(data[key])
    if poslen <= 1:
        continue
    print("Will delete:", poslen-1, "time(s)", key)
    iterpos = iter(data[key])
    next(iterpos)
    for pos in iterpos:
        delpos.append(pos)
delpos = list(map(int, delpos))
delpos.sort(reverse=True)

for item in delpos:
    p = subprocess.Popen(["/usr/bin/mpc", "del", str(item)],
                         shell=False, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
