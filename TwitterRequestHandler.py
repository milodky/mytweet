from TwitterAPI import *
from unicodedata import normalize

class TwitterRequestHandler:
	def __init__(self, Tokens):
		self.OToken = Tokens[0]
		self.OSecret = Tokens[1]
		self.CKey = Tokens[2]
		self.CSecret = Tokens[3]
	def MakeRequest(self):
		api = TwitterAPI(self.CKey, self.CSecret, self.OToken, self.OSecret)
		# this must be switched later to user's timeline
		r = api.request('statuses/filter', {'locations' : '-74,40,-73,41'})
		# in the end user should set the number of tweets they wanna read
		Num = 10
		results = []
		# this method is too slow, can we get #Num tweets at the same time?
		for item in r.get_iterator():
			Size = len(results)
			if Size == Num:
				break
			results.append(item)
		
		contents = []
		for i in range(0, len(results)):
			info = results[i]
			content = info[u'user'][u'description']
			if content == None:
				continue
			asc2_content = content.encode('ascii','ignore')
			contents.append(asc2_content)
		return contents


if __name__ == "__main__":
	OAUTH_TOKEN = '913876524-iqDHk8QIq3AL6LRi34R4JGNGXekXG7yTubcp2lyK'
	OAUTH_SECRET = '8lXzL0JhwNsRktp51Ny6QN8kAtbckTXH0C0r9Uo0m0h1m'
	CONSUMER_KEY = '3NC3fjWZrRvTrppNrOrfIQ'
	CONSUMER_SECRET = 'XZRqEAUHWCjiNbd4Ve2Kk1WWVXvjDPqmq986DHP110'
	tokens = (OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
	ReqHandler = TwitterRequestHandler(tokens);

	description = ReqHandler.MakeRequest()
	print description
