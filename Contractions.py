import contractions


def handleContractions(Text):
    for i in Text :
        i = contractions.fix(i)
    return Text
    
if __name__ == "__main__":
    t = ["you're happy nw"]
    te = handleContractions(t)
    print(t)
