# Capstone-Project


## Seller Page 

We use Python and utilsise Streamlit to create a web-based interface for interacting with a smart contract on the Ethereum blockchain.

#### Installation Instructions

os - handling operating system operations.
json - for working with JSON objects.
Streamlit - creating web-based interfaces.
Web3 - connecting to the Ethereum network.
pathlib - for working with file paths.
dotenv - loading environment variables.

The Web interface has three main sections; Register New Artwork, Edit the Product Listing & Get Price History. 

### Register New Artwork

This section allows the user to input details of a new artwork (name, artist name, price, and URI), which are then submitted to the smart contract. When the user clicks the "Register Artwork" button, the contract's "registerArtwork" function is called with the provided parameters, and a transaction is submitted to the Ethereum network.

### Edit the Product Listing

The edit function allows the user to select an existing artwork token ID and update its price using the "editPrice" function in the smart contract. The user can also enter notes about the change, which are recorded as part of the transaction.

### Get Price History

We allow the user to enter an artwork token ID and retrieve the price history for that artwork. The script creates an event filter using the contract's "Appraisal" event, which is emitted whenever the price of an artwork is updated. The filter is set to retrieve all events with the specified artwork token ID and then returns the event logs and arguments associated with each event.

Overall the Seller Page provides a user freidnly interface for interacting with the Ethereum smart contract allowing users to register new artwork, update artwork prcies and retriefe proce history.


## Buyer Page 

### Creation of Wallet 

#### Installation Instructions

We import the necessary Python libraries for interacting with Ethereum:

os 
requests 
dotenv 
bip44 
web3 
Account

### Wallet Function 

The wallet composes of three main functions: Generate the account, Get Balance and Sending Transactions.

Generate Acc


