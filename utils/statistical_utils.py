def sigmoid(x,s):
    return s/(1+np.exp(-x/s))

def softmax(x, temperature = 0.1):
    return np.exp(x/temperature)/np.sum(np.exp(x/temperature))