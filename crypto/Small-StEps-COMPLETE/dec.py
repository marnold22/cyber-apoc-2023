#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes
message = 412926389432612660984016953290834154417829082237
dec = long_to_bytes(message)
print(dec)