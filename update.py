#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

PACKAGE_NAME = "grappelli_extras"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, PACKAGE_NAME)

TO = os.path.join(PROJECT_DIR, PACKAGE_NAME)
FROM = os.path.join(PROJECT_DIR, 'testapp', PACKAGE_NAME)
RM = "rm -rf %s" % TO
CP = "cp -r %s %s" % (FROM, PROJECT_DIR)


VERSION_FILE = os.path.join(FROM, '__init__.py')

version_text = open(VERSION_FILE, "rt").read()

print(version_text)
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, version_text, re.M)
x, y, z = 0, 0, 0
x = int(mo.group(1).split(".")[2])
y = int(mo.group(1).split(".")[1])
z = int(mo.group(1).split(".")[0])
print (x,y,z)
if x < 9:
    x += 1
elif x == 9 and y < 9:
    x = 0
    y += 1
elif x == 9 and y == 9:
    x = 0
    y = 0
    z += 1
else:
    print ("Formato de version anterior invalido por favor use __version__ = 'x.y.z'")

NEW_VERSION = "__version__ = '%s.%s.%s'" % (z, y , x)
open(VERSION_FILE, "w").write(NEW_VERSION)

import os
os.system(RM)
os.system(CP)
print (NEW_VERSION)