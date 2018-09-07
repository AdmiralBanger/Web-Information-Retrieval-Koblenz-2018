import operator

import pandas as pd


def getTermProbDocModels(docs, words):
    matrDocModel = [[0 for x in range(len(docs) + 1)] for y in range(len(words))]
    for j in range(len(words)):
        for i in range(len(docs) + 1):
            count = 0
            if i == 0:
                matrDocModel[j][i] = words[j]
            else:
                doc = docs[i - 1].split()
                for word in doc:
                    if word == words[j]:
                        count += 1
                matrDocModel[j][i] = count / len(doc)
    return matrDocModel


def getTermProbCorpModels(docs, words):
    matrCorpModel = [[0 for x in range(2)] for y in range(len(words))]
    lenCorpWord = 0

    for doc in docs:
        docWords = doc.split()
        lenCorpWord += len(docWords)

    for j in range(len(words)):
        count = 0
        for i in range(2):
            if i == 0:
                matrCorpModel[j][i] = words[j]
            else:
                for doc in docs:
                    docWords = doc.split()
                    for word in docWords:
                        if word == words[j]:
                            count += 1
                matrCorpModel[j][i] = count / lenCorpWord
    return matrCorpModel


def getLinInterpModel(lyambda, matrDocModel, matrCorpModel):
    matrLinInterp = [[0 for x in range(len(docs) + 1)] for y in range(len(words))]
    for j in range(len(words)):
        for i in range(len(docs) + 1):
            count = 0
            if i == 0:
                matrLinInterp[j][i] = words[j]
            else:
                matrLinInterp[j][i] = lyambda*matrDocModel[j][i]+(1-lyambda)*matrCorpModel[j][1]
    return matrLinInterp


def getRank(matrModel, query):
    Rank = [[0 for x in range(2)] for y in range(len(docs))]
    wordsInQuery = query.split()
    for j in range(len(matrModel[0]) - 1):
        for k in range(2):
            if k == 0:
                Rank[j][k] = "d" + str(j)
            else:
                multipl = 1
                for word in wordsInQuery:
                    for i in range(len(matrModel)):
                        if word == matrModel[i][0]:
                            multipl = multipl * matrModel[i][j + 1]
                Rank[j][k] = multipl
    return Rank


if __name__ == '__main__':
    d1 = "click go the shears boys click click click"
    d2 = "click click"
    d3 = "metal here"
    d4 = "metal shears click here"
    query = "click shears"
    lyambda = 0.5
    docs = [d1, d2, d3, d4]
    print(pd.DataFrame(docs, columns=["Document"]))
    print()

    words = set()
    for doc in docs:
        for temp in doc.split(' '):
            words.add(temp)
    words = list(words)
    print(words)
    print()

    matrDocModel = getTermProbDocModels(docs, words)
    matrCorpModel = getTermProbCorpModels(docs, words)
    temp1 = pd.DataFrame(matrDocModel, columns=["Word", "d0", 'd1', 'd2', 'd3'])
    temp2 = pd.DataFrame(matrCorpModel, columns=["Word", "Prob"])

    print(temp1)
    print(temp2)
    print()

    rank1 = pd.DataFrame(sorted(getRank(matrDocModel, query), key=lambda x: x[1], reverse=True), columns=["Doc", "un-smoothed"])
    matrLinInterp = getLinInterpModel(lyambda, matrDocModel, matrCorpModel)
    rank2 = pd.DataFrame(sorted(getRank(matrLinInterp, query), key=lambda x: x[1], reverse=True), columns=["Doc", "linear-interpolated"])
    print(rank1)
    print(rank2)