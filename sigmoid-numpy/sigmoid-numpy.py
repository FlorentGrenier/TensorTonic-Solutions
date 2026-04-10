import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.asarray(x)
    result = np.asarray(1/(1+np.exp(-x)))
    return result