import pandas as pd


def makeTDM(words, docs):
    # pre-make headers for columns
    columns = ["word"]
    counter = 1
    for doc in docs:
        columns.append('d' + str(counter))
        counter += 1

    # create Term-Document Matrix
    tdm = [[0 for x in range(len(docs) + 1)] for y in range(len(words))]

    # filling in TDM
    for i in range(len(words)):
        for j in range(len(docs)):
            if words[i] in docs[j].split():     # if word is in document, then set to 1
                tdm[i][j+1] = 1
        tdm[i][0] = words[i]        # add word's name to a row

    df = pd.DataFrame(tdm, columns=columns)
    print(df)

    return tdm


def makePosInd


if __name__ == '__main__':
    d0 = "preliminary findings in cancer research"
    d1 = "novel cancer research findings"
    d2 = "new research in cancer healing"
    docs = [d0, d1, d2]
    print(pd.DataFrame(docs, columns=["Document"]))
    print()

    words = set()
    for doc in docs:
        for temp in doc.split(' '):
            words.add(temp)
    words = list(words)

    TDM = makeTDM(words, docs)
