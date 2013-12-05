# accountLookp.py

import os

from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import RequestHandler


class getquotefromtwitter(RequestHandler):
	def get(self):		
#		news_rss_url = 'http://search.twitter.com/search.atom?q=perkytweets'
#		import feedparser


#		from twitter import *
#		from httplib2 import *
		import TwitterRequestHandler
		OAUTH_TOKEN = '913876524-iqDHk8QIq3AL6LRi34R4JGNGXekXG7yTubcp2lyK'
		OAUTH_SECRET = '8lXzL0JhwNsRktp51Ny6QN8kAtbckTXH0C0r9Uo0m0h1m'
		CONSUMER_KEY = '3NC3fjWZrRvTrppNrOrfIQ'
		CONSUMER_SECRET = 'XZRqEAUHWCjiNbd4Ve2Kk1WWVXvjDPqmq986DHP110'
		token = (OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
		TRHandler = TwitterRequestHandler.TwitterRequestHandler(token)
		result = TRHandler.MakeRequest()
	#	t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
		
	#	d = t.statuses.home_timeline()

	#	info = feedparser.parse(news_rss_url)
		#info = feedparser.parse(d)

	#	size = len(d)
	#	records = []
	#	for i in range(0, size):
	#		x = d[i]
	#		records.append(x[u'text'])



	#	records = info['entries']
		records = result['personal']
#		records = ['abc', 'edf']
		template_values = {"accounts": records};
		path = os.path.join(os.path.dirname(__file__), "templates/main.html")
		self.response.out.write(template.render(path, template_values))
		
