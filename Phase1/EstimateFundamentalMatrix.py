import numpy as np
from typing import Any, TypeVar, List


# 課題の意向に沿うため、Fundamental matrixを求める点においてはnumpy.linalg.svdを用いなかった。
def linear_least_square(A: np.ndarray) -> np.ndarray:
    square_mat = A.T @ A
    e_val, e_vec= np.linalg.eig(square_mat)
    min_arg = np.argmin(e_val)
    return e_vec[:, min_arg]


def solve_fundamental(y1: np.ndarray, y2: np.ndarray) -> np.ndarray:
    """
    y1: List[ array(n x 3)]
    y2: List[ array(n x 3)]
    return: np.array (3 x 3)
    """
    n = y1.shape[0]
    prod = np.einsum('ij,ik->ijk',y1,y2)
    result = prod.reshape(n, -1)
    fund_flat = linear_least_square(result)
    fund = fund_flat.reshape(3, 3)
    # make fund rank 2
    U, S, Vt = np.linalg.svd(fund)
    S[2] = 0
    fund_rank2 = U @ np.diag(S) @ Vt
    return fund_rank2


def project_points(p_num):
    points = np.random.rand(p_num, 3)  # 8x3行列、各行が一つの点を表す
    s = np.ones((p_num, 1))
    proj_xy = points[:, :2]  # X, Y座標を取得
    proj_xy = np.concatenate((proj_xy, s), axis=1)
    proj_yz = points[:, 1:]  # Y, Z座標を取得
    proj_yz = np.concatenate((proj_yz, s), axis=1)
    return proj_xy, proj_yz 

def test_code():
    point_num = 8
    proj_xy, proj_yz = project_points(point_num)
    proj_xy = np.array(range(point_num * 3)).reshape(point_num, 3)
    proj_yz = np.array(range(point_num * 3)).reshape(point_num, 3)
    fund = solve_fundamental(proj_xy, proj_yz)
    print(f"fundamental matrix = {fund}")
    print(f"rank = {np.linalg.matrix_rank(fund)}")
    for i in range(point_num):
        print(f"x{i} * F * x{i}^T = {proj_xy[i] @ fund @ proj_yz[i]}")


def main():
    test_code()


if __name__ == "__main__":
    main()
