import sys

from learn import Learn
finance_path = 'financetweets.txt'
finance_count = '1000'
finance_cate = 'finance'
finance_args = ['bayes.py', 'learn', finance_cate, finance_path, finance_count]

finance_mode = Learn()

finance_mode.validate(finance_args)
finance_mode.execute()
sports_path = 'sportstweets.txt'
sports_count = '1000'
sports_cate = 'sports'
sports_args = ['bayes.py', 'learn', sports_cate, sports_path, sports_count]
#['bayes.py', 'learn', 'sports', 'sportstweets.txt', '1000']
sports_mode = Learn()
sports_mode.validate(sports_args)
sports_mode.execute()
