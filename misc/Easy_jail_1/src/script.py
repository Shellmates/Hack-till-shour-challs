#!/usr/bin/env python2.7

import sys

FLAG="FAKE_FLAG"

while True :
    try:
        sys.stdout.write("Input>> ")
        sys.stdout.flush()
        exp=input()
        print exp
    except:
        sys.stdout.write("Error\n");
        sys.stdout.flush()
