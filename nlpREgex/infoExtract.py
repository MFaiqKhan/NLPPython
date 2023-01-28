import re

text='''
Born	Elon Reeve Musk
June 28, 1971 (age 50)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa (1971–present)
Canada (1971–present)
United States (2002–present)
Education	University of Pennsylvania (BS, BA)
Title	
Founder, CEO and Chief Engineer of SpaceX
CEO and product architect of Tesla, Inc.
Founder of The Boring Company and X.com (now part of PayPal)
Co-founder of Neuralink, OpenAI, and Zip2
Spouse(s)	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)
'''

def findPatternMatch(pattern, text):
    matches = re.findall(pattern, text)
    if len(matches) > 0:
        return matches[0]
    else:
        return None

# for Age

pattern = "age (\d+)" # where + means one or more digits, means age should be followed by one or more digits cant be zero

x = findPatternMatch(pattern, text)
print(x)

# for his full name

pattern = "Born(.*)\n" # where * means any character 0 or more times and \n means new line 

x = findPatternMatch(pattern, text).strip() # strip() removes the white space from the beginning and end of the string
print(x)

# for his born date

pattern = 'Born.*\n(.*)\(age' # anything after the new line and before (age

x = findPatternMatch(pattern, text).strip()
print(x)

# for his birth place

pattern = "\(age.*\n(.*)"

x = findPatternMatch(pattern, text).strip()
print(x)

def extractInformation(text):
    info = {} # empty dictionary , # info[] is a dictionary and name is the key and findPatternMatch is the value
    info['name'] = findPatternMatch("Born(.*)\n", text).strip() 
    info['bornDate'] = findPatternMatch('Born.*\n(.*)\(age', text).strip()
    info['bornPlace'] = findPatternMatch("\(age.*\n(.*)", text).strip()
    info['age'] = findPatternMatch("age (\d+)", text)
    return info

print(extractInformation(text))

text = '''
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 64)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Stanford University (drop-out)
Occupation	Chairman and MD, Reliance Industries
Spouse(s)	Nita Ambani ​(m. 1985)​[3]
Children	3
Parent(s)	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
'''

print(extractInformation(text))