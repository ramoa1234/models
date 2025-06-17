import requests, websockets, time


def create_headers():
    return {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }




url = 'api.cdp.coinbase.com'
class coinbase_api:
    def __init__(self):
        pass
    
    def create_payload(amount, from_asset_id, to_asset_id):
        return {
            'amount': amount,
            'from_asset_id': from_asset_id,
            'to_asset_id': to_asset_id
        }

    #amount should be in tokens
    def trade(self, amount, from_wallet_id, to_wallet_id, wallet_id, address_id):
        try:
            headers = create_headers()
            payload = self.create_buy_payload(amount, from_wallet_id, to_wallet_id)
            response = requests.post(f'{url}/platform/v1/wallets/{wallet_id}/addresses/{address_id}/trades', json=payload, headers=headers)
            return response
        except:
            print("Failed trade")
            return None
            
    def trade_object(amount, trade_id, from_asset, to_asset):
        return {
            'amount': amount,
            'trade_id': trade_id,
            'from_asset': from_asset,
            'to_asset': to_asset
        }
        
    def parse_response(self, resposne):
       pass


from util import load_api_key

class btc_listener:
    #NEED TO UPDATE SO THAT WHEN THE FUCNTION IS CALLED THE OBJECT IS RETURNED
    async def __init__(self):
        self.ws_url = 'wss://ws-feed.exchange.coinbase.com'
        self.api_key = load_api_key()
        self.running = True
        while self.running:
            await self.run()
            time.sleep(5)

    def create_subscription_message():
        return {
            "type": "subscribe",
            "product_ids": ["BTC-USD"],
            "channels": [
                "level2",
                "heartbeat",
                {
                "name": "ticker",
                "product_ids": ["BTC-USD"]
                }
            ]
        }
        
    async def run(self):
        async with websockets.connect(self.ws_url) as connection:
            await connection.send(self.create_subscription_message())
            response = await websockets.recv()
            json = json.loads(response)
            print(json)




