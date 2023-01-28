# Regex in Customer Service Chatbot

import re

chat1 = "Hi, how can I help you?, I am having an issue with my order # 1234567890"
pattern = "order[^\d]*(\d*)" # [^\d] means match anything except a digit after the word order and (\d*) means match any digit after the word order
# so the pattern will match the first character after order which will be space
matches = re.findall(pattern, chat1)
print(matches)

chat2 = "Hi, how can I help you?, I am having an issue with my order number 1234567890, I need to cancel it"
pattern = "order[^\d]*(\d*)"
matches = re.findall(pattern, chat2)
print(matches)

chat3 = "My order 1234567890 is not delivered yet"
pattern = "order[^\d]*(\d*)"
matches = re.findall(pattern, chat3)
print(matches)

# making a function to find the order number

def findPatternMatch(pattern, text):
    matches = re.findall(pattern, text)
    if len(matches) > 0:
        return matches[0]
    else:
        return None

x = findPatternMatch("order[^\d]*(\d*)", chat1)
print(x)


##########-------------------------------------------------------------------------###########
## retrieve email addess and phone number from a text

chat1 = "Hi, how can I help you?, I am having an issue with my order # 1234567890, my email is  absbadbsa@sdssss.com and my phone number is 1234567890"
chat2 = "here's my email address: abc_@xyz.io, (123)-456-7890"
chat3 = "get in touch with me at email id : ssd_sad_@opp.net and phone number 1234567890"

pattern = "[a-zA-Z0-9_]*@[a-zA-Z0-9_]*\.[a-zA-Z0-9]*" # [a-zA-Z0-9_]* means match any alphanumeric character including underscore 0 or more times after @ and before and \. means match . and repeat the same pattern after the dot

x = findPatternMatch("[a-zA-Z0-9_]*@[a-zA-Z0-9_]*\.[a-zA-Z0-9]*", chat1)
print(x)
x = findPatternMatch("[a-zA-Z0-9_]*@[a-zA-Z0-9_]*\.[a-zA-Z0-9]*", chat2)
print(x)
x = findPatternMatch("[a-zA-Z0-9_]*@[a-zA-Z0-9_]*\.[a-zA-Z0-9]*", chat3)
print(x)

# phone number pattern

pattern = "(\d{10})|(\(\d{3}\)-\d{3}-\d{4})"

x = findPatternMatch("(\d{10})|(\(\d{3}\)-\d{3}-\d{4})", chat1)
print(x)
x = findPatternMatch("(\d{10})|(\(\d{3}\)-\d{3}-\d{4})", chat2)
print(x)
x = findPatternMatch("(\d{10})|(\(\d{3}\)-\d{3}-\d{4})", chat3)
print(x)

