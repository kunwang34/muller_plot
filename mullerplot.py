import numpy as np
import matplotlib.pyplot as plt

def mullerplot(data, label, absolute=0):
    if absolute:
        norm = max(np.sum(data, axis = 0))
    else:
        norm = np.sum(data, axis=0)
    data_normed = data / norm
    mp = np.cumsum(data_normed, axis=0)
    adjustpos = 0.5*(1-mp[-1])
    
    #plt.plot(mp.T,color='black', lw=1)
    fig, ax = plt.subplots(1, 1)
    if absolute:
        ax.fill_between(range(data.shape[1]), np.zeros(data.shape[1])+adjustpos, mp[0]+adjustpos, label = label[0], alpha = 0.5)
        for i in range(mp.shape[0] - 1):
            ax.fill_between(range(data.shape[1]), mp[i]+adjustpos, mp[i+1]+adjustpos,
                            label = label[i+1], alpha = 0.5)
    else:
        ax.fill_between(range(data.shape[1]), mp[0], label=label[0],alpha=0.5)
        for i in range(mp.shape[0]-1):
            ax.fill_between(range(data.shape[1]), mp[i], mp[i+1], label=label[i+1],alpha=0.5)
    ax.legend(bbox_to_anchor=(1, 0), loc=3, borderaxespad = 0)
    plt.show()

if __name__ == '__main__':
    data = np.random.rand(20, 10)
    label = range(20)
    mullerplot(data,label)
