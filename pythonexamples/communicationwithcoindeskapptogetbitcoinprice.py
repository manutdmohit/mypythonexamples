import requests
response=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
binfo=response.json()
#print(type(binfo))
#print(binfo)
print('Bitcoin price on ',binfo['time']['updated'])
print('1 BitCoin=$',binfo['bpi']['USD']['rate'])
