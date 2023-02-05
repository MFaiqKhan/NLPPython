import spacy

nlp = spacy.load('en_core_web_sm') # Load the small English model

# why spacy is object oriented
# because we create a Doc object and then use different methods on it which are defined in the Doc class

# Create a Doc object

doc = nlp("Tea is healthy and calming, don't you think?. Said by Mr. John the Doctor")

print(doc.text)

print ("-------------------Sentence tokenization------------------")

# sentence segmentation/tokenizations, seperating sentences
# spacy uses a statistical model to predict where the sentences end and begin
# and also it is trained on a lot of data
# uses a set of rules to predict where the sentences end and begin and heuristic rules 
# like if the next word is capitalized then it is a new sentence etc.
# use CRF model to predict where the sentences end and begin

for sentence in doc.sents:
    print(sentence)

# word tokenization

print ("-------------------Word tokenization------------------")

for sentence in doc.sents:
    for token in sentence:
        print(token.text)

