import numpy as np
from typing import Any, TypeVar, List


# 課題の意向に沿うため、Fundamental matrixを求める点においてはnumpy.linalg.svdを用いなかった。
def linear_least_square(A: np.ndarray) -> np.ndarray:
    square_mat = A.T @ A
    e_val, e_vec= np.linalg.eig(square_mat)
    min_arg = np.argmin(e_val)
    return e_vec[:, min_arg]


def estimate_fundamental(y1: np.ndarray, y2: np.ndarray) -> np.ndarray:
    """
    y1: List[np.array of shape (3, n)]
    y2: List[np.array of shape (3, n)]
    return: np.array (3 x 3)
    """
    n = y1.shape[1]
    prod = np.einsum('ji,ki->ijk',y1,y2)
    result = prod.reshape(n, 9)
    fund_flat = linear_least_square(result)
    fund = fund_flat.reshape(3, 3)
    # make fund rank 2
    U, S, Vt = np.linalg.svd(fund)
    S[2] = 0 # Rank S should be 2 to make Ker S of dim 1
    fund_rank2 = U @ np.diag(S) @ Vt
    return fund_rank2

