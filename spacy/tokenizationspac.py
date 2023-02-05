import spacy

# this just create a blank pipeline with default tokenizer
nlp = spacy.blank("en") # Load the small English model
# blank model creates a new empty Doc   object and then we can add tokens to it, it does create a new model 
# with the specified language ID and blank pipeline but with no text.

doc = nlp("Tea is healthy and calming, don't you think?. Said by Mr. John the Doctor")

# default tokenizer, gives word tokenization
for tokens in doc:
    print(tokens)

print ("-------------------indexing------------------")

print(doc[-1])

print("""-------------------token attributes------------------""")

token0 = doc[0]
print(token0)
print(type(token0)) # gives the type of the token object
print(dir(token0)) # gives all the attributes of the token object

# using attributes

print(token0.like_num) # checks if the token is a number

print(token0.is_alpha) # checks if the token is alphabetical


print("""-------------------email extraction------------------""")

with open("students.txt") as f: # with is a context manager, it will automatically close the file
    text = f.readlines() # readlines() reads the file line by line and returns a list of lines

print(text)

text = " ".join(text) # join() joins the list of lines into a single string
print(text)

doc = nlp(text)
emails = []
for token in doc:
    if token.like_email:
        emails.append(token.text)

print(emails)

## Now If I want to do sentence segmentation than I would have to add a new component to the pipeline

# add a new component to the pipeline

# lets add a component for sentencizer # sentencizer is a component that does sentence segmentation

print(nlp.pipe_names) # first it will print the default tokenizer, which will be empty

nlp.add_pipe("sentencizer") # add_pipe() adds a new component to the pipeline
print (nlp.pipe_names) # pipe_names gives the names of the components in the pipeline

doc = nlp("Tea is healthy and calming, don't you think?. Said by Mr. John the Doctor")

for sentence in doc.sents:
    print(sentence)

print("Exercise:")

#Exercise: 

text='''
Look for data to help you address the question. Governments are good
sources because data from public research is often freely available. Good
places to start include http://www.data.gov/, and http://www.science.
gov/, and in the United Kingdom, http://data.gov.uk/.
Two of my favorite data sets are the General Social Survey at http://www3.norc.org/gss+website/, 
and the European Social Survey at http://www.europeansocialsurvey.org/.
'''

doc = nlp(text)

websites = []

for tokens in doc:
    if tokens.like_url:
        websites.append(tokens.text)

print(websites)

transactions = "Tony gave two $ to Peter, Bruce gave 500 € to Steve"

doc = nlp(text)

array = []

for tokens in doc:
    if tokens.like_num and doc[tokens.i + 1].is_currency:
        a = tokens.text, doc[tokens.i + 1].text
        array.append(a)

print(array)