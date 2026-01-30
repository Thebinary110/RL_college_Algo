import numpy as np

np.random.seed(1)

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

X = np.c_[np.ones((100,1)), X]

theta = np.random.randn(2,1)

lr = 0.1
epochs = 100
batch_size = 20

for epoch in range(epochs):
    idx = np.random.permutation(100)
    X = X[idx]
    y = y[idx]

    for i in range(0, 100, batch_size):
        xi = X[i:i+batch_size]
        yi = y[i:i+batch_size]

        grad = (2/batch_size) * xi.T.dot(xi.dot(theta) - yi)
        theta -= lr * grad

print("Final parameters:")
print(theta)
