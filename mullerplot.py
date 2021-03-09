import numpy as np
import matplotlib.pyplot as plt

def mullerplot(data, label):
    data_normed = data / np.sum(data, axis=0)
    mp = np.cumsum(data_normed, axis=0)
    plt.plot(mp.T,color='black', lw=1)
    plt.fill_between(range(data.shape[1]), mp[0], label=label[0],alpha=0.5)
    print(mp.shape)
    for i in range(mp.shape[0]-1):
        plt.fill_between(range(data.shape[1]), mp[i], mp[i+1], label=label[i+1],alpha=0.5)
    plt.legend(bbox_to_anchor=(1, 0), loc=3, borderaxespad=0)
    plt.show()

if __name__ == '__main__':
    data = np.random.rand(20, 10)
    label = range(20)
    mullerplot(data,label)
