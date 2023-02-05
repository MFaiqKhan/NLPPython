import nltk

from nltk.tokenize import word_tokenize, sent_tokenize

# nltk.download('punkt') # punkt is a pre-trained model, you can actually train your own model or download different models

text = "Tea is healthy and calming, don't you think?. Said by Mr. John the Doctor"

print(sent_tokenize(text))

print(word_tokenize(text))
