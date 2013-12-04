#!/usr/bin/env python
from httplib2 import *
import urllib
import base64
import httplib
import urllib2
import json
from StringIO import * 
from gzip import * 

if __name__ == "__main__":

	CONSUMER_KEY = 'nuIALqzz8W5wlyrQZSlcA'
	CONSUMER_SECRET = 'JaSEgDkcWItX47shHDS5XK8Z9IYAqv0wRiYDT9eUzo'
	
	encoded_CONSUMER_KEY = urllib.quote(CONSUMER_KEY)
	encoded_CONSUMER_SECRET = urllib.quote(CONSUMER_SECRET)
	
	concat_consumer_url = encoded_CONSUMER_KEY + ":" + encoded_CONSUMER_SECRET
	
	host = 'api.twitter.com'
	url = '/oauth2/token/'
	params = urllib.urlencode({'grant_type' : 'client_credentials'})
	req = httplib.HTTPSConnection(host)
	req.putrequest("POST", url)
	req.putheader("Host", host)
	req.putheader("User-Agent", "My Twitter 1.1")
	req.putheader("Authorization", "Basic %s" % base64.b64encode(concat_consumer_url))
	req.putheader("Content-Type" ,"application/x-www-form-urlencoded;charset=UTF-8")
	req.putheader("Content-Length", "29")
	req.putheader("Accept-Encoding", "gzip")
	
	req.endheaders()
	req.send(params)
	
	resp = req.getresponse()
	print resp.status, resp.reason
	
	raw_data = resp.read()
	
	stream = StringIO(raw_data)
	
	decompressor = GzipFile(fileobj=stream) 
	cooked_data = json.loads(decompressor.read())
	print cooked_data
	bearer_token = cooked_data["access_token"]
	
	new_host = 'api.twitter.com'
	new_url = '/1.1/search/tweets.json'
	
	new_params = urllib.urlencode({'geocode' : '40.809881,-73.959746,5mi'})
	
	new_req = httplib.HTTPSConnection(new_host)
	
	new_req.putrequest("GET", new_url)
	new_req.putheader("HOST", new_host)
	new_req.putheader("User-Agent", "My Twitter 1.1")
	new_req.putheader("Authorization", "Bearer %s" % bearer_token)
	new_req.putheader("Content-Type" ,"application/x-www-form-urlencoded;charset=UTF-8")
	
	#new_req.putheader("Content-Length", "29")
	new_req.putheader("Accept-Encoding", "gzip")
	new_req.endheaders()
	new_req.send(new_params)
	
	my_resp = new_req.getresponse()
	print my_resp.status, my_resp.reason
	
	
	
	#h.add_credentials('Authorization')
	
	
	
	
	OAUTH_TOKEN = '913876524-iqDHk8QIq3AL6LRi34R4JGNGXekXG7yTubcp2lyK'
	OAUTH_SECRET = '8lXzL0JhwNsRktp51Ny6QN8kAtbckTXH0C0r9Uo0m0h1m'
	CONSUMER_KEY = '3NC3fjWZrRvTrppNrOrfIQ'
	CONSUMER_SECRET = 'XZRqEAUHWCjiNbd4Ve2Kk1WWVXvjDPqmq986DHP110'


