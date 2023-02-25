# Buyer Interface

################################################################################
# For this Challenge, you will assume the perspective of a KryptoJobs2Go
# customer in order to do the following:

# * Generate a new Ethereum account instance by using your mnemonic seed phrase
# (which you created earlier in the module).

# * Fetch and display the account balance associated with your Ethereum account
# address.

# * Calculate the total value of an Ethereum transaction, including the gas
# estimate, that pays a KryptoJobs2Go candidate for their work.

# * Digitally sign a transaction that pays a KryptoJobs2Go candidate, and send
# this transaction to the Ganache blockchain.

# * Review the transaction hash code associated with the validated blockchain transaction.

# Once you receive the transaction’s hash code, you will navigate to the Transactions
# section of Ganache to review the blockchain transaction details. To confirm that
# you have successfully created the transaction, you will save screenshots to the
# README.md file of your GitHub repository for this Challenge assignment.

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
################################################################################
# Step 1:
# Import Ethereum Transaction Functions into the KryptoJobs2Go Application

# In this section, you'll import several functions from the `crypto_wallet.py`
# script into the file `krypto_jobs.py`, which contains code for Fintech
# Finder’s customer interface, in order to add wallet operations to the
# application. For this section, you will assume the perspective of a Fintech
# Finder customer (i.e., you’ll provide your Ethereum wallet and account
# information to the application).

# Complete the following steps:

# 1. Review the code contained in the `crypto_wallet.py` script file. Note that
# the Ethereum transaction functions that you have built throughout this
# module-including `wallet`, `wallet.derive_acount`, `get_balance`, `fromWei`,
# `estimateGas`, `sendRawTransaction`, and others&mdash;have now been
# incorporated into Python functions that allow you to automate the process of
# accessing them.

# 2. Add your mnemonic seed phrase (provided by Ganache) to the starter code’s `SAMPLE.env` file.
# When the information has been added, rename the file `.env`.

# 3. Import the following functions from the `crypto_wallet.py` file:
# * `generate_account`
# * `get_balance`
# * `send_transaction`

# 4. Within the Streamlit sidebar section of code, create a variable named
# `account`. Set this variable equal to a call on the `generate_account`
# function. This function will create the KryptoJobs2Go customer’s (in this
# case, your) HD wallet and Ethereum account.

# 5. Within this same section of the `krypto_jobs.py` file, define a
# new `st.sidebar.write` function that will display the balance of the
# customer’s account. Inside this function, call the `get_balance` function
# and pass it your Ethereum `account.address`.


################################################################################
# Step 1 - Part 3:
# Import the following functions from the `crypto_wallet.py` file:
# * `generate_account`
# * `get_balance`
# * `send_transaction`

# @TODO:
# From `crypto_wallet.py import the functions generate_account, get_balance,
#  and send_transaction
from crypto_wallet import generate_account, get_balance, send_transaction

################################################################################
# KryptoJobs2Go Candidate Information

# Database of KryptoJobs2Go candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
item_database = {
    "Manhattan": [
        "Manhattan",
        "0x8e5F1c3b8067F8137ABEa0e0f78597D29BAdBd75",
        "token_address_manhattan",
        0.20,
        "Images/manhattan.jpg",
    ],
    "Martini": [
        "Martini",
        "0xd2671FBaDead020604660d0f707DC625EfAFb199",
        "token_address_martini",
        0.33,
        "Images/martini.jpg",
    ],
    "Negroni": [
        "Negroni",
        "0x052f5033855d44fcF74b16492839428Ed667848f",
        "token_address_negroni",
        0.19,
        "Images/negroni.jpg",
    ],
    "Bellini": [
        "Bellini",
        "0x297845b491b0503a7f4638Fcbc1946dA5f758B11",
        "token_address_bellini",
        0.16,
        "Images/bellini.jpg",
    ],
}

# A list of the KryptoJobs2Go candidates first names
cocktails = ["Manhattan", "Martini", "Negroni", "Bellini"]


def get_people():
    """Display the database of KryptoJobs2Go candidate information."""
    db_list = list(item_database.values())

    for number in range(len(cocktails)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Seller Address: ", db_list[number][1])
        st.write("Cocktail Address: ", db_list[number][2])
        st.write("Price: ", db_list[number][3], "eth")
        st.text(" \n")


################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Cocktails2Go!")
st.markdown("## Have a Cocktail NFT!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################
# Step 1 - Part 4:
# Create a variable named `account`. Set this variable equal to a call on the
# `generate_account` function. This function will create the KryptoJobs2Go
# customer’s (in this case, your) HD wallet and Ethereum account.

# @TODO:
#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################
# Step 1 - Part 5:
# Define a new `st.sidebar.write` function that will display the balance of the
# customer’s account. Inside this function, call the `get_balance` function and
#  pass it your Ethereum `account.address`.

# @TODO
# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
ether = get_balance(w3, account.address)
st.sidebar.write("## Your Balance of Ether")
st.sidebar.write(ether)
st.sidebar.write("---------")

##########################################

# Create a select box to chose a FinTech Hire candidate
cocktail = st.sidebar.selectbox("Select a Cocktail", cocktails)

# Create a input field to record the number of hours the candidate worked
number = st.sidebar.number_input("Number of Drinks")

st.sidebar.markdown("## Cocktail Name, Price, and Ethereum Address")

# Identify the FinTech Hire candidate
drink = item_database[cocktail][0]

# Write the KryptoJobs2Go candidate's name to the sidebar
st.sidebar.write(drink)

# Identify the KryptoJobs2Go candidate's hourly rate
price = item_database[cocktail][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(price)

# Identify the KryptoJobs2Go candidate's Ethereum Address
drink_address = item_database[cocktail][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(drink_address)

# Write the KryptoJobs2Go candidate's name to the sidebar

st.sidebar.markdown("## Total Price in Ether")

################################################################################
# Step 2: Sign and Execute a Payment Transaction

# Complete the following steps:

# 1. KryptoJobs2Go customers will select a fintech professional from the
# application interface’s drop-down menu, and then input the amount of time for
# which they’ll hire the worker. Code the application so that once a customer
# completes these steps, the application will calculate the amount that the
# worker will be paid in ether. To do so, complete the following steps:

# * Write the equation that calculates the candidate’s wage. This equation
#  should assess the candidate’s hourly rate from the candidate database
# (`candidate_database[person][3]`) and then multiply this hourly rate by
# the value of the `hours` variable. Save this calculation’s output as a
# variable named `wage`.

# * Write the `wage` variable to the Streamlit sidebar by
# using `st.sidebar.write`.

# 2. Now that the application can calculate a candidate’s wage, write the code
# that will allow a customer (you, in this case) to send an Ethereum blockchain
# transaction that pays the hired candidate. To accomplish this, locate the
# code that reads `if st.sidebar.button("Send Transaction")`. You’ll need to
# add logic to this `if` statement that sends the appropriate information to
# the `send_transaction` function (which you imported from the `crypto_wallet`
# script file). Inside the `if` statement, add the following functionality:

# * Call the `send_transaction()` function and pass it three parameters:
# - Your Ethereum `account` information. (Remember that this `account`
# instance was created when the `generate_account` function was called.)
#  From the `account` instance, the application will be able to access the
#  `account.address` information that is needed to populate the `from` data
# attribute in the raw transaction.
# - The `candidate_address` (which will be created and identified in the
# sidebar when a customer selects a candidate). This will populate the `to`
# data attribute in the raw transaction.
# - The `wage` value. This will be passed to the `toWei` function to
# determine the wei value of the payment in the raw transaction.

# * Save the transaction hash that the `send_transaction` function returns
# as a variable named `transaction_hash`, and have it display on the
# application’s web interface.

##########################################
# Step 2 - Part 1:
# * Write the equation that calculates the candidate’s wage. This equation
# should assess the candidate’s hourly rate from the candidate database
# (`candidate_database[person][3]`) and then multiply this hourly rate by
# the value of the `hours` variable. Save this calculation’s output as a
# variable named `wage`.
# * Write the `wage` variable to the Streamlit sidebar by using `st.sidebar.write`.

# @TODO
# Calculate total `wage` for the candidate by multiplying the candidate’s hourly
# rate from the candidate database (`candidate_database[person][3]`) by the
# value of the `hours` variable
total_price = price * number

# @TODO
# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(total_price)

##########################################
# Step 2 - Part 2:
# * Call the `send_transaction` function and pass it three parameters:
# - Your Ethereum `account` information. (Remember that this `account`
# instance was created when the `generate_account` function was called.)
#  From the `account` instance, the application will be able to access the
#  `account.address` information that is needed to populate the `from` data
# attribute in the raw transaction.
# - The `candidate_address` (which will be created and identified in the
# sidebar when a customer selects a candidate). This will populate the `to`
# data attribute in the raw transaction.
# - The `wage` value. This will be passed to the `toWei` function to
# determine the wei value of the payment in the raw transaction.

# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface.


if st.sidebar.button("Send Transaction"):

    # @TODO
    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `candidate_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    transaction_hash = send_transaction(w3, account, drink_address, total_price)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes KryptoJobs2Go candidates to the Streamlit page
get_people()

################################################################################
# Step 3: Inspect the Transaction

# Send a test transaction by using the application’s web interface, and then
# look up the resulting transaction hash in Ganache.

# Complete the following steps:

# 1. From your terminal, navigate to the project folder that contains
# your `.env` file and the `krypto_jobs.py` and `crypto_wallet.py` files.
# Be sure to activate your Conda `dev` environment if it is not already active.

# 2. To launch the Streamlit application,
# type `streamlit run krypto_jobs.py`.

# 3. On the resulting webpage, select a candidate that you would like to hire
# from the appropriate drop-down menu. Then, enter the number of hours that you
# would like to hire them for. (Remember, you do not have a lot of ether in
# your account, so you cannot hire them for long!)

# 4 Click the Send Transaction button to sign and send the transaction with
# your Ethereum account information. If the transaction is successfully
# communicated to Ganache, validated, and added to a block,
# a resulting transaction hash code will be written to the Streamlit
# application sidebar.

# 5. Navigate to the Ganache accounts tab and locate your account (index 0).
# * Take a screenshot of the address, balance, and transaction (TX) count.
# Save this screenshot to the README.md file of your GitHub repository for
#  this Challenge assignment.

# 6. Navigate to the Ganache transactions tab and locate the transaction.
# * Click the transaction and take a screenshot of it.
# Save this screenshot to the README.md file of your GitHub repository for
#  this Challenge assignment.
