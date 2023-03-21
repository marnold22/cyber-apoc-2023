# Navigating-The-Unknown

## FLAG: HTB{9P5_50FtW4R3_UPd4t3D}

## Status: Complete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: Your advanced sensory systems make it easy for you to navigate familiar environments, but you must rely on intuition to navigate in unknown territories. Through practice and training, you must learn to read subtle cues and become comfortable in unpredictable situations. Can you use your software to find your way through the blocks?

## NOTES

1. Deploy Docker
   1. > IP: 167.172.50.208:30907 -> this is our RPC connection
   2. > IP: 167.172.50.208:30715 -> this is our TCP connection
2. Run NC
   1. > nc 167.172.50.208 30715
      1. RESPONSE:
         1. 1 - Connection information
         2. 2 - Restart Instance
         3. 3 - Get flag
         4. Action: [USER_INPUT_HERE]
      2. If we ask for connection information we are given
         1. Private key:  0x5e968d0b9f79cfbe2b767a1e01a6976b38e39886ab85a5cb29ac462ea2bb8e4a
         2. Address:  0x6B6c10e42230dB2890f992848b8aE6696eA0dAbb
         3. Target contract:  0x219c147d41e37f0940eB8B1Ab4F99AbB6f0C3Fb9
         4. Setup contract:  0x675b6912B16F1187e97ae51cc7a43bAc672aBC1c
      3. We will need these addresses later
3. Extract files
   1. > unzip blockchain_navigating_unknown.zip
      1. FILE(S): README, Setup.sol, Unknown.sol
4. Examine code
   1. Looking at the setup.sol file we see

        ```s
            pragma solidity ^0.8.18;

            import {Unknown} from "./Unknown.sol";

            contract Setup {
                Unknown public immutable TARGET;

                constructor() {
                    TARGET = new Unknown();
                }

                function isSolved() public view returns (bool) {
                    return TARGET.updated();
                }
            }
        ```

       1. In here we see
          1. an import
             1. This imports our unknown.sol
          2. a constructor
             1. This sets up our TARGET as a new Unknown() object **We will see this in the unknown.sol**
          3. a function -> isSolved
             1. This checks our TARGET (Unknown.sol) for if the updated value is set to true or false
   2. Looking at the unknown.sol file we see

        ```s
            pragma solidity ^0.8.18;


            contract Unknown {
                
                bool public updated;

                function updateSensors(uint256 version) external {
                    if (version == 10) {
                        updated = true;
                    }
                }

            }
        ```

       1. In here we see
          1. a public bool variable `updated`
          2. a function -> updateSensors
             1. This funstion will check if the value is 10, if so set the `updated` bool to true
5. So by examining the code we essentially understand the flow of how things should work
   1. We need to update the sensors so that way the boolean=true
   2. Then we check the isSilved function to hopefully get our flag
6. Now the tricky part is the blockchain/eth part
7. So based on our readme file that was provided
   1. We will interact with the challenge contract
   2. We might need to look into web3py
8. Web3py script
   1. Lets craft a basic py script using the web3py library to see if we can interact with our contracts
      1. > python3 flag.py
      2. Both contracts returned true so we should be able to netcat back in and use option 3 to get our flag
9. NC
   1. > nc 167.172.50.208 30715
   2. > 3 - Get flag
      1. RESPONSE: `FLAG=HTB{9P5_50FtW4R3_UPd4t3D}`
