# Roten

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: The iMoS is responsible for collecting and analyzing targeting data across various galaxies. The data is collected through their webserver, which is accessible to authorized personnel only. However, the iMoS suspects that their webserver has been compromised, and they are unable to locate the source of the breach. They suspect that some kind of shell has been uploaded, but they are unable to find it. The iMoS have provided you with some network data to analyse, its up to you to save us.

## NOTES

1. Extract files
   1. > unzip forensics_roten.zip
      1. FILE: challenge.pcap
      2. Since this is a PCAP file lets examine it in Wireshark
2. WIRESHARK
   1. Statistics -> Protocol Hierarchy
      1. In here we see the majority of the information/traffic is TCP, and under the TCP category the next majoprity is HTTP. So more than likely tons of GET & POST requests
      2. We see several attempts at trying to find the endpoint galactic.php
         1. GET /SOME_VALUE_HERE/galactic.php -> with everal 404's meaning it wasn't found
         2. They do find a /uploads directory
            1. Then they find the galactic.php file under /uploads
      3. Galacticmap.php?dir=%2fvar%2fwww%2fhtml%2fuploads&cmd=[COMMAND_HERE]
         1. It looks like the attacker was using LFI to try and run commands
            1. > whoami [No.18511]
               1. www-data [No.18513]
            2. > ls [No.18535]
               1. boot, dev, etc, home... What looks like a normal linux file system [No.18537]
      4. map-update.php
         1. It looks like there were several PDF's of mapus being uploaded to this page
            1. aus-map.pdf
            2. asia-map.pdf
