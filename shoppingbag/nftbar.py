#print("Script is being executed")

#imports
import os
import json
import pandas as pd
import streamlit as st

from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv

from crypto_wallet import generate_account, get_balance, send_transaction

load_dotenv()

#define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

st.title("Welcome to NFT Bar")

#########################################################################################
# Product Listing - Cocktails
# Database of cocktails art including token ID, artwork name, artist, price in Ether 
# and seller address
#########################################################################################

col1, col2, col3 = st.columns(3)

drink_db = {
    "0": [
            "0", 
            "Manhattan",
            "N. Barclay", 
            20,
            "0xc9b0A36b22DDBaCddfb366b5327D9F2238EfA446",
            "images/cocktail_manhattan.jpg"],
    "1": [
            "1", 
            "Martini", 
            "N. Barclay", 
             20,
             "0xd2671FBaDead020604660d0f707DC625EfAFb199",
             "images/cocktail_martini.jpg"],
    "2": [
            "2", 
            "Negroni", 
            "N. Barclay", 
            20,
            "0x052f5033855d44fcF74b16492839428Ed667848f",
            "images/cocktail_negroni.jpg"],
    "3": [
            "3", 
            "Bellini", 
            "N. Barclay", 
            20,
            "0x297845b491b0503a7f4638Fcbc1946dA5f758B11",
            "images/cocktail_bellini.jpg"],
    "4": [
            "4", 
            "Cappucino",
            "N. Barclay", 
            20,
            "0xc9b0A36b22DDBaCddfb366b5327D9F2238EfA446",
            "images/coffee_cap.jpg"],
    "5": [
            "5", 
            "Flatwhite", 
            "N. Barclay", 
             20,
             "0xd2671FBaDead020604660d0f707DC625EfAFb199",
             "images/coffee_flatwhite.jpg"],
    "6": [
            "6", 
            "Latte", 
            "N. Barclay", 
            20,
            "0x052f5033855d44fcF74b16492839428Ed667848f",
            "images/coffee_latte.jpg"],
    "7": [
            "7", 
            "Mocha", 
            "N. Barclay", 
            20,
            "0x297845b491b0503a7f4638Fcbc1946dA5f758B11",
            "images/cocktail_mocha.jpg"],
    "8": [
            "8", 
            "Black Tea",
            "N. Barclay", 
            20,
            "0xc9b0A36b22DDBaCddfb366b5327D9F2238EfA446",
            "images/tea_black.jpg"],
    "9": [
            "9", 
            "Green Tea", 
            "N. Barclay", 
             20,
             "0xd2671FBaDead020604660d0f707DC625EfAFb199",
             "images/tea_green.jpg"],
    "10": [
            "10", 
            "Oolong Tea", 
            "N. Barclay", 
            20,
            "0x052f5033855d44fcF74b16492839428Ed667848f",
            "images/tea_oolong.jpg"],
    "11": [
            "11", 
            "Pu-Erh Tea", 
            "N. Barclay", 
            20,
            "0x297845b491b0503a7f4638Fcbc1946dA5f758B11",
            "images/tea_puerh.jpg"]

}

#initialise an empty list to store selected artwork as user clicked on add to cart
if "selected_artwork" not in st.session_state:
        st.session_state.selected_artwork = []

# Create a get_drink function to display the listing
def get_drink():
        
    """Display the database of artwork information."""
    db_list = list(drink_db.values())
    
    with col1:
        st.header("Cocktail")
        for number in range(0,3):
            st.image(db_list[number][5], width=200)
            tokenID = st.write("TokenID:", db_list[number][0])
            artwork_name = st.write("Name: ", db_list[number][1])
            artist_name = st.write("Artist: ", db_list[number][2])
            artwork_price = st.write("Price: ", db_list[number][3],"eth")
            address = st.write("Seller address: ", db_list[number][4])
            if st.button("Add To Cart", key = number):
               st.session_state.selected_artwork.append([db_list[number][1],db_list[number][3],db_list[number][4]])

    with col2:
        st.header("Coffee")
        for number in range(4,7):
            st.image(db_list[number][5], width=200)
            tokenID = st.write("TokenID:", db_list[number][0])
            artwork_name = st.write("Name: ", db_list[number][1])
            artist_name = st.write("Artist: ", db_list[number][2])
            artwork_price = st.write("Price: ", db_list[number][3],"eth")
            address = st.write("Seller address: ", db_list[number][4])
            if st.button("Add To Cart", key = number):
               st.session_state.selected_artwork.append([db_list[number][1],db_list[number][3],db_list[number][4]])

    with col3:
        st.header("Tea")
        for number in range(8,11):
            st.image(db_list[number][5], width=200)
            tokenID = st.write("TokenID:", db_list[number][0])
            artwork_name = st.write("Name: ", db_list[number][1])
            artist_name = st.write("Artist: ", db_list[number][2])
            artwork_price = st.write("Price: ", db_list[number][3],"eth")
            address = st.write("Seller address: ", db_list[number][4])
            if st.button("Add To Cart", key = number):
                st.session_state.selected_artwork.append([db_list[number][1],db_list[number][3],db_list[number][4]])


get_drink()


#########################################################################################
# Streamlit Sidebar Code - Start
#########################################################################################
st.sidebar.markdown("## Your Account Address and Ethernet Balance in Ether")

#  Call the `generate_account` function and save it as the variable `account`
#write the user's ethereum account address to the sidebar
account = generate_account()
st.sidebar.write(account.address)

# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
ether = get_balance(w3, account.address)
st.sidebar.markdown("Your Balance of Ether")
st.sidebar.write(ether)

st.sidebar.markdown("---------")

st.sidebar.header("**My Shopping Cart:**") 

selected_df = pd.DataFrame(st.session_state.selected_artwork, 
                           columns = ["Name","Price","Seller_Address"])

totalpayable = selected_df["Price"].sum()
sellertotal_df = selected_df.groupby("Seller_Address")["Price"].sum()

st.sidebar.dataframe(selected_df, use_container_width=True)

if st.sidebar.button("Clear cart"):
    st.session_state.selected_artwork = []

st.sidebar.markdown(f"## Total Payable in Ether: {totalpayable}")
st.sidebar.markdown(f"### Amount payable grouped by seller:")
st.sidebar.dataframe(sellertotal_df , use_container_width = True)

if st.sidebar.button("Checkout"):
   # transaction_hash = send_transaction(w3, account, seller_address, totalpayable)

    st.sidebar.markdown("#### Validated TransactionHash")
    # st.sidebar.write(transaction_hash)

    st.snow()

    st.session_state.selected_artwork=[]


