import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix M (swap rows and columns).
    """
    A = np.asarray(A)
    rows, cols = A.shape
    result = np.empty((cols, rows), dtype=A.dtype)
    
    for i in range(rows):
        result[:, i] = A[i, :]
    
    return result
