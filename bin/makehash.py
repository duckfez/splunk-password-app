#!/usr/bin/env python

import sys
import os.path

#sys.path.append

x=os.path.sep.join([os.path.dirname(sys.argv[0]),'..','etc','passwd'])
print os.path.normpath(x)
