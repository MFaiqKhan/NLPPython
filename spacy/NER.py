import spacy

nlp = spacy.load('en_core_web_sm')

print(nlp.pipe_names)

doc = nlp('Apple is looking at buying U.K. startup for $1 billion')

for ent in doc.ents:
    print(ent.text, " | " , ent.label_, " | " , spacy.explain(ent.label_))

## spacy default entity isn't good enough for our use case, and it isn't powerful

print(nlp.pipe_labels['ner']) # ner is the name of the pipeline component for named entity recognition (NER) 
# pipe_labels is a dictionary of the pipeline component names and their labels
# by default NER has 18 labels, but we can add more if we train our own model

# using NER inbuilt capabilities in spacY to add new entity labels

doc = nlp("Tesla is going to acquire Twitter for $1 billion")

for ent in doc.ents:
    print(ent.text, " | " , ent.label_, " | " , spacy.explain(ent.label_))

# As we know that tokens are span objects, we can use the same to get the start and end index of the entity

type(doc[2:4]) # spacy.tokens.span.Span object which is a span of tokens 
# span is a slice of a Doc object and can be used to access the tokens in the slice

from spacy.tokens import Span # importing Span class from spacy.tokens

# creating a new entity label
s1 = Span(doc, 0, 1, label = 'ORG') # creating a span object for Tesla
s2 = Span(doc, 5, 6, label = 'ORG') # creating a span object for Twitter

doc.set_ents([s1, s2], default="unmodified") # setting the entities in the doc object
# s1 and s2 are the span objects for Tesla and Twitter respectively and 
# default is the label for the rest of the entities

for ent in doc.ents:
    print(ent.text, " | " , ent.label_, " | " , spacy.explain(ent.label_))

# Excerise 1:

text = """Kiran want to know the famous foods in each state of India. So, he opened Google and search for this question. Google showed that
in Delhi it is Chaat, in Gujarat it is Dal Dhokli, in Tamilnadu it is Pongal, in Andhrapradesh it is Biryani, in Assam it is Papaya Khar,
in Bihar it is Litti Chowkha and so on for all other states"""

doc = nlp(text)

Country_names = []

for ent in doc.ents:
    if ent.label_ == "GPE":
        a = ent.text, " | " , ent.label_, " | " , spacy.explain(ent.label_)
        Country_names.append(a)

print(Country_names)

text = """Sachin Tendulkar was born on 24 April 1973, Virat Kholi was born on 5 November 1988, Dhoni was born on 7 July 1981
and finally Ricky ponting was born on 19 December 1974."""

doc = nlp(text)

dates = []

for ent in doc.ents:
    if ent.label_ == "DATE":
        a = ent.text
        dates.append(a)

print(dates)