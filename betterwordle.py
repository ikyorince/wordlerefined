#importing required libraries
import random
import requests


#downloading an open source list of English word I found, replace it with a better version if you want, it's just a text file
url = 'http://www.mieliestronk.com/corncob_lowercase.txt'
r = requests.get(url, allow_redirects=True)

open('corncob_lowercase.txt', 'wb').write(r.content)

file = open("corncob_lowercase.txt")
#Turning the text file into a python list of words
words = file.read().split("\n")

# #number of words
# count = 0
# for word in words:
#     if len(word) == 5:
#         count += 1
#         valid = True
# print(count)


def appendnewword(word):
    """
    This method appends the new word to the old file
    """
    textfile = open("previouswords.txt", "a")
    textfile.write(word + "\n")
    textfile.close()

def generatenewword():
    """
    This method generates a random 5 letter word from the list of words given in the text file
    """
    valid = False
    while(not valid):
        index = random.randint(0,58000)
        word = words[index]
        if len(word)==5:
            valid = True
            return word

def checknewword(newword):
    """
    This method checks if the word has been used before, if not, it updates the list in a text file
    """
    file = open("previouswords.txt", "a+" )
    # Turning the text file into a python list of words
    previousWords = file.read().split("\n")
    file.close()
    if newword in previousWords:
        newword = generatenewword()
        checknewword(newword)
    else:
        appendnewword(word=newword)
        print(newword)


