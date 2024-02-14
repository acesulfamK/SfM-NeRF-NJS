import numpy as np
from typing import Any, TypeVar


def linear_least_square(A: np.ndarray):
    square_mat = A.T * A
    e_val, e_vec= np.linalg.eig(square_mat)
    min_arg = np.argmin(e_val)
    return e_vec[min_arg]



def main():
    A = np.random.rand(8, 9)
    min_vec = linear_least_square(A)
    import pdb; pdb.set_trace()

if __name__ == "__main___":
    main()
