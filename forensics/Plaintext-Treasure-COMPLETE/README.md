# Plaintext-Treasure

## FLAG: HTB{th3s3_4l13ns_st1ll_us3_HTTP}

## Status: Incomplete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: Threat intelligence has found that the aliens operate through a command and control server hosted on their infrastructure. Pandora managed to penetrate their defenses and have access to their internal network. Because their server uses HTTP, Pandora captured the network traffic to steal the server's administrator credentials. Open the provided file using Wireshark, and locate the username and password of the admin.

## NOTES

1. Extract the content
   1. > unzip forensics_plaintext_treasure.zip
      1. FILE: capture.pcap
      2. Since a pcap file lets open with wireshark
2. WIRESHARK
   1. There is quite a bit of TCP connections but we also see HTTP protocols
   2. Sort by Protocol
   3. Looking throught the HTTP we see several that say (text/plain) and given the title of the challenge lets look at thses
   4. FOLLOW HTTP STREAM
      1. And in the first POST we see

        ```text
            POST /token HTTP/1.1
            Host: 192.168.1.30:1337
            User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
            Accept: application/json, text/plain, */*
            Accept-Language: en-US,en;q=0.5
            Accept-Encoding: gzip, deflate
            Content-Type: multipart/form-data; boundary=---------------------------4236021980508159708606749430
            Content-Length: 332
            Origin: http://192.168.1.30:4173
            Connection: keep-alive
            Referer: http://192.168.1.30:4173/

            -----------------------------4236021980508159708606749430
            Content-Disposition: form-data; name="username"

            cosmic-operator
            -----------------------------4236021980508159708606749430
            Content-Disposition: form-data; name="password"

            HTB{th3s3_4l13ns_st1ll_us3_HTTP}
            -----------------------------4236021980508159708606749430--
        ```

   5. With the FLAG: `HTB{th3s3_4l13ns_st1ll_us3_HTTP}`
