from TwitterAPI import *


OAUTH_TOKEN = '913876524-iqDHk8QIq3AL6LRi34R4JGNGXekXG7yTubcp2lyK'
OAUTH_SECRET = '8lXzL0JhwNsRktp51Ny6QN8kAtbckTXH0C0r9Uo0m0h1m'
CONSUMER_KEY = '3NC3fjWZrRvTrppNrOrfIQ'
CONSUMER_SECRET = 'XZRqEAUHWCjiNbd4Ve2Kk1WWVXvjDPqmq986DHP110'




api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_SECRET)

r = api.request('statuses/filter', {'locations' : '-74,40,-73,41'})
Num = 10
results = []
for item in r.get_iterator():
	Size = len(results)
	if Size == Num:
		break
	results.append(item)
#print results

description = []
# u'description'
for i in range(0, len(results)):
	info = results[i]
	#print info
	content = info[u'user'][u'description']
	description.append(content)

print description



