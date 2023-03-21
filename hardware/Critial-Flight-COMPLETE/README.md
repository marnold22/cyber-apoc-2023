# Critial-Flight

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: Your team has assigned you to a mission to investigate the production files of Printed Circuit Boards for irregularities. This is in response to the deployment of nonfunctional DIY drones that keep falling out of the sky. The team had used a slightly modified version of an open-source flight controller in order to save time, but it appears that someone had sabotaged the design before production. Can you help identify any suspicious alterations made to the boards?

## NOTES

1. Extract files
   1. > unzip hw_critical_flight.zip
      1. FILE(S): flight_control_board -> HadesMicro*.gbr
2. Examine files
   1. > file HadesMicro-B_Cu.gbr
      1. RESPONSE: `HadesMicro-B_Cu.gbr: ASCII text, with CRLF line terminators`
3. RESEARCH
   1. It looks like .gbr files are used in circuit board designs so lets download some circuitboard design software so we can open these up
   2. Install gerbv
      1. > apt isntall gerbv
4. GERBV
   1. Open all of the Hades*.gbr files
   2. On the left we can see all our layers
   3. BUT!! In the viewer we the circuit board, and our flag is on the board
      1. However, this is just part of the flag, we can see the rest as we toggle the different layers
         1. LAYER: HadesMicro-B_Cu.gbr
            1. `HTB{533_7h3_1nn32_w02k1n95`
         2. LAYER: HadesMicro-In1_Cu.gbr
            1. `_0f_313c720n1c5#$@}`
   4. Combinine to get flag
      1. FLAG: `HTB{533_7h3_1nn32_w02k1n95_0f_313c720n1c5#$@}`
