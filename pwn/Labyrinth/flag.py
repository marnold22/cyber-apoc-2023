#!/usr/bin/env python3
from pwn import *
import pprint

elf = ELF("/home/marnold/CTF/cyber-apoc-2023/pwn/Labyrinth/challenge/labyrinth")
pprint.pprint(elf.symbols)