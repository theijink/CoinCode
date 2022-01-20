from binance.client import Client

class client(Client):
    def __init__(self, pkey, skey, requests_params=None, tld='com', testnet=False):
        super().__init__(api_key, api_secret, requests_params, tld, testnet)

    def get_markets(self, base):
        tix=self.get_ticker()
        symbols=[]
        for s in [m['symbol'] for m in tix]:
           if s[:len(base)]==base or s[-len(base):]==base:
               symbols.append(s)
        return symbols

    def get_data(self, symbol, interval, start):
        '''[otime, open, high, low, close, volume, ctime, QuoteAssetVolume, nofTrades, TakerBuyBaseAssetVolume, TakerBuyQuoteAssetVolume, Ignore]'''
        return [[r[0], r[1], r[2], r[3], r[4], r[5]] for r in self.get_historical_klines(symbol, interval, start)]
    
