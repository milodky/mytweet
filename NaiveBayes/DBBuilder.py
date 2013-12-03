from learn import Learn
"""
this package builds the database needed for the twitter classifier
"""
class CateBuilder:
	def __init__(self, args):	
		self.mode = Learn()
		self.mode.validate(args)
		self.mode.execute()
class DBBuilder:
	def __init__(self):
		finance_path = 'financetweets.txt'
		finance_count = '1000'
		finance_cate = 'finance'
		finance_args = ['bayes.py', 'learn', finance_cate, finance_path, finance_count]
		sports_path = 'sportstweets.txt'
		sports_count = '1000'
		sports_cate = 'sports'
		sports_args = ['bayes.py', 'learn', sports_cate, sports_path, sports_count]
		self.finance = CateBuilder(finance_args)
		self.sports = CateBuilder(sports_args)

if __name__ == '__main__':
	builder = DBBuilder()
