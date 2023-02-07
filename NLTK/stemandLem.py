import nltk

from nltk.stem import PorterStemmer # nltk.stem is a module, PorterStemmer is a class in that module 
# PorterStemmer is a class that has a method called stem() which takes a word as input and returns the stem of that word
# stem() is a method that takes a word as input and returns the stem of that word

stemmer = PorterStemmer() # create an object of the PorterStemmer class and assign it to the stemmer variable

print(stemmer.stem("working")) # print the stem of the word working

words = ["give", "giving", "given", "gave", "cattle"] # create a list of words

for word in words: # iterate over the words list
    print(word,"|",stemmer.stem(word)) # print the stem of each word in the words list


#####

import spacy # import the spacy module

nlp = spacy.load('en_core_web_sm') # Load the small English model, it comes with a default pipeline

doc = nlp("eat eating eaten eats went good fair hardest harden typical") # create a document object

for token in doc: # iterate over the tokens in the document
    print(token, "|", token.lemma_, "|", token.lemma)

# token.lemma_ gives the lemma of the token means the base form of the word
# token.lemma is the hash value of the lemma of the token that is used internally by spacy, it is used for
# faster comparison of the tokens and lemmas, as eat and eating have the same lemma, so they have the same hash value


## editing the lemma of a token from attribute ruler 

print(nlp.pipe_names) # print the names of the components in the pipeline

ar = nlp.get_pipe("attribute_ruler") # get the attribute ruler component from the pipeline
 
ar.add([[{"TEXT": "dawg"}], [{"TEXT":"fam"}]], {"LEMMA": "Brother"}) # add a pattern to the attribute ruler component
 # add a pattern to the attribute ruler component
# the pattern is a list of two lists, the first list contains the tokens that we want to match and the second list
# contains the tokens that we want to replace the matched tokens with, the third argument is a dictionary that contains
# the attributes that we want to change in the matched tokens, in this case we want to change the lemma of the matched 
# tokens to Brother

doc = nlp("Hey dawg, what's up fam?") # create a document object

for token in doc: # iterate over the tokens in the document
    print(token, "|", token.lemma_) 