# Persistence

## FLAG: HTB{y0u_h4v3_p0w3rfuL_sCr1pt1ng_ab1lit13S!}

## Status: Complete

+ DOCKER: Yes
+ DOWNLOADABLE: No

Description: Thousands of years ago, sending a GET request to /flag would grant immense power and wisdom. Now it's broken and usually returns random data, but keep trying, and you might get lucky... Legends say it works once every 1000 tries.

## NOTES

1. Deploy Docker
   1. > IP: 46.101.80.159:30465
2. GET REQUEST
   1. Lets do a test request to /flag endpoint
      1. > curl 46.101.80.159:30465/flag
         1. RESPONSE: `RXOR|3G6vpzfTx{dV^Dgh`
         2. This gives us a scrambled text
         3. BUT the description mentiond it could take 1000 tries
         4. SO lets make a bash script to loop 1000 times requestion the flag
3. SCRIPT
   1. Bash code

        ```bash
            #!/bin/bash
            for i in {1..1000}
            do
                curl 46.101.80.159:30465/flag
            done
        ```

   2. Now run the script and pipe the content out to a log.txt file, so we can search for the flag with grep
4. FLAG
   1. After about 260 iterations we get the flag
      1. FLAG: `HTB{y0u_h4v3_p0w3rfuL_sCr1pt1ng_ab1lit13S!}`
