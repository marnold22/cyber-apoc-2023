# Questionnaire

## FLAG: HTB{th30ry_bef0r3_4cti0n}

## Status: Complete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: It's time to learn some things about binaries and basic c. Connect to a remote server and answer some questions to get the flag.

## NOTES

1. Deploy Machine
   1. > IP: 104.248.169.175:30311
2. Extract zip files
   1. > unzip pwn_questionnaire.zip
      1. FILE(S): test, test.c
   2. Examine test file
      1. > file test
         1. RESPONSE: `test: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=5a83587fbda6ad7b1aeee2d59f027a882bf2a429, for GNU/Linux 3.2.0, not stripped`
      2. > checksec test
         1. Arch:     amd64-64-little
         2. RELRO:    Partial RELRO
         3. Stack:    No canary found
         4. NX:       NX enabled
         5. PIE:      No PIE (0x400000)
3. Examine C code
   1. test.c

        ```c
            #include <stdio.h>
            #include <stdlib.h>

            /*
            This is not the challenge, just a template to answer the questions.
            To get the flag, answer the questions. 
            There is no bug in the questionnaire.
            */

            void gg(){
                system("cat flag.txt");
            }

            void vuln(){
                char buffer[0x20] = {0};
                fprintf(stdout, "\nEnter payload here: ");
                fgets(buffer, 0x100, stdin);
            }

            void main(){
                vuln();
            }
        ```

   2. In here we see that ther is a vulnerable function fgets()
   3. And there is also a buffer of 0x20-bytes that is filled with 0's
4. Examine test binary
   1. > GDB test
      1. Get the address of gg()
         1. > p gg
            1. RESPONSE: `$1 = {<text variable, no debug info>} 0x401176 <gg>`
5. NC
   1. > nc 104.248.169.175 30311
      1. QUESTION 1 - Is this a '32-bit' or '64-bit' ELF? (e.g. 1337-bit)
         1. >> 64-bit
      2. QUESTION 2 - What's the linking of the binary? (e.g. static, dynamic)
         1. >> dynamic
      3. QUESTION 3 - Is the binary 'stripped' or 'not stripped'?
         1. >> not stripped
      4. QUESTION 4 - Which protections are enabled (Canary, NX, PIE, Fortify)?
         1. >> NX
      5. QUESTION 5 - What is the name of the custom function that gets called inside `main()`? (e.g. vulnerable_function())
         1. >> vuln()
      6. QUESTION 6 - What is the size of the 'buffer' (in hex or decimal)?
         1. >> 0x20
      7. QUESTION 7 - Which custom function is never called? (e.g. vuln())
         1. >> gg()
      8. QUSETION 8 - What is the name of the standard function that could trigger a Buffer Overflow? (e.g. fprintf())
         1. >> fgets()
      9. QUESTION 9 - Insert 30, then 39, then 40 'A's in the program and see the output. After how many bytes a Segmentation Fault occurs (in hex or decimal)?
         1. >> 40
      10. What is the address of 'gg()' in hex? (e.g. 0x401337)
          1. >> 0x401176
      11. Great job! It's high time you solved your first challenge! Here is the flag!
          1. >> HTB{th30ry_bef0r3_4cti0n}
