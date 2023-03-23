# Alien-Saboteaur

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: You finally manage to make it into the main computer of the vessel, it's time to get this over with. You try to shutdown the vessel, however a couple of access codes unknown to you are needed. You try to figure them out, but the computer start speaking some weird language, it seems like gibberish...

## NOTES

1. Extract files
   1. > unzip rev_alien_saboteur.zip
      1. FILE(S): bin, vm
2. Examine Files
   1. > file bin
      1. RSEPONSE: `bin: data`
   2. > file vm
      1. RESPONSE: `vm: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=10fb238b19d3a82b46536b51e47396525086a09c, for GNU/Linux 3.2.0, not stripped`
3. Run the file
   1. First attempt
      1. > ./vm
         1. RESPONSE: `Usage: ./chall file`
         2. This tells me we need to potentially provide it with some form of input
   2. Second attempt
      1. > ./vm bin
         1. RESPONSE: `[Main Vessel Terminal] < Enter keycode <`
4. GHIDRA
   1. Import -> Analyze Now
   2. Main()
      1. Lets examine the code

            ```c
                undefined8 main(int param_1,long param_2)

                {
                FILE *__stream;
                size_t __size;
                void *__ptr;
                undefined8 uVar1;
                
                if (param_1 < 2) {
                    printf("Usage: ./chall file");
                                    /* WARNING: Subroutine does not return */
                    exit(1);
                }
                __stream = fopen(*(char **)(param_2 + 8),"rb");
                fseek(__stream,0,2);
                __size = ftell(__stream);
                rewind(__stream);
                __ptr = malloc(__size);
                fread(__ptr,__size,1,__stream);
                fclose(__stream);
                uVar1 = vm_create(__ptr,__size);
                vm_run(uVar1);
                return 0;
                }
            ```

      2. In the main function we see the break down
         1. If the supplied param is < 2 (meaning 0 or 1) we get an error printing out "Usage ./chall file"
         2. The file then opens up a file (our bin file)
         3. It **seeks** the stream with params (__stream,0,2)
         4. It **rewinds** the stream
         5. freads()
         6. fclose()
         7. vm_run() -> lets go examine this code
   3. vm_run()
      1. Examine the code

            ```c
                void vm_run(long param_1)

                {
                while (*(char *)(param_1 + 4) == '\0') {
                    vm_step(param_1);
                }
                return;
                }
            ```

      2. We see while look where it checks param_1 + 4 = '\0'
         1. If so... then vm_step()
