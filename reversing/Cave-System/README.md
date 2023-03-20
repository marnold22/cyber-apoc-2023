# Cave-System

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: Deep inside a cave system, 500 feet below the surface, you find yourself stranded with supplies running low. Ahead of you sprawls a network of tunnels, branching off and looping back on themselves. You don't have time to explore them all - you'll need to program your cave-crawling robot to find the way out...

## NOTES

1. Extract files
   1. > unzip_rev_cavessystem.zip
      1. FILE(S): cave
2. Examine file
   1. > file cave
   2. > strings cave
3. GHIDRA
   1. Opening up in ghidra we can look at the main function

```c

/* WARNING: Could not reconcile some variable overlaps */

undefined8 main(void)

{
  int iVar1;
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
  undefined8 local_18;
  undefined8 local_10;
  
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
  local_18 = 0;
  local_10 = 0;
  printf("What route will you take out of the cave? ");
  fgets((char *)&local_88,0x80,stdin);
  iVar1 = memcmp(&local_88,&DAT_00102033,4);
  if (((((((iVar1 == 0) && ((byte)(local_78._5_1_ * (char)local_58) == '\x14')) &&
         ((byte)((byte)local_68 - local_68._4_1_) == -6)) &&
        (((((((byte)(local_68._5_1_ - local_70._2_1_) == -0x2a &&
             ((byte)((byte)local_78 - (char)local_58) == '\b')) &&
            (((char)(local_58._7_1_ - (char)local_80) == -0x2b &&
             (((byte)(local_70._2_1_ * local_88._7_1_) == -0x13 &&
              ((char)(local_88._4_1_ * (char)local_70) == -0x38)))))) &&
           ((local_68._2_1_ ^ local_70._4_1_) == 0x55)) &&
          (((((byte)(local_70._6_1_ - local_58._7_1_) == '4' &&
             ((byte)(local_50._3_1_ + local_58._2_1_) == -0x71)) &&
            ((byte)(local_60._4_1_ + local_70._3_1_) == -0x2a)) &&
           (((local_78._1_1_ ^ local_80._6_1_) == 0x31 &&
            ((byte)((byte)local_50 * local_78._4_1_) == -0x54)))))) &&
         (((((byte)(local_50._2_1_ - local_70._2_1_) == -0x3e &&
            (((local_70._2_1_ ^ local_88._6_1_) == 0x2f &&
             ((local_80._6_1_ ^ local_68._7_1_) == 0x5a)))) &&
           ((local_60._4_1_ ^ local_68._7_1_) == 0x40)) &&
          ((((((byte)local_60 == local_70._2_1_ &&
              ((byte)(local_78._7_1_ + local_58._1_1_) == -0x68)) &&
             ((byte)(local_78._7_1_ * local_50._3_1_) == 'h')) &&
            (((byte)(local_88._1_1_ - local_70._4_1_) == -0x25 &&
             ((byte)((char)local_70 - local_70._5_1_) == -0x2e)))) &&
           (((char)(local_68._6_1_ - (char)local_70) == '.' &&
            ((((byte)local_68 ^ local_78._6_1_) == 0x1a &&
             ((byte)(local_60._4_1_ * local_88._4_1_) == -0x60)))))))))))) &&
       ((((((byte)(local_68._6_1_ * local_70._3_1_) == '^' &&
           ((((byte)(local_80._7_1_ - (byte)local_60) == -0x38 &&
             ((local_58._1_1_ ^ local_58._5_1_) == 0x56)) &&
            ((local_70._2_1_ ^ local_60._5_1_) == 0x2b)))) &&
          ((((((local_58._6_1_ ^ local_80._1_1_) == 0x19 &&
              ((byte)(local_70._4_1_ - local_60._7_1_) == '\x1a')) &&
             (((byte)(local_58._2_1_ + local_78._3_1_) == -0x5f &&
              (((byte)(local_68._5_1_ + local_50._1_1_) == 'V' &&
               ((local_70._5_1_ ^ local_78._2_1_) == 0x38)))))) &&
            ((local_60._4_1_ ^ local_50._4_1_) == 9)) &&
           ((((((char)(local_80._7_1_ * local_68._6_1_) == 'y' &&
               ((local_68._5_1_ ^ local_70._6_1_) == 0x5d)) &&
              ((byte)(local_88._2_1_ * (byte)local_68) == '\\')) &&
             (((byte)(local_80._2_1_ * local_78._2_1_) == '9' && (local_70._5_1_ == local_78._5_1_))
             )) && (((byte)(local_68._3_1_ * local_78._5_1_) == '/' &&
                    (((byte)((char)local_80 * local_68._5_1_) == -0x55 &&
                     ((byte)(local_68._7_1_ + local_70._2_1_) == -0x6d)))))))))) &&
         (((((((local_70._2_1_ ^ local_68._2_1_) == 0x73 &&
              ((((local_78._4_1_ ^ local_70._7_1_) == 0x40 &&
                ((byte)(local_70._1_1_ + (byte)local_78) == -0x57)) &&
               ((local_68._7_1_ ^ local_50._3_1_) == 0x15)))) &&
             ((((byte)((byte)local_88 + local_50._3_1_) == 'i' &&
               ((byte)(local_68._2_1_ + local_60._6_1_) == -0x5b)) &&
              (((local_70._6_1_ ^ local_58._4_1_) == 0x37 &&
               (((byte)((byte)local_88 * local_70._4_1_) == '\b' &&
                ((byte)(local_68._2_1_ - (byte)local_50) == -0x3b)))))))) &&
            ((byte)(local_78._2_1_ + local_50._4_1_) == -0x1c)) &&
           (((((local_68._3_1_ ^ (byte)local_60) == 0x6e &&
              ((byte)((byte)local_50 * (byte)local_78) == -0x54)) &&
             ((byte)(local_58._6_1_ - local_60._7_1_) == '\r')) &&
            ((((byte)(local_70._6_1_ + local_58._7_1_) == -100 &&
              ((byte)(local_88._6_1_ + local_68._1_1_) == -0x2c)) &&
             (((byte)(local_88._7_1_ * local_70._5_1_) == -0x13 &&
              ((((byte)local_50 ^ local_70._5_1_) == 0x38 &&
               ((byte)(local_88._1_1_ * local_68._5_1_) == 'd')))))))))) &&
          ((((byte)local_50 ^ local_50._2_1_) == 0x46 &&
           (((((((char)(local_88._2_1_ * local_78._3_1_) == '&' &&
                ((local_70._2_1_ ^ local_78._6_1_) == 0x2b)) &&
               ((byte)(local_88._1_1_ + local_88._7_1_) == -0x79)) &&
              (((local_70._3_1_ ^ (byte)local_88) == 0x2a &&
               ((byte)(local_78._5_1_ - local_88._1_1_) == '\v')))) &&
             ((byte)(local_70._3_1_ + local_58._6_1_) == -0x32)) &&
            (((local_78._1_1_ ^ local_80._5_1_) == 0x3b &&
             ((byte)(local_78._3_1_ - local_50._2_1_) == '\x12')))))))))) &&
        ((((local_78._1_1_ == local_80._2_1_ &&
           ((((byte)(local_80._6_1_ - local_50._2_1_) == 'M' &&
             ((byte)(local_60._2_1_ * local_58._4_1_) == 'N')) && (local_58._2_1_ == (byte)local_68)
            ))) && (((local_60._7_1_ ^ local_58._3_1_) == 0x38 &&
                    ((char)(local_68._6_1_ + local_70._1_1_) == -0x6c)))) &&
         ((byte)(local_60._1_1_ + local_58._4_1_) == -0x31)))))) &&
      ((((local_60._4_1_ == local_78._4_1_ && ((char)(local_80._4_1_ + local_70._1_1_) == 'f')) &&
        (((byte)(local_50._4_1_ + local_68._4_1_) == -0xf &&
         ((((byte)(local_60._1_1_ - local_78._5_1_) == '\x11' &&
           ((byte)(local_68._4_1_ - local_58._1_1_) == 'D')) &&
          ((byte)(local_80._1_1_ - local_68._3_1_) == 'D')))))) &&
       ((((local_58._5_1_ ^ local_58._3_1_) == 1 && ((local_68._2_1_ ^ local_50._1_1_) == 0xd)) &&
        ((((byte)(local_80._3_1_ - local_70._4_1_) == -0x15 &&
          (((((char)(local_78._7_1_ + (char)local_70) == -0x67 &&
             ((byte)((char)local_70 + local_80._5_1_) == -0x6b)) &&
            (((byte)(local_80._4_1_ - (byte)local_88) == -0x17 &&
             (((((byte)(local_68._2_1_ + local_70._7_1_) == '`' &&
                ((byte)(local_88._5_1_ + local_58._5_1_) == -0x6a)) &&
               ((byte)(local_58._1_1_ * local_60._2_1_) == '`')) &&
              (((byte)((char)local_58 * local_78._5_1_) == '\x14' &&
               ((byte)(local_70._3_1_ - local_58._4_1_) == '\x03')))))))) &&
           ((byte)(local_50._1_1_ + local_78._4_1_) == -0x6b)))) &&
         ((((byte)(local_80._2_1_ * local_58._5_1_) == -0x26 &&
           ((byte)(local_88._1_1_ + local_60._1_1_) == -0x3c)) &&
          (((byte)(local_60._7_1_ - local_88._1_1_) == '\v' &&
           (((local_60._3_1_ == local_78._3_1_ && ((byte)(local_68._7_1_ + local_60._7_1_) == -0x6d)
             ) && ((byte)(local_80._4_1_ * local_50._2_1_) == 'Q')))))))))))))) &&
     (((((byte)((char)local_80 * local_70._2_1_) == 'A' &&
        ((byte)(local_60._6_1_ - local_70._7_1_) == 'E')) &&
       ((byte)(local_88._7_1_ + local_68._5_1_) == 'h')) &&
      (((((char)(local_68._4_1_ + local_88._4_1_) == -0x44 &&
         ((byte)(local_70._7_1_ + (byte)local_68) == -0x5e)) &&
        (((char)(local_70._1_1_ + local_88._5_1_) == 'e' &&
         ((((byte)(local_60._3_1_ * local_70._5_1_) == -0x13 &&
           ((local_80._5_1_ ^ local_60._5_1_) == 0x10)) &&
          ((char)((char)local_58 - local_80._4_1_) == ';')))))) &&
       (((((char)(local_78._7_1_ - (char)local_80) == '\t' &&
          ((local_88._7_1_ ^ local_60._2_1_) == 0x41)) &&
         ((char)(local_88._5_1_ - local_60._3_1_) == -3)) &&
        (((((local_50._4_1_ ^ local_78._2_1_) == 0x1a && ((local_88._1_1_ ^ local_88._3_1_) == 0x2f)
           ) && (((byte)(local_78._1_1_ - local_68._7_1_) == '+' &&
                 (((((byte)((char)local_80 + local_78._4_1_) == -0x2d &&
                    ((byte)(local_80._3_1_ * local_58._5_1_) == -0x28)) &&
                   ((byte)(local_70._3_1_ + local_88._6_1_) == -0x2e)) &&
                  (((byte)(local_88._5_1_ + local_88._3_1_) == -0x55 &&
                   ((byte)(local_68._3_1_ - local_60._7_1_) == -0x2e)))))))) &&
         (((byte)local_78 ^ local_68._1_1_) == 0x10)))))))))) {
    puts("Freedom at last!");
  }
  else {
    puts("Lost in the darkness, you\'ll wander for eternity...");
  }
  return 0;
}
```
