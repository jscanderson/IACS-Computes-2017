# Import the Twython class from the twython library.
# Assumes you have already installed twython using 'easy_install twython' or similar.
from twython import Twython
#import json # Not necessary because twython does the parsing.
import re # Regular expressions for matching words by pattern.

# Login credentials can be obtained on the web through the Twitter API documentation.
APP_KEY = "R9TTlO9BvQ50ftyYA6IwA"
APP_SECRET = "uAjP8CThyXnbdEqXxsVlgE3tJIvePm2a7PL8cB8N74"
OAUTH_TOKEN = "555507083-njJAAWYiGJpUxeX7tAtuFhxSM2rFUgj9KEKFgFwo"
OAUTH_TOKEN_SECRET = "DIzvCloqs7LoC2Fh5b5H43svJk3F6A6SVmckh1KOhDY"

# Initialize the Twython object.
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Choose a hashtag or other search keyword.
myHashtag = "#DawgPound"

# The search function exposes the search endpoint of the Twitter API.
matchedTweets = twitter.search(q=myHashtag, count=100)

# Look at the results returned.
matchedTweets
type(matchedTweets)
matchedTweets.keys()

# Look at the text of the tweets.
for tweet in matchedTweets["statuses"]:
	print(tweet["text"])

# Create lists of positive and negative words.
posWords = open('positive-words.txt', 'r')
negWords = open('negative-words.txt', 'r')

posWordList = []
for line in posWords:
	#print line,
	nextWord = line.strip()
	if len(nextWord) > 0 and not nextWord.startswith(";"):
		posWordList.append(nextWord)

posWordList

negWordList = []
for line in negWords:
	#print line,
	nextWord = line.strip()
	if len(nextWord) > 0 and not nextWord.startswith(";"):
		negWordList.append(nextWord)

negWordList

# For each tweet, look for each word.
# Keep a running tally of positive and negative words.
totalPos = 0
totalNeg = 0

for tweet in matchedTweets["statuses"]:
	tweetText = tweet["text"]
	tweetText = tweetText.encode('utf-8')
	tweetText = tweetText.strip()
	# Look for any positive words.
	for nextWord in posWordList:
		#print(nextWord)
		searchPattern = re.compile("\\b" + nextWord + "\\b")
		searchMatches = searchPattern.findall(tweetText)
		#if len(searchMatches) > 0:
		#	print tweetText, str(len(searchMatches)), nextWord
		#print(searchMatches)
		totalPos = totalPos + len(searchMatches)
	
	# Look for any negative words.
	for nextWord in negWordList:
		#print(nextWord)
		searchPattern = re.compile("\\b" + nextWord + "\\b")
		searchMatches = searchPattern.findall(tweetText)
		if len(searchMatches) > 0:
			print tweetText, str(len(searchMatches)), nextWord
		#print(searchMatches)
		totalNeg = totalNeg + len(searchMatches)

