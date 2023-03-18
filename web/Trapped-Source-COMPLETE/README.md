# Trapped-Source

## FLAG: HTB{V13w_50urc3_c4n_b3_u53ful!!!}

## Status: Complete

+ DOCKER: Yes
+ DOWNLOADABLE: No

Description: Intergalactic Ministry of Spies tested Pandora's movement and intelligence abilities. She found herself locked in a room with no apparent means of escape. Her task was to unlock the door and make her way out. Can you help her in opening the door?

## NOTES

1. Deploy Docker
   1. > IP: 46.101.80.24:30504
2. Navigate to the webpage
   1. We asre brought to a vault that looks like it takes a 4 digit pin
   2. Inspect the source code
      1. Looking at the script portion we see

            ```html
                <script>
                    window.CONFIG = window.CONFIG || {
                        buildNumber: "v20190816",
                        debug: false,
                        modelName: "Valencia",
                        correctPin: "8291",
                    }
                </script>
            ```

      2. This shows us that the correct pin is 8291
   3. Input the pin
      1. FLAG: `HTB{V13w_50urc3_c4n_b3_u53ful!!!}`
