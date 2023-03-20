# Ancient-Encodings

## FLAG: HTB{1n_y0ur_j0urn3y_y0u_wi1l_se3_th15_enc0d1ngs_ev3rywher3}

## Status: Complete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: Your initialization sequence requires loading various programs to gain the necessary knowledge and skills for your journey. Your first task is to learn the ancient encodings used by the aliens in their communication

## NOTES

1. Extract files
   1. > unzip crypto_ancient_encodings.zip
      1. FILE(S): source.py, output.txt
2. Examine the code
   1. Looking at source.py

        ```py
            from Crypto.Util.number import bytes_to_long
            from base64 import b64encode

            FLAG = b"HTB{??????????}"


            def encode(message):
                return hex(bytes_to_long(b64encode(message)))


            def main():
                encoded_flag = encode(FLAG)
                with open("output.txt", "w") as f:
                    f.write(encoded_flag)


            if __name__ == "__main__":
                main()
        ```

      1. In here we see that the flag is encoded using hex(bytes_to_long(base64())) and then written to an output.txt file
   2. Looking at the output.txt file we see
      1. `0x53465243657a467558336b7764584a66616a4231636d347a655639354d48566664326b786246397a5a544e66644767784e56396c626d4d775a4446755a334e665a58597a636e6c33614756794d33303d`
      2. This is a giant hex string so lets reverse the process and decode it
3. DECODE
   1. First we need to "undo" the hex
      1. Cyberchef -> FROM HEX
         1. RESPONSE: `SFRCezFuX3kwdXJfajB1cm4zeV95MHVfd2kxbF9zZTNfdGgxNV9lbmMwZDFuZ3NfZXYzcnl3aGVyM30=`
   2. Now it looks like we have base64 to lets decode that
      1. Cyberchef -> FROM BASE64
         1. RESPONSE: `HTB{1n_y0ur_j0urn3y_y0u_wi1l_se3_th15_enc0d1ngs_ev3rywher3}`
