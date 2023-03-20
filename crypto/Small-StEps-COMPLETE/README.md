# Small-StEps

## FLAG: HTB{5ma1l_E-xp0n3nt}

## Status: Complete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: As you continue your journey, you must learn about the encryption method the aliens used to secure their communication from eavesdroppers. The engineering team has designed a challenge that emulates the exact parameters of the aliens' encryption system, complete with instructions and a code snippet to connect to a mock alien server. Your task is to break it.

## NOTES

1. Deploy Docker
   1. > IP: 138.68.158.112:32060
2. Extract files
   1. > unzip crypto_small_steps.zip
      1. FILE(S): solver.py, server.py, README
3. Examine code
   1. README
      1. In here we see a set of instructions that give us options for interacting with the server via a py script or using nc
      2. We are also given a hint *The implementation is textbook RSA, except for the value of `e`.*
   2. SERVER.py
      1. In here we see the interworkings of how the flag is encrypted
      2. This looks to be basic RSA encryption where p & q are some 256 bit prime number, BUT!! e is very small!
   3. SOLVER.py
      1. This looks mainly like another way to connect to the remote connection for newer users
4. DECRYPT
   1. First lets run establish a connection and see what is given
      1. > nc 138.68.158.112 32060
         1. RESPONSE:

            ```text
                The public key is:
                N: 8970056788222527566085506940333173778072139754940358635597806287462141933660773927726745943402524667524890744187817833838988672827181215507057185488063397
                e: 3

                The encrypted flag is: 70407336670535933819674104208890254240063781538460394662998902860952366439176467447947737680952277637330523818962104685553250402512989897886053
            ```

      2. We see that we are given the encrypted flag, the public key (N), and the e value used
      3. NOTE
         1. N = 8970056788222527566085506940333173778072139754940358635597806287462141933660773927726745943402524667524890744187817833838988672827181215507057185488063397
         2. enc = 70407336670535933819674104208890254240063781538460394662998902860952366439176467447947737680952277637330523818962104685553250402512989897886053
         3. So if our plaintext ^ e < N then we can exploit
   2. Go to factordb
      1. Input: enc_flag
      2. Output: we get the cube root = 412926389432612660984016953290834154417829082237
   3. Decrypt this from long_to_bytes
      1. Write a quick python script to decrypt this

        ```py
            #!/usr/bin/env python3

            from Crypto.Util.number import long_to_bytes
            message = 412926389432612660984016953290834154417829082237
            dec = long_to_bytes(message)
            print(dec)
        ```

   4. We get the value : `b'HTB{5ma1l_E-xp0n3nt}'`
   5. So our flag is
      1. FLAG: `HTB{5ma1l_E-xp0n3nt}`