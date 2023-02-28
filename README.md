# Capstone-Project


## Seller Page 

We use Python and utilsise Streamlit to create a web-based interface for interacting with a smart contract on the Ethereum blockchain.

#### Installation Instructions

* os - handling operating system operations.
* json - for working with JSON objects.
* Streamlit - creating web-based interfaces.
* Web3 - connecting to the Ethereum network.
* pathlib - for working with file paths.
* dotenv - loading environment variables.

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

* os 
* requests 
* dotenv 
* bip44 
* web3 
* Account

### Wallet Function 

The wallet composes of three main functions: Generate the account, Get Balance and Sending Transactions.

#### Generate Account 

This function creates a new Ethereum account by generating a mnemonic seed phrase, creating a new Wallet object from the bip44 library, deriving an Ethereum private key from the mnemonic, and then converting the private key to an Ethereum account using the web3 library. This function returns the newly created account object.

#### Get Balance 

This function takes an Ethereum account address and returns the account's balance in Ether, by first retrieving the account's balance in Wei using the web3 library, then converting the Wei value to Ether. 

#### Send Transaction 

This function sends an Ethereum transaction by constructing a raw transaction object with the given Ethereum account, recipient address, and value in Ether.

Overall, these functions can be used to interact with the Ethereum network, such as by querying an account's balance or sending an authorized transaction to another account on the network.


## Cocktail NFT Buyer Interface 

#### Installation Instructions

* streamlit 
* dataclasses
* typing
* web3

#### Import functions from crypto_wallet.py

* generate_account
* get_balance
* send_transaction

#### Our Cocktails 

The item_database variable is a dictionary that stores the information for each Cocktail NFT. The get_drinks() function is used to display this information on the web interface.

#### Streamlit Code 

We introduce our Cocktail NFT Bar. 

The sidebar contains the client account address, Ethernet balance in ether, a select box to choose a Cocktail NFT, and the NFT's name, price, transaction fee, and seller's Ethereum address. It also shows the total price in ether and provides a button to send the transaction.

When the "Send Transaction" button is clicked, the send_transaction function is called with three parameters: the buyer's account, the drink_address of the seller, and the total_price of the Cocktail NFT. The function returns a transaction hash, which is displayed on the web interface. If the transaction is successful, a balloon celebration appears on the screen.



