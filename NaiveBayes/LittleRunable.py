from DBBuilder import DBBuilder
from rawclassifier import RawClassifier
Builder = DBBuilder()
data = 'Poseys grand slam and solid defense almost single-handedly won Game 5. http://t.co/POFAfuPW #Giants'

TweetClassifier = RawClassifier()
result = TweetClassifier.SFHandler(data)

print result
