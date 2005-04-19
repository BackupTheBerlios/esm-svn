#! /usr/bin/python

import sys
import sha

password = sys.argv[1]
pw = sha.new(password).hexdigest()

if len(sys.argv) == 2:
    print pw
if len(sys.argv) == 3:
    f = open(sys.argv[2],"w")
    f.write(pw)
    f.close()