from CoinCode.key import pkey, skey
from CoinCode.CoinCode import client

if __name__=="main":
    cli = client(pkey, skey)
    markets = cli.get_markets('EUR')
    [print(m) for m in markets]
