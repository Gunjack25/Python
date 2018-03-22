from numpy import *


def run():
        #seterr(divide='ignore', invalid='ignore')
    x = matrix('1,1,2; 1,2,2; 1,3,4;1,4,5')
    y = matrix('3; 4; 7; 9')
    theta = matrix('0; 0; 0')
    alpha = 0.001
    num_iter = 5000
    theta = gradient_des(x, y, theta, alpha, num_iter)
    print(theta)

    # print(x)


def gradient_des(x, y, theta, alpha, num_iter):
    # j = len(x)
    m = 3
    k = []
    for i in range(num_iter):
        k = error(x, y, theta)

        theta = theta - (alpha / m) * k

    return theta


def error(x, y, theta):
    errorr = matmul(x, theta) - y
    m = 3

    answer = []
    # x is n*m matrix and theta is m*1 matrix, so x.theta is n*1 matrix
    # y is also n*1 matrix
    for t in range(m):
        el_mul = multiply(errorr, x[:, t])
        answer.append(sum(el_mul))
    # print(transpose(answer))
    return transpose(answer)


def normalization(x):

    m = 3
    n = size(x)

    for l in range(n):

        for i in range(m):
            rangexx = max(x[:, i]) - min(x[:, i])
            mean_val = mean(x[:, i])

            x[l, i] = (x[l, i] - mean_val) / rangexx

    return x


run()
