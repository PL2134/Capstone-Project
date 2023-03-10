# Cocktail NFT Buyer Interface

################################################################################

# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

################################################################################

# From `crypto_wallet.py import the functions generate_account, get_balance,
#  and send_transaction
from crypto_wallet import generate_account, get_balance, send_transaction

################################################################################

# Cocktail NFTs Information

# Database of cocktail NFTs including name of NFT, digital address, token ID and price.
item_database = {
    "Cosmopolitan": [
        "Cosmopolitan",
        "0xcab67550CeCAa7cd34D81C29B832E0fbC2a89E01",
        "3",
        8,
        "Images/cosmopolitan.jpg",
    ],
    "Margarita": [
        "Margarita",
        "0x2157032A1dA319f967FaAf2dABa07E379CAF2Fdb",
        "4",
        2,
        "Images/margarita.jpg",
    ],
    "Manhattan": [
        "Manhattan",
        "0x05F98e8b028380266455aCee5C0183746B449ad3",
        "5",
        6,
        "Images/manhattan.jpg",
    ],
    "Martini": [
        "Martini",
        "0x306F8095896bc7D0ef79605FEe6416637ee73B01",
        "6",
        3,
        "Images/martini.jpg",
    ],
}

# A list of the cocktail NFTs
cocktails = ["Cosmopolitan", "Margarita", "Manhattan", "Martini"]


def get_drinks():
    """Display the database of cocktail NFTs information."""
    db_list = list(item_database.values())

    for number in range(len(cocktails)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Seller Address: ", db_list[number][1])
        st.write("Token ID: ", db_list[number][2])
        st.write("Price: ", db_list[number][3], "eth")
        st.text(" \n")


################################################################################

# Streamlit Code

# Streamlit application headings
st.markdown("# NFT BAR")
st.markdown("## Have a Elegant Cocktail NFT!")
st.text(" \n")

################################################################################

# Streamlit Sidebar Code - Start
st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################

#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

##########################################

# Write the NFT buyer's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################

# Call `get_balance` function and pass it the buyer's account address
# Write the returned ether balance to the sidebar
ether = get_balance(w3, account.address)
st.sidebar.write("## Your Balance of Ether")
st.sidebar.write(ether)
st.sidebar.write("---------")

##########################################

# Create a select box to chose a cocktail NFT
cocktail = st.sidebar.selectbox("Select a Cocktail", cocktails)

# Create a title on the sidebar
st.sidebar.markdown("## Cocktail Name, Price, Transaction Fee and Ethereum Address")

# Identify the cocktail NFT
drink = item_database[cocktail][0]

# Write the cocktail NFT's name to the sidebar
st.sidebar.write(drink)

# Identify the cocktail NFT's price
price = item_database[cocktail][3]

# Write the cocktail NFT's price to the sidebar
st.sidebar.write(price)

# Calculate transaction fee for the transaction
fee = price * 0.025

# Write the transaction fee to the sidebar
st.sidebar.write(fee)

# Identify the cocktail NFT seller's Ethereum Address
drink_address = item_database[cocktail][1]

# Write the cocktail NFT seller's name to the sidebar
st.sidebar.write(drink_address)

# Create a title on the sidebar
st.sidebar.markdown("## Total Price in Ether")

################################################################################

# Calculate `total price` for the NFT transaction by adding the transaction fee 
# to the price of the NFT
total_price = price + fee

# Write the `total price` calculation to the Streamlit sidebar
st.sidebar.write(total_price)

##########################################

# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application???s
# web interface.

if st.sidebar.button("Send Transaction"):

    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `drink_address`, and the `total_price` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    transaction_hash = send_transaction(w3, account, drink_address, total_price)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes cocktail NFT to the Streamlit page
get_drinks()