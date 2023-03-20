# Pandoras-Box

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: You stumbled upon one of Pandora's mythical boxes. Would you be curious enough to open it and see what's inside, or would you opt to give it to your team for analysis?

## NOTES

1. Deploy Docker
   1. > IP: 104.248.169.117:32339
2. Extract files
   1. > unzip pwn_pandoras_box.zip
      1. FILE(S): pb, glibc
3. Examine the files
   1. > file pb
      1. RESPONSE: `pb: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./glibc/ld-linux-x86-64.so.2, BuildID[sha1]=d0165634ba8886a0cdf61584d8c941d30ff3820e, for GNU/Linux 3.2.0, not stripped`
   2. > pwn checksec pb
      1. Arch:     amd64-64-little
      2. RELRO:    Full RELRO
      3. Stack:    No canary found
      4. NX:       NX enabled
      5. PIE:      No PIE (0x400000)
      6. RUNPATH:  b'./glibc/'
4. Lets run the binary
   1. ./pb
      1. Will you open it or Return it to the Library for analysis? (1. Open, 2. Return)
         1. If we select 1 the program yells and says `WHAT HAVE YOU DONE` then exits
         2. If we select 2 the program asks `Insert location of the library:`
   2. This makes me think we will need to do a buffer overflow
5. GDB
   1. > gdb ./pb
      1. > pattern create -> this will create a cyclical pattern so we can find exactly where the program is sigfaulting at
      2. > r pb -> runs the pb binary
      3. Select option 2
      4. Then once it asks location paste in our pattern
         1. Inside our debugger we see that it is broken at `gaaaaaaa` so lets look at where in our pattern this lands so we can see the offset
            1. > pattern offset $rsp (stack pointer)
               1. RESPONSE: `Found at offset 56 (little-endian search)`
               2. So we know our offset is 56, but since we are 64BIT we need to take into account the canonical so isntead of adding 8 "B"'s after we want to add just 6
         2. We also see that when we break the RIP (return instruction pointer) is still inside the box() function
            1. `$rip   : 0x000000004013a5  →  <box+227> ret`
      5. Send `AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBB`
      6. > r pb
         1. option 2
         2. location `AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBB`
         3. 
