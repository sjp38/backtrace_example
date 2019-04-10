#!/usr/bin/env python

import os
import sys
import subprocess

for line in sys.stdin:
    spltd = line.split()
    addr = spltd[-1][1:-1]
    print spltd[0]
    cmd = "addr2line -e program %s" % addr
    subprocess.call(cmd, shell=True, executable="/bin/bash")
