"""
Genesis block
{
    index:0,
    timestamp: current time,
    data: "Hello I am Lakshmi",
    proof:3,
    previous_hash: "0"
} -> hash() -> 2343aaa

{
    index:1,
    timestamp: current time,
    data: "Hello this is the first block",
    proof:2343,
    previous_hash: 2343aaa
} -> hash() -> 9876ffe

{
    index:2,
    timestamp: current time,
    data: "Hello this is the second block",
    proof:2312,
    previous_hash: 9876ffe
} -> hash() -> 2367bba

"""

import fastapi as _fastapi
import blockchain as _blockchain

blockchain = _blockchain.Blockchain()
app = _fastapi.FastAPI()


# endpoint to mine a block
@app.post("/mine_block/")
def mine_block(data: str):
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")
    block = blockchain.mine_block(data=data)

    return block


# endpoint to return the blockchain
@app.get("/blockchain/")
def get_blockchain():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")
    chain = blockchain.chain
    return chain


# endpoint to see if the chain is valid
@app.get("/validate/")
def is_blockchain_valid():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")

    return blockchain.is_chain_valid()


# endpoint to return the last block
@app.get("/blockchain/last/")
def previous_block():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")

    return blockchain.get_previous_block()

mine_block("Hello world")
mine_block("This is the third block")
print(get_blockchain())