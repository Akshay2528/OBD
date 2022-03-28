import sys
import ctypes
import time
from ctypes import *
libc = ctypes.CDLL("/usr/lib/libOBD2.so")
rc = libc.init(0)
print(hex((rc + (1 << 32)) % (1 << 32)))
rc=libc.wifi_init(0)
print(hex((rc + (1 << 32)) % (1 << 32)))					
