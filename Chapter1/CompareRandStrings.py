import string, random
compareTo = "methinks it is like a weasel"
chars = list(string.ascii_lowercase)
chars.append(" ")

def createString():
    theString = []
    for i in range(28):
        theString.append(random.choice(chars))
    return "".join(theString)

def checkScore(compare):
    score = 0;
    for ch1, ch2 in zip(compare, compareTo):
        if (ch1 == ch2):
            score += 1
    return score

def compare():
    compare = createString()
    count = 0
    bestWord = ""
    bestScore = 0
    while (checkScore(compare) != 28):
        if (checkScore(compare) > bestScore):
            bestScore = checkScore(compare)
            bestWord = compare
        if (count % 1000 == 0):
            print(count, bestWord, bestScore)
        compare = createString()
        count += 1

compare()