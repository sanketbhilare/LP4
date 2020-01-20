import numpy as np
import random
from matplotlib import pyplot as plt

#======= Q(a) ========

# generate training data set
X = [np.random.normal(size=2) for i in range(100)]
Z = np.random.normal()
a1 = np.array([3, 3])
a2 = np.array([3, -3])
Y = [(1.0 / (1.0 + np.exp(-np.dot(a1, x))) + np.dot(a2, x)**2 + Z) for x in X]

# generate testing data set
X_test = [np.random.normal(size=2) for i in range(1000)]
Z = np.random.normal()
a1 = np.array([3, 3])
a2 = np.array([3, -3])
Y_test = [(1.0 / (1.0 + np.exp(-np.dot(a1, x))) + np.dot(a2, x)**2 + Z) for x in X_test]


def SGDsolver(X, Y, n, hid):
    # initialize the parameters, assume we have k, i, j layers
    # input X_k, hidden layer output H, last layer output y
    # hid is the number of hidden layers
    eta = 0.001
    W_ki = np.random.normal(size=(2, hid))
    W_ij = np.random.normal(size=hid)
    W_k0 = 0
    W_i0 = 0

    for i in range(n):
        # print i
        ind = random.randint(0, len(Y)-1)
        X_k = X[ind]
        t = Y[ind]
        H = 1. / (1. + np.exp(-(np.dot(X_k, W_ki) + W_k0)))
        y = np.dot(W_ij, H) + W_i0

        # update the last layer
        W_ij_new = W_ij - 2*eta*(y - t)*H
        W_i0_new = W_i0 - 2*eta*(y - t)
        W_ki_new = W_ki - eta*np.outer(np.multiply(2*(y - t)*W_ij, H), X_k).T
        W_k0_new = W_k0 - eta*np.multiply(2*(y - t)*W_ij, H).T

        W_ij = W_ij_new
        W_ki = W_ki_new
        W_i0 = W_i0_new
        W_k0 = W_k0_new

    return W_ki, W_ij, W_i0, W_k0


def forward(W_ki, W_ij, W_i0, W_k0, X, Y):
    err_sq = 0
    for i in range(0,len(Y)):
        X_k = X[i]
        t = Y[i]
        H = 1. / (1. + np.exp(-(np.dot(X_k, W_ki) + W_k0)))
        y = np.dot(W_ij, H) + W_i0
        err_sq += (t - y)**2
    return err_sq/len(Y)

#======= Q(b) ========

err_train = []
err_test = []
epoch = range(100, 2000, 200)
for i in epoch:
    W_ki, W_ij, W_i0, W_k0 = SGDsolver(X, Y, i, 10)
    err_train.append(forward(W_ki, W_ij, W_i0, W_k0, X, Y))
    err_test.append(forward(W_ki, W_ij, W_i0, W_k0, X_test, Y_test))

plt.plot(epoch, err_train, 'r', epoch, err_test, 'b')

# I use 100 to 2000 epochs with 200 interval here.
# The results show decrease during this range and there is no obvious over-fitting case here.

#======= Q(c) ========

err_train = []
err_test = []
epoch = range(100, 2000, 200)

for j in range(1, 11, 1):
    for i in epoch:
        W_ki, W_ij, W_i0, W_k0 = SGDsolver(X, Y, i, j)
        err_train.append(forward(W_ki, W_ij, W_i0, W_k0, X, Y))
        err_test.append(forward(W_ki, W_ij, W_i0, W_k0, X_test, Y_test))

    print np.mean(err_train), np.mean(err_test)
print err_train[-1], err_test[-1]
