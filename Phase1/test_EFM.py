import numpy as np
from EstimateFundamentalMatrix import estimate_fundamental 


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
    fund = estimate_fundamental(proj_xy, proj_yz)
    print(f"fundamental matrix = {fund}")
    print(f"rank = {np.linalg.matrix_rank(fund)}")
    for i in range(point_num):
        print(f"x{i} * F * x{i}^T = {proj_xy[i] @ fund @ proj_yz[i]}")



def main():
    test_code()


if __name__ == "__main__":
    main()
