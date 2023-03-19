# Drobots

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: Pandora's latest mission as part of her reconnaissance training is to infiltrate the Drobots firm that was suspected of engaging in illegal activities. Can you help pandora with this task?

## NOTES

1. Deploy Docker
   1. > IP: 46.101.90.48:32025
2. Extract files
   1. > unzip web_drobots.zip
      1. FILES: Webserver files (web_drobots)
3. Navigate to website
   1. This directs us to a login form
4. Looking at the code
   1. Starting in the ROUTES.py we see

        ```py
            flag = open('/flag.txt').read()
            @web.route('/home')
            @isAuthenticated
            def home():
                return render_template('home.html', flag=flag)
        ```

   2. This shows us our flag being loaded adn is accessible from the route /home
   3. This means we need to successfully authenticate and login
      1. Which means we need a successful **username** & **password**
   4. Lets keep exploring for these
5. ENTRYPOINT.sh
   1. In here we see the database script that generates/populates the DB
      1. SCRIPT

            ```sql
                mysql -u root << EOF
                CREATE DATABASE drobots;
                CREATE TABLE drobots.users (
                    id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    username varchar(255) NOT NULL UNIQUE,
                    password varchar(255) NOT NULL
                );
                INSERT INTO drobots.users (username, password) VALUES ('admin', '$(genPass)');
                CREATE USER 'user'@'localhost' IDENTIFIED BY 'M@k3l@R!d3s$';
                GRANT SELECT, INSERT, UPDATE ON drobots.users TO 'user'@'localhost';
                FLUSH PRIVILEGES;
                EOF
            ```

   2. In this script we see that a value of `admin` is set for the username and then it calls the $genPass function to generate a password
   3. Lets see if we can see how they authenticate in terms of the actual query
6. DATABASE.py
   1. In here we see the following query

        ```py
            # We should update our code base and use techniques like parameterization to avoid SQL Injection
            user = query_db(f'SELECT password FROM users WHERE username = "{username}" AND password = "{password}" ', one=True)
        ```

   2. This gives us two major pieces of information
      1. We get the hint talking about "preventing SQL Injection"
      2. We see that the **password** is the only thing being selected from the database

1' AND 1=1 --+