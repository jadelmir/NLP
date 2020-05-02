import sys 
from autocorrect import Speller
count = 0
spell = Speller(lang='en')
def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(
                    1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


def checkDistances(WordToCheck="worlt", fileName='words'):
    WordToCheck = WordToCheck.lower()
    minX = 100 
    name = None
    with open(fileName,'r') as fd:
        for line in fd.readlines():
            word =line.strip()
            x = levenshteinDistance(word, WordToCheck)
            if x < minX :
                minX,name = x , word
    return name


def openWord():
    arr = [] 
    with open("words", 'r') as fd:
        for line in fd.readlines():
            word = line.strip()
            arr.append(word)
    return arr 


def SpellSentence(sentence , words):
    global count
    sentence = sentence.split()
    arr = []

    for word in sentence:
        count += 1 
        if (count % 1000) == 0 :
            print(count , " word check for spelling error")
        word = word.lower()
        if word in words :
            arr.append(word)
            continue
        try:
            
            word = spell(word)
            arr.append(word)
        
        except :
            arr.append(word)
            pass

    return arr

def SpellText(Text):
    words = openWord()
    for i in Text:
            i = ",".join(SpellSentence(i,words))

    return Text


if __name__ == "__main__":
    stri  = "hello hte"
    print(SpellSentence(stri))
