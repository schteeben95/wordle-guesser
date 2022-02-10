from sys import exit

with open("words_alpha.txt", "r") as f:
    allWords = f.read().splitlines()

fiveLetters = [w for w in allWords if len(w) == 5]


def possibleWords(inputDict, confirmed, possible, avoid):
    noAvoids = []
    for word in inputDict:
        if len([l for l in avoid if l in word]) == 0:
            noAvoids.append(word)

    withConfirmed = []
    for word in noAvoids:
        filterIn = True
        for i in range(5):
            if confirmed[i] != "." and confirmed[i] != word[i]:
                filterIn = False
                break
        if filterIn:
            withConfirmed.append(word)

    withPossible = []
    for word in withConfirmed:
        possibleLetters = [l for l in possible if l != "."]
        if len([l for l in word if l in possibleLetters]) > 0:
            withPossible.append(word)

    final = []
    for word in withPossible:
        filterIn = True
        for i in range(5):
            if possible[i] != ".":
                if word[i] == possible[i]:
                    filterIn = False
        if filterIn:
            final.append(word)

    return final


def guess(inputDict=fiveLetters):

    if len(inputDict) == 1:
        print(f"The word is {inputDict[0]}")
        exit(0)

    if inputDict != fiveLetters:
        print(inputDict)

    inputConfirm = input("Enter confirmed letters: ")
    inputPossible = input("Enter possible letters: ")
    inputAvoid = input("Enter avoid letters: ")

    filteredDict = possibleWords(
        inputDict, inputConfirm, inputPossible, inputAvoid)
    guess(filteredDict)


guess()
