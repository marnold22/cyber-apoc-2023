# Initialise-Connection

## FLAG: HTB{g3t_r34dy_f0r_s0m3_pwn}

## Status: Complete

+ DOCKER: Yes
+ DOWNLOADABLE: No

Description: In order to proceed, we need to start with the basics. Start an instance, connect to it via $ nc e.g. nc 127.0.0.1 1337 and send 1 to get the flag.

## NOTES

1. This tells us we need to send '1' to our nc connection
2. Deploy Docker
   1. IP: 167.71.143.44:31262
3. NetCat
   1. > nc 167.71.143.44 31262
      1. RESPOSNE: "Enter 1 to get the flag!"\
   2. > 1
      1. RSEPONSE:
         1. `HTB{g3t_r34dy_f0r_s0m3_pwn}`
