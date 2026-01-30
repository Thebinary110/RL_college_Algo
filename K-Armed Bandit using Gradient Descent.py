import numpy as np

k = 5
steps = 1000
alpha = 0.1

true_reward = np.random.normal(0, 1, k)
q = np.zeros(k)
pi = np.ones(k) / k

def softmax(x):
    e = np.exp(x - np.max(x))
    return e / np.sum(e)

for t in range(steps):
    action = np.random.choice(k, p=pi)

    reward = np.random.normal(true_reward[action], 1)

    baseline = np.mean(q)

    for i in range(k):
        if i == action:
            q[i] += alpha * (reward - baseline) * (1 - pi[i])
        else:
            q[i] -= alpha * (reward - baseline) * pi[i]

    pi = softmax(q)

print("Estimated action values:", q)
print("Final policy:", pi)
