# Restricted

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: You 're still trying to collect information for your research on the alien relic. Scientists contained the memories of ancient egyptian mummies into small chips, where they could store and replay them at will. Many of these mummies were part of the battle against the aliens and you suspect their memories may reveal hints to the location of the relic and the underground vessels. You managed to get your hands on one of these chips but after you connected to it, any attempt to access its internal data proved futile. The software containing all these memories seems to be running on a restricted environment which limits your access. Can you find a way to escape the restricted environment ?

## NOTES

1. Deploy Docker
   1. > IP: 209.97.134.50:30806
2. Extract files
   1. > unzip misc_restricted.zip
      1. FILE(S): Docker Build
3. Examine files
   1. Looking at the docker file we see

        ```docker
            FROM debian:latest

            RUN apt update -y && apt upgrade -y && apt install openssh-server procps -y

            RUN adduser --disabled-password restricted
            RUN usermod --shell /bin/rbash restricted
            RUN sed -i -re 's/^restricted:[^:]+:/restricted::/' /etc/passwd /etc/shadow

            RUN mkdir /home/restricted/.bin
            RUN chown -R restricted:restricted /home/restricted

            RUN ln -s /usr/bin/top /home/restricted/.bin
            RUN ln -s /usr/bin/uptime /home/restricted/.bin
            RUN ln -s /usr/bin/ssh /home/restricted/.bin

            COPY src/sshd_config /etc/ssh/sshd_config
            COPY src/flag.txt /flag.txt
            COPY src/bash_profile /home/restricted/.bash_profile

            RUN chown root:root /home/restricted/.bash_profile
            RUN chmod 755 /home/restricted/.bash_profile
            RUN chmod 755 /flag.txt

            RUN mv /flag.txt /flag_`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 5 | head -n 1`

            RUN ssh-keygen -A
            RUN mkdir -p /run/sshd

            EXPOSE 1337

            ENTRYPOINT ["/usr/sbin/sshd", "-D", "-o", "ListenAddress=0.0.0.0", "-p", "1337"]
        ```

   2. We see that:
      1. a user is added
      2. a directory is made
      3. sumbolic links are established for /usr/bin/top, /usr/bin/uptime, /usr/bin/ssh
      4. sshd_conf file is copied from src
      5. flag file is copied from src
