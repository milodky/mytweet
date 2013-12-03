from TwitterAPI import *
from TwitterRequestHandler import *

def GetToken():
	a = '913876524-iqDHk8QIq3AL6LRi34R4JGNGXekXG7yTubcp2lyK'
	b = '8lXzL0JhwNsRktp51Ny6QN8kAtbckTXH0C0r9Uo0m0h1m'
	c = '3NC3fjWZrRvTrppNrOrfIQ'
	d = 'XZRqEAUHWCjiNbd4Ve2Kk1WWVXvjDPqmq986DHP110'
	Ret = (a, b, c, d)
	return Ret


if __name__ == "__main__":
	OAUTH_TOKEN = '913876524-iqDHk8QIq3AL6LRi34R4JGNGXekXG7yTubcp2lyK'
	OAUTH_SECRET = '8lXzL0JhwNsRktp51Ny6QN8kAtbckTXH0C0r9Uo0m0h1m'
	CONSUMER_KEY = '3NC3fjWZrRvTrppNrOrfIQ'
	CONSUMER_SECRET = 'XZRqEAUHWCjiNbd4Ve2Kk1WWVXvjDPqmq986DHP110'
	Tokens = GetToken()
	ReqHandler = TwitterRequestHandler(Tokens);
	#ReqHandler = TwitterRequestHandler(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET);

	description = ReqHandler.MakeRequest()

	print description


#	api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_SECRET)
#	
#	r = api.request('statuses/filter', {'locations' : '-74,40,-73,41'})
#	Num = 10
#	results = []
#	for item in r.get_iterator():
#		Size = len(results)
#		if Size == Num:
#			break
#		results.append(item)
#	
#	description = []
#	for i in range(0, len(results)):
#		info = results[i]
#		content = info[u'user'][u'description']
#		description.append(content)
#	
#	print description



