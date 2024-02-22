import numpy as np

def EssentialMatrixFromFundamentalMatrix(F, K):
    E = K.T @ F @ K
    U, S, Vh = np.linalg.svd(E)
    D = np.diag([1, 1, 0])
    E_new = U @ D @ Vh
    return E_new
