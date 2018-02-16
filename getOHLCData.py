import oandapy
import json
import csv
from datetime import datetime, timedelta

account = ""
access_token = ""
with open('config.json', 'r') as f:
		config = json.load(f)
		
#environment = raw_input("Live or practice: ")
environment = "live"
if (environment == "live"):
	account = config['liveAccount']
	access_token = config['liveToken']
elif (environment == "practice"):
	account = config['practiceAccount']
	access_token = config['practiceToken']

def getData(pair, timeframe, numDataPoints):
	granularity = timeframe
	count = 5000
	oanda = oandapy.API(environment=environment, access_token=access_token)
	end = datetime.utcnow()
	
	#print end
	#history = oanda.get_history(instrument = pair, granularity=granularity, count=count, candleFormat="midpoint", end = end.isoformat('T'))
	#use to get more history sincne max is 5k in one call
	if timeframe == "M1":
		timeDelta = timedelta(minutes=count)
	elif timeframe == "S1":
		timeDelta = timedelta(seconds=count)
	elif timeframe == "H1":
		timeDelta = timedelta(hours=count)
	start = end - timeDelta
	

	


	'''end = end - timeDelta
	print end
	history2 = oanda.get_history(instrument = pair, granularity=granularity, count = count,candleFormat=midpoint, end=end.isoformat('T'))

	end = end - timeDelta
	print end
	history3 = oanda.get_history(instrument = pair, granularity=granularity, count = count,candleFormat=midpoint, end=end.isoformat('T'))

	end = end - timeDelta
	print end
	history4 = oanda.get_history(instrument = pair, granularity=granularity, count = count,candleFormat=midpoint, end=end.isoformat('T'))
'''
	
	while numDataPoints > 0:
		print end
		
		
		history = oanda.get_history(instrument = pair, granularity=granularity, count = count, start = start.isoformat("T"), end = end.isoformat("T"))
		numDataPoints -= count
		if numDataPoints < count:
			count = numDataPoints
			

		







	#print history
	#print history["instrument"]
	#print history["candles"][0]
	#print history["candles"][499]

	#print history["candles"][0]["closeBid"]

	file = open(pair+'_'+granularity+'_'+'OHLCV.csv', "w")
	for candle in history4['candles']:
		file.write(str(candle['time'])+','+str(candle['openMid'])+','+str(candle['highMid'])+','+str(candle['lowMid'])+','+str(candle["closeMid"])+','+str(candle['volume'])+'\n')
	for candle in history3["candles"]:
		file.write(str(candle['time'])+','+str(candle['openMid'])+','+str(candle['highMid'])+','+str(candle['lowMid'])+','+str(candle["closeMid"])+','+str(candle['volume'])+'\n')
	for candle in history2["candles"]:
		file.write(str(candle['time'])+','+str(candle['openMid'])+','+str(candle['highMid'])+','+str(candle['lowMid'])+','+str(candle["closeMid"])+','+str(candle['volume'])+'\n')
	for candle in history["candles"]:
		file.write(str(candle['time'])+','+str(candle['openMid'])+','+str(candle['highMid'])+','+str(candle['lowMid'])+','+str(candle["closeMid"])+','+str(candle['volume'])+'\n')	
		
	#for candle in history["EUR_USD"]["candles"]

	#with open('history.json', 'w') as f:
	#	json.dumps(json.load(history), f)
	#oanda.get_autochartist()

getData("EUR_USD", "H1", 22000)
