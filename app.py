from betterwordle import generatenewword
from betterwordle import checknewword


if __name__ == "__main__":
    newword = generatenewword()
    print("**********Your new word is************")
    checknewword(newword)
    print("**********And here are all your previous words************")
    file = open("previouswords.txt", "r")
    # Turning the text file into a python list of words
    previousWords = file.read().split("\n")
    file.close()
    for word in previousWords[0:(len(previousWords) - 2)]:
        print(word)
