import spacy

nlp = spacy.blank("en") # Load the blank English model, with no pipeline

doc1 = nlp("Tea is healthy and calming, don't you think?. Said by Mr. John the Doctor")
doc2 = nlp("Microsoft announced its quarterly earnings report last week, beating the estimates by $2 billion.")


# won't work because there is no pipeline
for ent in doc2.ents: # ent is an entity object and doc.ents gives all the entities in the document
    print(ent.text, " | " , ent.label_, " | " , spacy.explain(ent.label_)) # ent.label_ gives the label of the entity

print(nlp.pipeline)
print(nlp.pipe_names)

nlp = spacy.load('en_core_web_sm') # Load the small English model, it comes with a default pipeline

doc = nlp("Tea is healthy and calming, don't you think?. Said by Mr. John the Doctor")

print(nlp.pipeline)
print(nlp.pipe_names)

for token in doc:
    print(token, " | " , token.pos_ , " | " , token.lemma_ , " | " , token.head.text)  

# token.pos_ gives the part of speech of the token means the type of the word
# token.lemma_ gives the lemma of the token means the base form of the word
# token.head.text gives the head of the token means the word that the token is dependent on

text = "Microsoft announced its quarterly earnings report last week, beating the estimates by $2 billion."

doc = nlp(text)

for ent in doc.ents: # ent is an entity object and doc.ents gives all the entities in the document
    print(ent.text, " | " , ent.label_, " | " , spacy.explain(ent.label_)) # ent.label_ gives the label of the entity

# spacy.explain() gives the description of the entity label
# spacy.explain("ORG") gives the description of the ORG entity label
# ent.label_ gives the label of the entity means the type of the entity

# ner is a component that does named entity recognition means it recognizes the entities in the text
# entities are the objects in the text like person, organization, location, date, time, money, percentage, etc.

""" 
# Visualizing the dependency parse, https://spacy.io/usage/visualizers
from spacy import displacy
displacy.serve(doc, style="ent") # displacy is a visualizer, it renders the entities in the text 
"""


# Adding a new component to the Blank Pipeline

SourceNlp = spacy.load('en_core_web_sm') # Load the small English model, it comes with a default pipeline

nlps = spacy.blank("en") # Load the blank English model, with no pipeline

nlps.add_pipe("ner", source=SourceNlp) # add_pipe() adds a new component to the pipeline 
# ner is a component that does named entity recognition means it recognizes the entities in the text
# source=SourceNlp means we are using the ner component from the SourceNlp model

print(nlps.pipe_names) # add_pipe() adds a new component to the pipeline