import requests, asyncio, websockets 


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


class btc_listener:

    def __init__(self, is_running):
        self.ws_url = 'wss://ws-feed.exchange.coinbase.com'
        self.is_running = is_running
        self.running(self)

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

    async def listener(self):
        async with websockets.connection(self.ws_url) as websocket:
            message = self.create_subscription_message()
            websocket.send(message)
            response = websocket.recv
            yield response
        
    async def running(self):
        while self.is_running == True:
            async for message in self.listener():
                yield message 
        