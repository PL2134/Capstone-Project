#imports
import os
import json
import streamlit as st

from pathlib import Path
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

#define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Load_Contract Function
################################################################################

@st.cache(allow_output_mutation = True)
def load_contract():

    #load the contract ABI
    with open(Path('./contracts/compiled/arttoken_abi.json')) as f:
        contract_abi = json.load(f)

    #set the contract address(i.e. deployed contract address)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    #get the contract
    contract = w3.eth.contract(
        address = contract_address,
        abi = contract_abi
    )
    return contract