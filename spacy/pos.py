import spacy 
nlp = spacy.load('en_core_web_sm') 
doc = nlp("A Person named John Smith is working in the company named ABC, he is works as a Data Scientist")

for token in doc: 
    print(token, "|", token.pos, "|", token.pos_, spacy.explain(token.pos_))

    # adposition is a preposition or postposition and connects words, phrases, or clauses, 
    # preposition and postpostion together called adpositions

    # output 
""" 
A | 90 | DET determiner
Person | 96 | PROPN proper noun
named | 100 | VERB verb
John | 96 | PROPN proper noun
Smith | 96 | PROPN proper noun
is | 87 | AUX auxiliary
working | 100 | VERB verb
in | 85 | ADP adposition
the | 90 | DET determiner
company | 92 | NOUN noun
named | 100 | VERB verb
ABC | 96 | PROPN proper noun
, | 97 | PUNCT punctuation
he | 95 | PRON pronoun
is | 87 | AUX auxiliary
works | 100 | VERB verb
as | 85 | ADP adposition
a | 90 | DET determiner
Data | 96 | PROPN proper noun
Scientist | 96 | PROPN proper noun
"""

doc = nlp("Elon Musk is the CEO of Tesla, he is the founder of SpaceX")

for token in doc:
    print(token, "|", token.pos, "|", token.pos_, spacy.explain(token.pos_), "|", token.tag, "|", token.tag_, spacy.explain(token.tag_))

    # token.tag_ is further categorization of the token.pos_ attribute
    # it actually gives the part of speech of the token
    # and token.tag_ gives the fine-grained part of speech of the token
    # like if the token.pos_ is a noun then token.tag_ can be a singular noun or a plural noun
    # if it is a verb then token.tag_ can be a past tense verb or a present tense verb

    # spacy is smart enough to tell whether the noun is singular or plural, or verb is past tense or present tense.


## How pos tag can be used in real world applications
## It can use to extract unnecessary words/tokens from the text.

earning_text = """  Tesla reported automotive revenue of $21.3 billion in the fourth quarter, 
representing 33% growth year-over-year. $467 million of that came from regulatory credits 
in the fourth quarter of 2022, 
up by nearly half from the prior year in the same period."""

doc = nlp(earning_text)

for token in doc:
    if token.pos_ == "NOUN":
        print(token , "|", token.pos_, "|", token.tag_, "|", token.tag, "|", spacy.explain(token.tag_))

print("-------------------------------------`       ")

for token in doc:
    if token.pos_ not in ["SPACE", "PUNCT", "X"]:
        print(token, "|", token.pos_, "|", token.tag_, "|", token.tag, "|", spacy.explain(token.tag_))


filtered_tokens = []
for token in doc:
    if token.pos_ not in ["SPACE", "PUNCT", "X"]: # if the token is not a space, punctuation or X
        filtered_tokens.append(token) # append the token to the list
    
print(filtered_tokens)


#spacy gives you count of the tokens in the text
# doc.count_by(spacy.attrs.POS)
print(doc.count_by(spacy.attrs.POS)) # it gives you the count of the tokens in the text based on the POS tag of the token 
# in the text

# what is 103 ?
# 103 is the id of the token.pos_ attribute

print(doc.vocab[103].text) # it gives you the text of the token.pos_ attribute

for k, v in doc.count_by(spacy.attrs.POS).items(): # k and v are the key and value of the dictionary
    # dict here is the doc.count_by(spacy.attrs.POS) dictionary which is the count of the tokens in the text 
    # based on the POS tag of the token
    print(f"{k}. {doc.vocab[k].text:{5}}: {v}") # print the key and value of the dictionary

# num pos tag 
# give example of the num pos tag 
# num pos tag is used to represent the numbers in the text