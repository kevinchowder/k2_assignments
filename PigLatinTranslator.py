"""Prompts user to input a sentence, prints the pig latin version of sentence"""

vowels = ['a','e','i','o','u']

def findfirstvowel(string):
    """Returns index of first vowel in string"""
    index = 0

    while index < len(string):
        if string[index] in vowels:
            return index
        else:
            index = index + 1

def piglatinize(string):
    """Takes string and appends "way" if the word starts with a vowel,
    or 'ay' if a consonant and prints result"""
    newstring=[]
    for word in string:
        if findfirstvowel(word) == 0:
            newword = word[:] + "way"
            newstring.append(newword)
        else:
            newword = (word[findfirstvowel(word):len(word)] +
            word[:findfirstvowel(word)] + "ay")
            newstring.append(newword)
    newstring = " ".join(newstring)
    print(newstring)

# Main execution
userinput = input("Please enter your sentence without punctuation: ")
words = userinput.lower().split(" ") #converts to all lowercase, splits on space
piglatinize(words)
