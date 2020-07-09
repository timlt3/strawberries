# strawberries
COMP6452 Assignment 2 Code
Timothy WU
Yanjie (Henry) WANG
Manlin WANG

TODO (open) 
take the smart contract code and add functionality so that only the assigned role can sign off on a particular stage of the product.

i.e. make new hashes for each of the stages 
mapping (address => Friend) public pickers;
mapping (address => Friend) public processors;
...
etc etc 

and make additional functions that only allow for one stage change: 
e.g. 

function pickerSignoff(uint sID) public returns (bool){
        bool updated = false; 
        if (bytes(friends[msg.sender].name).length != 0) { // Friend exist TODO make sure this guy is a picker as well
            if (bytes(strawberries[sID].message).length != 0) {       //valid strawberry id  
                strawberries[sID].status = status.processing; //after the picking phase is complete the picker can set it to the following phase
                updated = true; 
            } 
        }
        return updated; 
    }
