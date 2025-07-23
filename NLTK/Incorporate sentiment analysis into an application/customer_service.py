from nltk.sentiment import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')
# nltk.download('subjective')
# nltk.download('movie_reviews')

# from import_nltk import download1
# download1()



sia = SentimentIntensityAnalyzer()

while True:
    new_message = input('Message: ')
    scores = sia.polarity_scores(new_message)
    compound = scores['compound']
    if compound > 0.1:
        print('positive comment')
    elif compound < -0.1:
        print('negitive comment')
    else:
        print('neutral comment')

