# Janken

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: As you approach an ancient tomb, you're met with a wise guru who guards its entrance. In order to proceed, he challenges you to a game of Janken, a variation of rock paper scissors with a unique twist. But there's a catch: you must win 100 rounds in a row to pass. Fail to do so, and you'll be denied entry.

## NOTES

1. Deploy Docker
   1. > IP: 167.99.86.8 32530
2. Extract files
   1. > unzip janken.zip
      1. FILE(S): glibc, janken, flag.txt
3. Examine files
   1. > file janken
      1. RESPONSE: `janken: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./.glibc/ld-linux-x86-64.so.2, BuildID[sha1]=56b54cdae265aa352fe2ebb016f86af831fd58d3, for GNU/Linux 3.2.0, not stripped`
4. GHIDRA
   1. Import -> Analyze Now
   2. Looking at the game() function and renaming a few variables for slef understadning we can see the gimmick

        ```c
            void game(void)

            {
            int random_integer;
            time_t tVar1;
            ushort **ppuVar2;
            size_t len_of_user_input;
            char *pcVar3;
            long in_FS_OFFSET;
            ulong num_games;
            char *choice [4];
            char *win_condition [4];
            undefined8 our_user_input;
            undefined8 local_30;
            undefined8 local_28;
            undefined8 local_20;
            long local_10;
            
            local_10 = *(long *)(in_FS_OFFSET + 0x28);
            tVar1 = time((time_t *)0x0);
            srand((uint)tVar1);
            random_integer = rand();
            choice[0] = "rock";
            choice[1] = "scissors";
            choice[2] = "paper";
            our_user_input = 0;
            local_30 = 0;
            local_28 = 0;
            local_20 = 0;
            win_condition[0] = "paper";
            win_condition[1] = &DAT_0010252a;
            win_condition[2] = "scissors";
            fwrite(&DAT_00102540,1,0x33,stdout);
            read(0,&our_user_input,0x1f);
            fprintf(stdout,"\n[!] Guru\'s choice: %s%s%s\n[!] Your  choice: %s%s%s",&DAT_00102083,
                    choice[random_integer % 3],&DAT_00102008,&DAT_0010207b,&our_user_input,&DAT_00102008);
            num_games = 0;
            do {
                len_of_user_input = strlen((char *)&our_user_input);
                if (len_of_user_input <= num_games) {
            LAB_001017a2:
                pcVar3 = strstr((char *)&our_user_input,win_condition[random_integer % 3]);
                if (pcVar3 == (char *)0x0) {
                    fprintf(stdout,"%s\n[-] You lost the game..\n\n",&DAT_00102083);
                                /* WARNING: Subroutine does not return */
                    exit(0x16);
                }
                fprintf(stdout,"\n%s[+] You won this round! Congrats!\n%s",&DAT_0010207b,&DAT_00102008);
                if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                                /* WARNING: Subroutine does not return */
                    __stack_chk_fail();
                }
                return;
                }
                ppuVar2 = __ctype_b_loc();
                if (((*ppuVar2)[*(char *)((long)&our_user_input + num_games)] & 0x2000) != 0) {
                *(undefined *)((long)&our_user_input + num_games) = 0;
                goto LAB_001017a2;
                }
                num_games = num_games + 1;
            } while( true );
        ```

   3. In here we see the comparison for **WHO WINS**
      1. `if (pcVar3 == (char *)0x0)`
   4. However, the line before sets the variable pcVar3
      1. `pcVar3 = strstr((char *)&our_user_input,win_condition[random_integer % 3]);`
      2. THis is a substring search
   5. SOOOO the gimmick is, as long as you have all three substrings (ie. rock, paper, and scissors) then it will return false and **YOU WIN**
5. TESTING
   1. Lets run our ./janken game
   2. > select 1 to play
   3. > for our choice input rockpaperscissors
      1. SUCCESS! We win@
   4. Now we need to do this 100 times
   5. Lets write a script
      1. Need to use sockets to connect to htb
      2. Need to read in game menu
      3. Need to send our repsonse 100 times
6. EXPLOIT
   1. > python3 win.py
      1. RESPONSE: `[+] You are worthy! Here is your prize: HTB{r0ck_p4p3R_5tr5tr_l0g1c_buG}`
