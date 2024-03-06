import numpy as np


def skew(x):
    """
    args: x (np.array of shape (3)) 
    return: skew symmetric matrix
    """
    return np.array(
        [
            [0, -x[2], x[1]],
            [x[2], 0, -x[0]],
            [-x[1], x[0], 0]
        ])

def LinearTrianglation(screen_pair_point, rcs, K):
    """
    args: 
        screen_pair_point (tuple of np.array of shape (2)): (x1, x2)
        rcs (2 elements tuple of tuple of np.array of shape (3), (3, 3)):
            ((C1, R1), (C2, R2))
        K: intrinsic matrix
    return: 
        np.array of shape (3)
    """

    x1, x2 = screen_pair_point
    x1 = np.hstack((x1, 1))
    x2 = np.hstack((x2, 1))
    (c1, r1), (c2, r2) = rcs
    I = np.eye(3)
    p1 = K @ r1 @ np.hstack((I, -c1.reshape(3, 1)))
    p2 = K @ r2 @ np.hstack((I, -c2.reshape(3, 1)))
    x1_skew = skew(x1)
    x2_skew = skew(x2)
    A = [[x1_skew @ p1], [x2_skew @ p2]]
    A = np.array(A).reshape((-1, 4))
    _, _, V = np.linalg.svd(A)
    v = V[-1, :]
    v /= v[-1]
    return v

def test1():
    x1 = np.array((0, 0))
    x2 = np.array((0, 0))

    c1 = np.array((0, 0, 0))
    r1 = np.array([
        [0.705, 0, 0.705],
        [0, 1, 0],
        [-0.705, 0, 0.705]
    ])

    c2 = np.array((1, 0, 0))
    r2 = np.array([
        [0.705, 0, -0.705],
        [0, 1, 0],
        [0.705, 0, 0.705]
    ])
    
    K = np.eye(3)
    
    return ((x1, x2), ((c1, r1.T), (c2, r2.T)), K), np.array((0.5, 0, 0.5))
if __name__ == "__main__":
    (pair_points, rcs, K), ans = test1()
    print(f"estimation = {LinearTrianglation(pair_points, rcs, K)}")
    print(f"true ans = {ans}")
