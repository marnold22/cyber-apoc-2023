# Perfect-Synchronization

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: The final stage of your initialization sequence is mastering cutting-edge technology tools that can be life-changing. One of these tools is quipquip, an automated tool for frequency analysis and breaking substitution ciphers. This is the ultimate challenge, simulating the use of AES encryption to protect a message. Can you break it?

## NOTES

1. Extract files
   1. > unzip crypto_perfect_synchronization.zip
      1. FILE(S): source.py, output.txt
2. Examine code
   1. OUTPUT.txt
      1. This lookslike our encoded flag
      2. However when looking closer I see that several of the lines are repeated throughout the
   2. SOURCE.py

    ```py
        from os import urandom
        from Crypto.Cipher import AES
        from secret import MESSAGE

        assert all([x.isupper() or x in '{_} ' for x in MESSAGE])

        class Cipher:

            def __init__(self):
                self.salt = urandom(15)
                key = urandom(16)
                self.cipher = AES.new(key, AES.MODE_ECB)

            def encrypt(self, message):
                return [self.cipher.encrypt(c.encode() + self.salt) for c in message]


        def main():
            cipher = Cipher()
            encrypted = cipher.encrypt(MESSAGE)
            encrypted = "\n".join([c.hex() for c in encrypted])

            with open("output.txt", 'w+') as f:
                f.write(encrypted)


        if __name__ == "__main__":
            main()
    ```

      1. In here we see
         1. salt = 15-bytes
         2. key = 16-bytes
         3. AES(ECB_MODE) so we know that there is potentially a block attack
3. RESEARCH
   1. It looks like that AES is vulnerable to copy-paste attack if ECB is enabled, which is what we see in the code
   2. The secret word will then be ciphered with each character
4. EXPLOIT
   1. Lets grab the original script and create our own message to see if we can identfy the block size
   2. MODIFY SCRIPT

        ```py
            from os import urandom
            from Crypto.Cipher import AES

            MESSAGE = "A"

            assert all([x.isupper() or x in '{_} ' for x in MESSAGE])


            class Cipher:

                def __init__(self):
                    self.salt = urandom(15)
                    key = urandom(16)
                    self.cipher = AES.new(key, AES.MODE_ECB)

                def encrypt(self, message):
                    return [self.cipher.encrypt(c.encode() + self.salt) for c in message]


            def main():
                cipher = Cipher()
                encrypted = cipher.encrypt(MESSAGE)
                encrypted = "\n".join([c.hex() for c in encrypted])

                with open("output.txt", 'w+') as f:
                    f.write(encrypted)


            if __name__ == "__main__":
                main()
        ```

       1. In here I am modifying the MESSAGE = "A" so only 1 letter of our plaintext message is being encrpyted
          1. Our response is `44d15c8221fe92f3774feee5fedd1bbb`
          2. And this response is 32 bytes long
       2. So now we want to add more "A"'s to increase our plaintext and see at which point our response increases. That way we know how many characters 1 block is
   3. INCREMENT A's
      1. By adding 1 extra "A" we now have two blocks of 32 bytes in our response. So this tells me each letter/character of the plaintext is its own block
         1. This makes sense because the salt is 15bytes and the key is 16 bytes so 15+16 = 31, plus our 1 character from plaintext which gives us our block of 32
