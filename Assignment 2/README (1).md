
# Solidity: METACOIN

## 1. Brief Introduction
In this program, solidity is used to create a smart contract: MetaCoin
which basically implements a basic token which the accounts can
give to each other with the sendCoin function, and see their balance with 
the getBalance function. 

The smartcontract's functionality was further to provide the
functionality of acting as a loan deposit and settling 
contract

There is an Owner of the Loan contract with 
an initial balane of 100K MetaCoins, as in the constructor of 
the MetaCoin class, With the assumption that this amount has been 
accumulated by taking loans. He would store the debt he is in to each 
creditor in a mapping called loans.

## 2. Working
### The various functions used are as following:

 1. getCompoundInterest : allows anyone(therefore puplic) to use it
to calculate the amount of interest for given values of P, R, T (in years). 
(interest rate as a whole number). The compound Interest(compounded annually) 
has been calculated in an iterative way. 
 

2. reqLoan: anyone(therefore public) should be able to use it to request
 the Owner to settle his loan. The P, R, T are entered is used to calculate the 
 dues, and is added to a mapping. In the end the Request event is emitted.

3. getOwnerBalance: anyone(therefore public) can use it to get the amount of 
MetaCoins owned by the owner.  

4. viewDues : only the owner(kept public, but used isOwner 
function to allow 
only the owner to access it) can access this to view the amount 
of loan he owes to the input address, which is stored in the loans
 mapping.

5. settleDues: only the owner(kept public, but used isOwner 
function to allow 
only the owner to access it) can use this to settle the amount 
of loan he owes to the input address, use MetaCoin's sendCoin 
function to settle these dues, with appropriate checks for the
 return values from sendCoin. 
## 3. SAMPLE INPUT 
owner address=0x5B38Da6a701c568545dCfcB03FcB875f56beddC4
After adding the code to remix ide, and deploying the code, the function of the code can be used:
1. reqLoan: In this function the inputs can be:
principle=500
rate=5
time=3
2. sendCoin: In this function address can be acquired from the predefined addresses of remix:
sender address:0x5B38Da6a701c568545dCfcB03FcB875f56beddC4
amount:5000
receiver address:0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2
3. settleDues: 
creditor address: 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4
4. getbalance:
for sender: 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4
expected output for sender/owner=95000
for receiver: 0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2
expected output for receiver=5000
