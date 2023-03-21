# Labyrinth

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: You find yourself trapped in a mysterious labyrinth, with only one chance to escape. Choose the correct door wisely, for the wrong choice could have deadly consequences.

## NOTES

1. Deploy Docker
   1. > IP: 165.232.108.36:31534
2. Extract files
   1. > unzip pwn_labyrinth.zip
      1. FILE(S): labyrinth, glibc, flag.txt
3. Examine files
   1. > file labyrinth
      1. RESPONSE: `labyrinth: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./glibc/ld-linux-x86-64.so.2, BuildID[sha1]=86c87230616a87809e53b766b99987df9bf89ad8, for GNU/Linux 3.2.0, not stripped`
   2. > pwn checksec labyrinth
      1. Arch:     amd64-64-little
      2. RELRO:    Full RELRO
      3. Stack:    No canary found
      4. NX:       NX enabled
      5. PIE:      No PIE (0x400000)
      6. RUNPATH:  b'./glibc/'
   3. > strings labyrinth
      1. One line in particular stood out
         1. Congratulations on escaping! Here is a sacred spell to help you continue your journey: %s ./flag.txt
      2. So we must have to guess the correct door or doors
4. GHIDRA
   1. Import -> Analyze Now
   2. Inspecting main()
      1. We see that we must guess the correct door
         1. In here it does a string_compare against the value `69` so we know it is door 69
   3. We also see a function escape_plan()
      1. In here we see the same string we saw earlier about congrats on escaping
      2. So we some how need to invoke the escape_plan() function
5. READELF
   1. Lets check for symbols and the memory addresses of functions
   2. > readelf -s labyrinth
      1. We see our escape_plan() at `49: 0000000000401255   208 FUNC    GLOBAL DEFAULT   13 escape_plan`
      2. So do we need to redirect to \x55\x12\x40
6. GDB
   1. Lets try some buffer overflow to see if we can redirect to $rip to the escape_plan()
   2. Flooding with our cyclic pattern we then can check the $rsp
      1. > pattern search $rsp -> `Found at offset 56 (little-endian search) likely`
