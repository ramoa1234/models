import asyncio

from coinbase import btc_listener
from coinbase import coinbase_api


"""
CREATE API FUNCTION TO GET PRICE RANGES BEFORE MAKING THE MODEL
AND ADD GIT IGNORE ON DATA 
"""

def main():
    test = btc_listener()
asyncio.run(main)



#set periods create models(mean reversion(in a moving average(convolution(each layer in somethign like a nn)))) from them and test
class mean_reversion_model:
    def __init__():
        pass