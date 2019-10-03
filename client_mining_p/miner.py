import hashlib
import requests

import sys

# TODO: Implement functionality to search for a proof 
def proof_of_work(block_string):
        proof = 0
        while valid_proof(block_string, proof) is False:
            proof +=1
        return proof

def valid_proof(block_string, proof):
        # TODO
        guess = f'{block_string}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:3] == "000"

if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # TODO: Get the last proof from the server
        URL = "localhost:5000/last_block"
        r = requests.get(url = URL)
        data = r.json()
        # Look for new proof
        last_proof = data['proof']
        new_proof = proof_of_work(last_proof)

        # TODO: When found, POST it to the server {"proof": new_proof}
        # TODO: We're going to have to research how to do a POST in Python
        # HINT: Research `requests` and remember we're sending our data as JSON
        URL_MINE = "localhost:5000/mine"
        r2 = requests.get(url=URL_MINE, json={new_proof})
        data_mine = r2.json()
        # TODO: If the server responds with 'New Block Forged'
        if data_mine['message'] == 'New Block Forged':
            coins_mined += 1
        print(data_mine['message'])
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
