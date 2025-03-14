#!/usr/bin/env python3
'''Author: Kevin Ho'''
'''Author ID: 100797190'''
'''Date Created: 2025/03/03'''

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])
    
while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')