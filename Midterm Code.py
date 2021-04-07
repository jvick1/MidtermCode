#Midterm Code

#----summary
#take user input
#ask for what service
#return requested service

#----Needed Packages
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

#---- user input
#user_input = input("Enter your string here: ")
user_input = "Hello how are you doing today?"
#what numbers are allowed
numbers = [1,2,3]
#pre-trained model
sia = SentimentIntensityAnalyzer()
#create empty dictionary
freqTable = dict()
#define stop words
stopWords=set(stopwords.words("english"))

#----What do you want done?
while True:
    try: 
        choice = int(input("Enter 1 for Part-Of-Speech Tagging.\nEnter 2 for Word Frequency.\nEnter 3 for Sentiemnt.\n"))
    except ValueError:
        print("Sorry, I didn't get that try again.")
        continue
    if choice in numbers:
        break
    else:
        print("Sorry, I didn't get that try again.")
        continue

#---- tokenize and functions
#break user input into words
words = word_tokenize(user_input)
#pos tag
tagged = nltk.pos_tag(words)
#this function is for if we pick #1 
def VerbsOrNouns():
    prompt = int(input("Enter 1 for all POS-tags.\nEnter 2 for Verbs.\nEnter 3 for Nouns.\n"))
    if prompt == 1:
        print(tagged)
    elif prompt == 2:
        print([(word,tag) for word, tag in tagged if tag in ("VB", "VBG", "VBD", "VBN", "VBP", "VBZ")])
    elif prompt == 3:
        print([(word,tag) for word, tag in tagged if tag in ("NN", "NNS", "NNP", "NNPS")])
    else:
        print("Try picking again...")
        VerbsOrNouns()


#----Results
#looking into what the user picked
if int(choice) == 1:
    VerbsOrNouns()
if int(choice) == 2:
    #count words
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    print(freqTable)
if int(choice) == 3:
    sia.polarity_scores(user_input)





