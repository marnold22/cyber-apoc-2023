# She-Shells-C-Shells

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: You've arrived in the Galactic Archive, sure that a critical clue is hidden here. You wait anxiously for a terminal to boot up, hiding in the shadows from the guards hunting for you. Unfortunately, it looks like you'll need a password to get what you need without setting off the alarms...

## NOTES

1. Extract fies
   1. > unzip rev_cshells.zip
      1. FILE(S): shell
2. Examine file
   1. > file shell
      1. REPONSE: `shell: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=c8ab24eb713f3b6c9036da743112176b91e58f1b, for GNU/Linux 3.2.0, not stripped`
      2. So we know this is a binary
   2. > strings shell
      1. RESPOSNE: `whoami, cat, getflag`
      2. So these all hint at there being some instructions we need to go through
      3. Lets open this up in ghidra
3. GHIDRA
   1. > ghidra shell
      1. Import -> shell
      2. Analyze Now
   2. Go to FUNCTIONS -> MAIN
      1. We see that there is aactually a getflag function
      2. getflag()
         1. c code

```c
    undefined8 func_flag(void)
    {
    undefined8 uVar1;
    undefined8 local_118;
    undefined8 local_110;
    undefined8 local_108;
    undefined8 local_100;
    undefined8 local_f8;
    undefined8 local_f0;
    undefined8 local_e8;
    undefined8 local_e0;
    undefined8 local_d8;
    undefined8 local_d0;
    undefined8 local_c8;
    undefined8 local_c0;
    undefined8 local_b8;
    undefined8 local_b0;
    undefined8 local_a8;
    undefined8 local_a0;
    undefined8 local_98;
    undefined8 local_90;
    undefined8 local_88;
    undefined8 local_80;
    undefined8 local_78;
    undefined8 local_70;
    undefined8 local_68;
    undefined8 local_60;
    undefined8 local_58;
    undefined8 local_50;
    undefined8 local_48;
    undefined8 local_40;
    undefined8 local_38;
    undefined8 local_30;
    undefined8 local_28;
    undefined8 local_20;
    int local_14;
    uint local_10;
    uint local_c;

    printf("Password: ");
    local_118 = 0;
    local_110 = 0;
    local_108 = 0;
    local_100 = 0;
    local_f8 = 0;
    local_f0 = 0;
    local_e8 = 0;
    local_e0 = 0;
    local_d8 = 0;
    local_d0 = 0;
    local_c8 = 0;
    local_c0 = 0;
    local_b8 = 0;
    local_b0 = 0;
    local_a8 = 0;
    local_a0 = 0;
    local_98 = 0;
    local_90 = 0;
    local_88 = 0;
    local_80 = 0;
    local_78 = 0;
    local_70 = 0;
    local_68 = 0;
    local_60 = 0;
    local_58 = 0;
    local_50 = 0;
    local_48 = 0;
    local_40 = 0;
    local_38 = 0;
    local_30 = 0;
    local_28 = 0;
    local_20 = 0;
    fgets((char *)&local_118,0x100,stdin);
    for (local_c = 0; local_c < 0x4d; local_c = local_c + 1) {
    *(byte *)((long)&local_118 + (long)(int)local_c) =
            *(byte *)((long)&local_118 + (long)(int)local_c) ^ m1[(int)local_c];
    }
    local_14 = memcmp(&local_118,t,0x4d);
    if (local_14 == 0) {
    for (local_10 = 0; local_10 < 0x4d; local_10 = local_10 + 1) {
        *(byte *)((long)&local_118 + (long)(int)local_10) =
            *(byte *)((long)&local_118 + (long)(int)local_10) ^ m2[(int)local_10];
    }
    printf("Flag: %s\n",&local_118);
    uVar1 = 0;
    }
    else {
    uVar1 = 0xffffffff;
    }
    return uVar1;
```
