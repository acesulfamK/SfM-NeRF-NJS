import numpy as np

def extract_camera_pose(E):
    U, s, Vh = np.linalg.svd(E)
    W = np.array([[0, -1, 0],
                  [1, 0, 0],
                  [0, 0, 1]])
    c1 = U[:, 2]; r1 = U @ W @ Vh.T
    c2 = -U[:, 2]; r2 = U @ W @ Vh.T
    c3 = U[:, 2]; r3 = U @ W.T @ Vh.T
    c4 = -U[:, 2]; r4 = U @ W.T @ Vh.T
    return (c1, r1), (c2, r2), (c3, r3), (c4, r4)

if __name__ == "__main__":
    A = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    ans = extract_camera_pose(A)
    print(ans)

