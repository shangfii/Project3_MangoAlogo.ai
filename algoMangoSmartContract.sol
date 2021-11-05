/*

Order Hash:

*/

pragma solidity ^0.5.0;

// Define a new contract named `AlgoMangoOrder`

import "github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";


contract AlgoMangoOrder {
    using SafeMath for uint;

    
address payable public clientsAddress ; //clientsAddress
address payable public companyAddress; //companyAddress

uint public contractBalance;

    /*
       a function named **withdraw** that will accept two arguments.
    - A `uint` variable named `amount`
    - A `payable address` named `recipient`
    */
    
    function withdraw(uint amount, address payable recipient) public {

        /*
        Define a `require` statement that checks if the `recipient` is equal to  `companyAddress`  and returns`"You don't own this account!"` if it does not.
        */
       
        
      require (recipient==companyAddress, "You don't own this account!" );
      
        /*
        Define a `require` statement that checks if the `balance` is sufficient to accomplish the withdraw operation. If there are insufficient funds, the text `Insufficient funds!` is returned.
        */

        
        require (amount <= contractBalance, "Insufficient funds!");

        
        recipient.transfer(amount);
        

        // new balance of the contract.
        
        
        contractBalance = address(this).balance;
    }

    // public payable` function named `deposit`.
    
    function deposit() public payable {

        /*
        contractBalance` variable set to the balance of the contract by using `address(this).balance`.
        */
        
        contractBalance = address(this).balance;
    }
    

    /*
    a `public` function named `setAccount` that receives an `address payable` arguments named `newOrder'
    
    */
    function setAccount(address payable newOrderAddress, address payable companyAddress1) public{
        
        clientsAddress=newOrderAddress;
        companyAddress=companyAddress1;
        
    }

    /*
    default fallback function** so that contract can store Ether sent from outside the deposit function.
    */

    
    function() external payable {}
}
