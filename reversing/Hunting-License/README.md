# Hunting-License

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: STOP! Adventurer, have you got an up to date relic hunting license? If you don't, you'll need to take the exam again before you'll be allowed passage into the spacelanes

## NOTES

1. Deploy Docker
   1. > IP: 178.62.9.10:30473
2. Extract files
   1. > unzip rev_hunting_license.zip
      1. FILE(S):license
3. Examine files
   1. > file license
      1. RESPONSE: `license: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=5be88c3ed329c1570ab807b55c1875d429a581a7, for GNU/Linux 3.2.0, not stripped`
   2. > checksec license
      1. Arch:     amd64-64-little
      2. RELRO:    Partial RELRO
      3. Stack:    No canary found
      4. NX:       NX enabled
      5. PIE:      No PIE (0x400000)
   3. > ldd license
      1. linux-vdso.so.1 (0x00007ffc4a972000)
      2. libreadline.so.8 => /lib/x86_64-linux-gnu/libreadline.so.8 (0x00007faad40f0000)
      3. libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007faad3f0f000)
      4. libtinfo.so.6 => /lib/x86_64-linux-gnu/libtinfo.so.6 (0x00007faad3edd000)
      5. /lib64/ld-linux-x86-64.so.2 (0x00007faad416b000)

   4. > strings license
      1. RESPONSE:

        ```text
            So, you want to be a relic hunter?
            First, you're going to need your license, and for that you need to pass the exam.
            It's short, but it's not for the faint of heart. Are you up to the challenge?! (y/n)
            Not many are...
            Well done hunter - consider yourself certified!
            Okay, first, a warmup - what's the first password? This one's not even hidden: 
            PasswordNumeroUno
            Not even close!
            Getting harder - what's the second password? 
            You've got it all backwards...
            Your final test - give me the third, and most protected, password: 
            Failed at the final hurdle!
            ;*3$"
            0wTdr0wss4P
            G{zawR}wUz}r
        ```

   5. Lets open this up with ghidra
4. GHIDRA
   1. > ghidra license
      1. Import -> Analyze Now
   2. MAIN()

        ```c
            undefined8 main(void)

            {
            char cVar1;
            int iVar2;
            
            puts("So, you want to be a relic hunter?");
            puts("First, you\'re going to need your license, and for that you need to pass the exam.");
            puts("It\'s short, but it\'s not for the faint of heart. Are you up to the challenge?! (y/n)");
            iVar2 = getchar();
            cVar1 = (char)iVar2;
            if (((cVar1 != 'y') && (cVar1 != 'Y')) && (cVar1 != '\n')) {
                puts("Not many are...");
                                /* WARNING: Subroutine does not return */
                exit(-1);
            }
            exam();
            puts("Well done hunter - consider yourself certified!");
            return 0;
            }
        ```

      1. In here we see essentially the banner portion that has all the set up (ie. asking if you are ready)
      2. We also see the exam() function that is called lets take a look at it
   3. EXAM()

        ```c
            int iVar1;
            undefined8 local_38;
            undefined8 local_30;
            undefined local_28;
            undefined8 local_1c;
            undefined4 local_14;
            char *local_10;

            local_10 = (char *)readline(
                                        "Okay, first, a warmup - what\'s the first password? This one\'s not ev en hidden: "
                                        );
            iVar1 = strcmp(local_10,"PasswordNumeroUno");
            if (iVar1 != 0) {
            puts("Not even close!");
                            /* WARNING: Subroutine does not return */
            exit(-1);
            }
            free(local_10);
            local_1c = 0;
            local_14 = 0;
            reverse(&local_1c,t,0xb);
            local_10 = (char *)readline("Getting harder - what\'s the second password? ");
            iVar1 = strcmp(local_10,(char *)&local_1c);
            if (iVar1 != 0) {
            puts("You\'ve got it all backwards...");
                            /* WARNING: Subroutine does not return */
            exit(-1);
            }
            free(local_10);
            local_38 = 0;
            local_30 = 0;
            local_28 = 0;
            xor(&local_38,t2,0x11,0x13);
            local_10 = (char *)readline("Your final test - give me the third, and most protected, password: ")
            ;
            iVar1 = strcmp(local_10,(char *)&local_38);
            if (iVar1 != 0) {
            puts("Failed at the final hurdle!");
                            /* WARNING: Subroutine does not return */
            exit(-1);
            }
            free(local_10);
            return;
        ```

        1. In here we see three questions, all asking about passwords
        2. We see the first funtion is a string compare of the **local_10** variable and the string `PasswordNumeroUno`
        3. It looks like the second fucntion looks at the reversed string of the original password
        4. Finally the third function looks like it XOR's the original password with the values
   4. REVERSE()

        ```c
            void reverse(long param_1,long param_2,ulong param_3)

            {
            int local_c;

            for (local_c = 0; (ulong)(long)local_c < param_3; local_c = local_c + 1) {
                *(undefined *)(param_1 + local_c) = *(undefined *)(param_2 + (param_3 - (long)local_c) + -1);
            }
            return;
        ```

      1. In the reverse funtion we see it takes 3 arguments
         1. param1 = string
         2. param2 = t
         3. param3 = iterator value
      2. For loop from 0 to 0xb (11)
      3. local_c is the iterator variable
      4. 

   5. XOR()
5. NC
   1. > nc 178.62.9.10 30473
      1. QUESTION 1 - What is the file format of the executable?
         1. >> ELF 64-Bit
      2. QUESTION 2 - What is the CPU architecture of the executable?
         1. >> x86-64
      3. QUESTION 3 - What library is used to read lines for user answers? (`ldd` may help)
         1. >> libreadline.so.8
      4. QUESTION 4 - What is the address of the `main` function?
         1. >> 0x401172
      5. QUESTION 5 - How many calls to `puts` are there in `main`? (using a decompiler may help)
         1. >> 5
      6. QUESTION 6 - What is the first password?
         1. >> PasswordNumeroUno
      7. QUESTION 7 - What is the reversed form of the second password?
         1. >> 
