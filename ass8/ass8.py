import pandas as pd


def multiply(arr, P, name):
    res = []
    for i in range(0, len(P)):
        res.append(arr.iat[0, 0] * P.iat[0, i] +
                   arr.iat[1, 0] * P.iat[1, i] +
                   arr.iat[2, 0] * P.iat[2, i] +
                   arr.iat[3, 0] * P.iat[3, i])
    return pd.DataFrame(res, columns=[name])


def iterate(arr, P, rounds):
    for i in range(0, rounds):
        arr = multiply(arr, P, "x"+str(i+1))
    return arr


if __name__ == '__main__':
    alpha = 0.1
    d = []

    matrix = pd.DataFrame([[0, 1, 1, 1],
                           [0, 0, 1, 0],
                           [0, 1, 0, 0],
                           [1, 1, 0, 0]])
    print(matrix)

    # Calculate d
    for i in range(0, len(matrix)):
        temp = 0
        for j in range(0, len(matrix[0])):
            if matrix[j][i] == 1:
                temp += 1
        d.append(temp)

    # Calculate P
    temp = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            temp[i][j] = alpha / 4 + (1 - alpha) / d[i] * matrix[j][i]
    P = pd.DataFrame(temp)

    x0 = pd.DataFrame([0.25, 0.25, 0.25, 0.25])

    print(d)
    print(P)

    '''x1 = multiply(x0, P, "x1")
    print(x1)
    x2 = multiply(x1, P, "x2")
    print(x2)
    x3 = multiply(x2, P, "x3")
    print(x3)
    x4 = multiply(x3, P, "x4")
    #print(x4)
    #x5 = multiply(x4, P, "x5")
    #print(x5)'''

    print(iterate(x0, P, 2))
    print(iterate(x0, P, 5))
