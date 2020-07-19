pragma solidity ^0.6.0; 

contract Strawberries{

    struct Strawberry {
        uint ID; 
        Phases phase; 
        Status status; 
        string message;
        string[] history; 
    }
    
    struct Friend{ 
        string name;
        Roles role;
    } 
    
    mapping(uint => Strawberry) public strawberries; //list of strawberries(id -> strawberry)
    mapping (address => Friend) public friends;
    
    enum Roles {Picker, Processor, Packer, Transporter, Seller} //0 1 2 3 
    enum Phases {Picking, Processing, Packing, Transporting, Selling}
    enum Status {Good, Warning, UnfitForSale} 

    
    uint public numStrawberries = 0;
    uint public numFriends = 0; 
    address public administrator; 
    
    //creates a new contract 
    constructor() public {
        administrator = msg.sender; 
    }
    
    //make a strabwerry
    function makeStrawberry() public returns (uint) {
        Strawberry memory myStrawberry;
        myStrawberry.ID = numStrawberries; 
        myStrawberry.phase = Phases.Picking; 
        myStrawberry.status = Status.Good; 
        myStrawberry.message = "I am a strawberry";
        strawberries[numStrawberries] = myStrawberry; 
        numStrawberries++; 
        /*TODO IMPLEMENT HISTORY FUNCTIONALITY SOMEHOW probably will have to communicate with oracle here*/ 
        return numStrawberries; 
    }
    
    //Add a new friend 
    function addFriend(address friendAddress, string memory name, Roles role) public restricted returns (uint){ 
        Friend memory f; 
        f.name = name; 
        f.role = role;
        friends[friendAddress] = f; 
        numFriends++;
        return numFriends; 
    }
    
    function updatePhase(uint sID, Phases phase, Roles role) public returns (bool) {
        bool updated = false;
        if (bytes(friends[msg.sender].name).length != 0 && friends[msg.sender].role != role) { //authorised user to update phase
            if (bytes(strawberries[sID].message).length != 0) {     //valid strawberry id
                strawberries[sID].phase = phase;
                updated = true;
            }
        }
        return updated;
    }
    
    function updateStatus(uint sID, Status status) public returns (bool){
        bool updated = false; 
        if (bytes(friends[msg.sender].name).length != 0) { // Friend exist
            if (bytes(strawberries[sID].message).length != 0) {       //valid strawberry id  
                strawberries[sID].status = status;
                updated = true; 
            } 
        }
        return updated; 
    }
    
     function updateMessage(uint sID, string memory message) public returns (bool){
        bool updated = false; 
        //remove this line if you want to test without adding friends
        if (bytes(friends[msg.sender].name).length != 0) { // Friend exist
            if (bytes(strawberries[sID].message).length != 0) {       //valid strawberry id  
                strawberries[sID].message = message;
                updated = true; 
            } 
        }
        return updated; 
    }
    
    modifier restricted() {
        require(msg.sender == administrator);
        _;
    }
    
                
}
