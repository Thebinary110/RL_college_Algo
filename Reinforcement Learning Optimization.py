import numpy as np

episodes = 500
gamma = 0.9
early_stop_reward = 195

rewards_all = []

for ep in range(episodes):
    total_reward = 0
    G = 0

    for t in range(100):
        reward = np.random.choice([1, -1], p=[0.8, 0.2])
        total_reward += reward
        G += (gamma ** t) * reward

    rewards_all.append(total_reward)

    if ep > 50 and np.mean(rewards_all[-50:]) >= early_stop_reward:
        print("Early stopping at episode:", ep)
        break

print("Final return:", G)
print("Average reward:", np.mean(rewards_all))
