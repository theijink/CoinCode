from coincode import Manage, Account, Trade

client=Account.login('username', 'password')
print(client)

wallet=Account.wallet(client)
[print(coin) for coin in wallet]
