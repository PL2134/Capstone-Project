#imports
import os
import json
import streamlit as st

from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

#define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################


@st.cache_resource
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/arttoken_abi.json')) as f:
        contract_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract


# Load the contract
contract = load_contract()

st.title("Welcome to NFT Bar")
st.write("Choose an account to get started")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")

################################################################################
# Register New Artwork
################################################################################
st.markdown("## Register New Artwork")

artwork_name = st.text_input("Enter the name of the artwork")
artist_name = st.text_input("Enter the artist name")
initial_price = st.text_input("Enter the price (ETH)")
artwork_uri = st.text_input("Enter the URI to the artwork")

if st.button("Register Artwork"):
    token_id = contract.functions.registerArtwork(
        address,
        artwork_name,
        artist_name,
        int(initial_price),
        artwork_uri
    ).call()
    tx_hash = contract.functions.registerArtwork(
        address,
        artwork_name,
        artist_name,
        int(initial_price),
        artwork_uri
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    st.write("TokenId:", token_id) 

    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
    st.balloons()
st.markdown("---")


################################################################################
# Edit the product listing
################################################################################
st.markdown("## Edit the product listing")
tokens = contract.functions.totalSupply().call()
token_id = st.selectbox("Choose an Art Token ID", list(range(tokens)))
new_price = st.text_input("Enter the new price (ETH)")
report_uri = st.text_area("Enter notes about the change")
if st.button("Update price"):

    # Use the token_id and the report_uri to record the appraisal
    tx_hash = contract.functions.editPrice(
        token_id,
        int(new_price),
        report_uri
    ).transact({"from": w3.eth.accounts[0]})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write(receipt["transactionHash"])
st.markdown("---")

################################################################################
# Get Price History
################################################################################
st.markdown("## Get the price history")
art_token_id = st.number_input("Artwork ID", value=0, step=1)
if st.button("Get Price Reports Details"):
    appraisal_filter = contract.events.Appraisal.createFilter(
        fromBlock=0,
        argument_filters={"tokenId": art_token_id}
    )
    appraisals = appraisal_filter.get_all_entries()
    if appraisals:
        for appraisal in appraisals:
            report_dictionary = dict(appraisal)
            #st.markdown("### Price Report Event Log")
            #st.write(report_dictionary)
            # st.markdown("### Price Report Details")
            st.write(report_dictionary["args"])
    else:
        st.write("This artwork has no changes to price.")

