# Pascket-Cyclone

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: Pandora's friend and partner, Wade, is the one that leads the investigation into the relic's location. Recently, he noticed some weird traffic coming from his host. That led him to believe that his host was compromised. After a quick investigation, his fear was confirmed. Pandora tries now to see if the attacker caused the suspicious traffic during the exfiltration phase. Pandora believes that the malicious actor used rclone to exfiltrate Wade's research to the cloud. Using the tool called chainsaw and the sigma rules provided, can you detect the usage of rclone from the event logs produced by Sysmon? To get the flag, you need to start and connect to the docker service and answer all the questions correctly.

## NOTES

1. Extract files
   1. > unzip forensics_packet_cyclone.zip
      1. FILE: Log/*.evtx
         1. These look like they are Event Logs (Windows Machine) stored in XML
      2. FILE: sigma_rules/*yaml
         1. These look like config or rule type files
2. Event Viewer
   1. Lets open up windows event viewer and import these log files
