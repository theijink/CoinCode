from binance.client import Client

class Account(Client):
    def __init__(self, api_key, api_secret, requests_params=None, tld='com', testnet=False):
        super().__init__(api_key, api_secret, requests_params, tld, testnet)
        self.all_markets=[m['symbol'] for m in self.get_ticker()]
        ## declare empty collections
        self.markets=set()
        self.raw_data={}
        ## declare empty parameters
        self.symbol=''
        self.interval=''
        self.start=''

    def get_markets(self, base):
        tix=self.get_ticker()
        symbols=[]
        for s in [m['symbol'] for m in tix]:
           if s[:len(base)]==base or s[-len(base):]==base:
               symbols.append(s)
        return symbols
    
    def set_markets(self, markets):
        ## fix datatype in case of a single input
        if not type(markets)==type([]):
            if type(markets)==type('') or type(markets)==type(0):
                markets=[markets]
            else:
                pass
        else:
            pass
        ## add to markets in case valid
        for s in markets:
            if s in self.all_markets:
                self.markets.add(s)
            else:
                pass

    def remove_markets(self, markets):
        ## fix datatype in case of a single input
        if not type(markets)==type([]):
            if type(markets)==type('') or type(markets)==type(0):
                markets=[markets]
            else:
                pass
        else:
            pass
        ## add to markets in case valid
        for s in markets:
            if s in self.all_markets:
                self.markets.remove(s)
            else:
                pass

    def get_raw_data(self):
        '''[otime, open, high, low, close, volume, ctime, QuoteAssetVolume, nofTrades, TakerBuyBaseAssetVolume, TakerBuyQuoteAssetVolume, Ignore]'''        
        ## first check if given symbol 
        if self.symbol in self.markets:
            self.raw_data[self.symbol]=[[r[0], r[1], r[2], r[3], r[4], r[5]] for r in self.get_historical_klines(self.symbol, self.interval, self.start)]
                

        


    