# Shooting-101

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: Your metallic body might have advanced targeting systems, but hitting a target is not just about technical proficiency. To truly master the art of targeting, you must learn to trust your instincts and develop a keen sense of intuition. During this training, you will emerge as a skilled marksman who can hit the targets with deadly precision. It's about time to train and prove yourself in the Shooting Area, can you make it?

## NOTES

1. Deploy Docker
   1. > IP: 165.227.224.40:30716
   2. > IP: 165.227.224.40:30571
2. Extract files
   1. > unzip blockchain_shooting_101.zip
      1. FILE(S): Setup.sol, ShootingArea.sol
3. Run NC
   1. > nc 165.227.224.40 30716 -> RPC
   2. > nc 165.227.224.40 30571 -> TCP
      1. RESPONSE:
         1. Connection Information
         2. Restart Instance
         3. Get Flag
         4. Action: [USER_INPUT_HERE]
      2. Get the connection information
         1. Private key     :  0xb269e06de08cb5349eae33922f87b225b0cc8f338f12f8d14c7e57eeddc44572
         2. Address         :  0xCA24679EC17D5dE10799A5798B883034646a0195
         3. Target contract :  0x6e68350f0851E6e68159F30b9DeB86092EE6fd04
         4. Setup contract  :  0x1De97ec03D3CafF6C8484FF4FDb012C1cfe5aDc5
4. Examine files
   1. Setup.sol
      1. In here we see
         1. Import -> shootingarea.sol
         2. Constructor
            1. This creates a new ShootingArea Object
         3. Functino -> isSolved()
            1. This function checks for the TARGET.firstShot() && TARGET.secondShot() && TARGET.thirdShot()
   2. ShootingArea.sol
      1. In here we see
         1. 3 public boolean variables
            1. first, second, & thirdshot
         2. 3 modifiers
            1. firstTarget, secondTarget, thirdTarget
            2. each of these require the previous shot value to be true
         3. 3 functions
            1. recieve() -> sets secondshot = true
            2. fallback() -> sets firstshot = true
            3. third() -> sets thirdshot = true
5. General Flow
   1. So based on reading through each of the .sol files we know we need to accomplish a few steps
      1. Call recieve() -> set firstShot=true
6. Web3py
   1. We will go back to our web3py library to create a script
   2. We need to get the ABI structure of each .sol file
7. REMIX.ORG
   1. Uploading our .sol files we can then copy the ABI structure
8. Research
   1. modifiers in solidity
      1. the `_;` symbol is called a merge wildcard. It merges the function code with the modifier code where the `_;` is placed.
      2. So this means the the main chunk of the code will take the place of the merge wildcard
