from sys import exit

with open("count_1w.txt", "r") as f:
    allWords = f.read().splitlines()

wordFreq = [w.split() for w in allWords]

fiveLetters = [w for w in wordFreq if len(w[0]) == 5]


def possibleWords(inputDict, confirmed, possible, avoid):
    if len(confirmed) < 5:
        confirmed = confirmed + "." * (5 - len(confirmed))
    if len(possible) < 5:
        possible = possible + "." * (5 - len(possible))
    noAvoids = []
    if len(avoid) > 0:
        for word in inputDict:
            filterIn = True
            for i in range(5):
                if word[0][i] not in confirmed and word[0][i] not in possible:
                    if word[0][i] in avoid:
                        filterIn = False
                        break
            # if len([l for l in avoid if l in word]) == 0:
            if filterIn:
                noAvoids.append(word)
    else:
        noAvoids = inputDict

    withConfirmed = []
    if len(confirmed) > 0:
        for word in noAvoids:
            filterIn = True
            for i in range(5):
                if confirmed[i] != "." and confirmed[i] != word[0][i]:
                    filterIn = False
                    break
            if filterIn:
                withConfirmed.append(word)
    else:
        withConfirmed = noAvoids

    withPossible = []
    for word in withConfirmed:
        possibleLetters = [l for l in possible if l != "."]
        if len(list(set([l for l in word[0] if l in possibleLetters]))) == len(list(set(possibleLetters))):
            withPossible.append(word)

    final = []
    if len(possible) > 0:
        for word in withPossible:
            filterIn = True
            for i in range(5):
                if possible[i] != ".":
                    if word[0][i] == possible[i]:
                        filterIn = False
            if filterIn:
                final.append(word)
    else:
        final = withPossible

    return final


def guess(inputDict=fiveLetters):

    if len(inputDict) == 1:
        print(f"The word is {inputDict[0][0]}")
        exit(0)

    if inputDict != fiveLetters:
        sortedList = sorted(inputDict, key=lambda x: int(x[1]), reverse=True)
        print("Top 10 guesses:")
        print([w[0] for w in sortedList[:10]])

    inputConfirm = input("Enter confirmed letters: ")
    if inputConfirm == "restart":
        guess(fiveLetters)

    inputPossible = input("Enter possible letters: ")
    inputAvoid = input("Enter avoid letters: ")

    filteredDict = possibleWords(
        inputDict, inputConfirm, inputPossible, inputAvoid)
    guess(filteredDict)


guess()
