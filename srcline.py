#!/usr/bin/env python

import os
import sys
import subprocess

for line in sys.stdin:
    spltd = line.split()
    addr = spltd[-1][1:-1]
    cmd = "addr2line -e program %s" % addr
    srcline = subprocess.check_output(cmd, shell=True, executable="/bin/bash")
    print spltd[0], srcline.strip()
