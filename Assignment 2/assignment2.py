import random
import matplotlib.pyplot as plt

# This returns datastream with 0's and 1's, consider 0 is false and 1 is true.
def genDatastream (N, TP):
    mas = []
    for i in range(0, N):
        mas.append(0)

    j = 0
    while j != TP:
        temp = random.randint(0, N-1)
        if mas[temp] != 1:
            mas[temp] = 1
            j += 1

    return mas


def calcPrecNRec (mas, TP):
    relCount = 0    # Counter for relevant documents
    procCount = 0   # Counter for processed documents
    precMat = [1]
    recMat = [0]
    for doc in mas:
        if doc == 1:
            relCount += 1
        procCount += 1
        prec = relCount/procCount
        rec = relCount/TP
        precMat.append(prec)
        recMat.append(rec)

    return zip(recMat, precMat)


def plot(mas, ax, num):
    x, y = zip(*mas)
    ax.plot(x, y, label='tp = ' + str(num))
    ax.legend(loc='upper right')
    ax.set_xlabel('recall')
    ax.set_ylabel('precision')


if __name__ == '__main__':
    mas1 = calcPrecNRec(genDatastream(10, 5), 5)
    mas2 = calcPrecNRec(genDatastream(50, 15), 15)
    mas3 = calcPrecNRec(genDatastream(75, 25), 25)
    mas4 = calcPrecNRec(genDatastream(100, 50), 50)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    plot(mas1, ax1, 1)
    plot(mas2, ax2, 2)
    plot(mas3, ax3, 3)
    plot(mas4, ax4, 4)
    plt.suptitle('Precision Recall Graph', fontsize=16)

    plt.show()
