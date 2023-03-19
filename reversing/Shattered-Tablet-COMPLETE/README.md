# Shattered-Tablet

## FLAG: HTB{br0k3n_4p4rt,n3ver_t0_b3_r3p41r3d}

## Status: Complete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: Deep in an ancient tomb, you've discovered a stone tablet with secret information on the locations of other relics. However, while dodging a poison dart, it slipped from your hands and shattered into hundreds of pieces. Can you reassemble it and read the clues?

## NOTES

1. Extract file
   1. > unzip rev_shattered_tablet.zip
      1. FILE: tablet
2. Analyze file
   1. > file tablet
      1. RESPOSNE: `tablet: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=efa8165e123acf37caf4e4b73aba0b826efae1f1, for GNU/Linux 3.2.0, not stripped`
   2. > strings tablet
      1. RSEPOSNE: `Hmmmm... I think the tablet says:` so we see potential, lets run this
3. Run file
   1. > ./tablet
      1. Hmmmm... I think the tablet says: [USER_INPUT]
      2. This tells me that there is a specific string that the tablet is looking for
         1. Lets open this in GHIDRA
4. Ghidra
   1. ghidra -> import -> tablet
   2. Analyze Now -> yes
   3. Lets go to functions -> main()
      1. In here we see

            ```c
                local_48 = 0;
                local_40 = 0;
                local_38 = 0;
                local_30 = 0;
                local_28 = 0;
                local_20 = 0;
                local_18 = 0;
                local_10 = 0;
                printf("Hmmmm... I think the tablet says: ");
                fgets((char *)&local_48,0x40,stdin);
                if (((((((((local_30._7_1_ == 'p') && (local_48._1_1_ == 'T')) && (local_48._7_1_ == 'k')) &&
                        ((local_28._4_1_ == 'd' && (local_40._3_1_ == '4')))) &&
                        ((local_38._4_1_ == 'e' && ((local_40._2_1_ == '_' && ((char)local_48 == 'H')))))) &&
                    (local_28._2_1_ == 'r')) &&
                    ((((local_28._3_1_ == '3' && (local_30._1_1_ == '_')) && (local_48._2_1_ == 'B')) &&
                    (((local_30._5_1_ == 'r' && (local_48._3_1_ == '{')) &&
                        ((local_30._2_1_ == 'b' && ((local_48._5_1_ == 'r' && (local_40._5_1_ == '4')))))))))) &&
                    (((local_30._6_1_ == '3' &&
                    (((local_38._3_1_ == 'v' && (local_40._4_1_ == 'p')) && (local_28._1_1_ == '1')))) &&
                    (((local_30._3_1_ == '3' && (local_38._1_1_ == 'n')) &&
                    (((local_48._4_1_ == 'b' && (((char)local_28 == '4' && (local_40._1_1_ == 'n')))) &&
                        ((char)local_38 == ',')))))))) &&
                    ((((((((char)local_40 == '3' && (local_48._6_1_ == '0')) && (local_38._7_1_ == 't')) &&
                        ((local_40._7_1_ == 't' && ((char)local_30 == '0')))) &&
                    ((local_40._6_1_ == 'r' && ((local_28._5_1_ == '}' && (local_38._5_1_ == 'r')))))) &&
                    (local_38._6_1_ == '_')) && ((local_38._2_1_ == '3' && (local_30._4_1_ == '_')))))) {
                puts("Yes! That\'s right!");
                }
                else {
                puts("No... not that");
                }
                return 0;
            ```

      2. So we can see a large IF() statemetnt that checks for very specific string
      3. Breaking this apart we see it checks for the letters `pTkd4e_Hr3_Br{br43vp13nb4n,30tt0r}r_3_` however this is the incorrect order.
      4. So lets assume each local value represents an array of characters (ie. word) and the ._X_X_ is the order/position in the array
         1. local_48 = HTB{br0k
         2. local_40 = 3n_4p4rt
         3. local_38 = ,n3ver_t
         4. local_30 = 0_b3_r3p
         5. local_28 = 41r3d}
      5. Putting them all together we get
         1. FLAG: `HTB{br0k3n_4p4rt,n3ver_t0_b3_r3p41r3d}`
