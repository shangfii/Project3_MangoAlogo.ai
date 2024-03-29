
# Block chain business orderbook

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib

################################################################################

# Record Data Class 

@dataclass
class Record:
    strategy_details: str
    payments_address: str
    phone_number: float
    email: str

################################################################################

# Store Record Data

@dataclass
class Block:

   record: Record
   creator_id: int
   prev_hash: str = 0
   timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
   nonce: str = 0

   def hash_block(self):
        sha = hashlib.sha256()

        record = str(self.record).encode()
        sha.update(record)

        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        return sha.hexdigest()


@dataclass
class NewOrder:
    chain: List[Block]
    difficulty: int = 4

    def proof_of_work(self, block):

        calculated_hash = block.hash_block()

        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):

            block.nonce += 1

            calculated_hash = block.hash_block()

        print("Wining Hash", calculated_hash)
        return block

    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

    def is_valid(self):
        block_hash = self.chain[0].hash_block()

        for block in self.chain[1:]:
            if block_hash != block.prev_hash:
                print("Blockchain is invalid!")
                return False

            block_hash = block.hash_block()

        print("Blockchain is Valid !")
        return True

################################################################################
# Streamlit Code

# Adds the cache decorator for Streamlit


@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return NewOrder([Block("Genesis", 0)])


st.markdown("# AlgoMango.Ai")
st.markdown("## Place your order here")

orderbook = setup()

################################################################################
# Step 3: Collecting new data


strategy_details  = st.text_input("# 1. Fill your strategy details in the space below")


sender = st.text_input(" 2. Your first and last name")


payments_address = st.text_input("3. Ethereum Wallet Address from where you will pay us (Ethereum Only)")


phone_number = st.text_input("4. Your phone number ")
email = st.text_input("5. Your email Address ")


if st.button("Click to place your order"):
    prev_block = orderbook.chain[-1]
    prev_block_hash = prev_block.hash_block()

 # Updating the new_block

    new_block = Block(

        record=strategy_details,
        creator_id=42,
        prev_hash=prev_block_hash
    )

    orderbook.add_block(new_block)
    st.balloons()

################################################################################
# Streamlit Code (continues)

st.markdown("## Order Book")

Orders_df = pd.DataFrame(orderbook.chain)
st.write(Orders_df)

#difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 2)
#orderbook.difficulty = difficulty

#st.sidebar.write("# Block Inspector")
#selected_block = st.sidebar.selectbox(
  #  "Which block would you like to see?", orderbook.chain
#)

#st.sidebar.write(selected_block)

if st.button("Validate Your Order!"):
    st.write(orderbook.is_valid())

################################################################################

# Test 