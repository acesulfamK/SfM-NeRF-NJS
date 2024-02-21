import numpy as np
import random
<<<<<<< HEAD
from scipy.stats import ortho_group
import matplotlib.pyplot as plt
from EstimateFundamentalMatrix import estimate_fundamental
from utils.GenerateScreenPoints import generate_spiral_corn
=======
from EstimateFundamentalMatrix import estimate_fundamental
from scipy.stats import ortho_group
>>>>>>> cad0cfa9ac766d70bb63c2ae6670c0ba78c610f8

def generate_points(p_num):
    """
    3次元空間上のp_num個の点をxy, yz座標に射映したものを返す
    return: 
        proj_xy (np.array of shape p_num x 3):
        proj_yz (np.array of shape p_num x 3):
    """
    points = np.random.rand(p_num, 3)  # 8x3行列、各行が一つの点を表す
    s = np.ones((p_num, 1))
    proj_xy = points[:, :2]  # X, Y座標を取得
    proj_xy = np.concatenate((proj_xy, s), axis=1)
    proj_yz = points[:, 1:]  # Y, Z座標を取得
    proj_yz = np.concatenate((proj_yz, s), axis=1)
    return proj_xy, proj_yz 

def generate_points_ortho(p_num):
    """
    3次元空間上のp_num個の点を射映したものを返す
    return: 
        proj1 (np.array of shape p_num x 3):
        proj2 (np.array of shape p_num x 3):
    """
    base_points = np.random.rand(p_num, 3)  # 8x3行列、各行が一つの点を表す
    o_mat1 = ortho_group.rvs(dim=3)
    o_mat2 = ortho_group.rvs(dim=3)
    s = np.ones((p_num, 1))
    proj1 = o_mat1 @ base_points
    proj1 = np.concatenate((proj1[:, :2], s), axis=1)
    proj2 = o_mat2 @ base_points
    proj2 = np.concatenate((proj2[:, :2], s), axis=1)
    return proj1, proj2

def ransac(proj_xy, proj_yz, repeat_num, max_point_num=8, eps=0.001):
    """
    args:
        proj_xy: np.array of shape (3, n)
            - each columns should be [x, y, 1]
        proj_yz: np.array of shape (3, n)
            - each columns should be [x, y, 1]
        repeat_num: int
        max_point_num: int
            - max point num to calculate fundamental matrix
        eps: float
            - (x,y)s such as xt*F*y < eps are proper tuples of screen points.
    """
    prov_max_good = 0
    assert proj_xy.shape[1] == proj_yz.shape[1], "The numbers of points of 2 screeens are not same!" 
    n = proj_xy.shape[1]
    for i in range(repeat_num):
        random_numbers = random.sample(range(n), min(max_point_num, n))
        ext_proj_xy = proj_xy[:, random_numbers]
        ext_proj_yz = proj_yz[:, random_numbers]
        fund = estimate_fundamental(ext_proj_xy, ext_proj_yz)
        good_indices = []
        for i in range(n):
            if abs(proj_xy[:, i].T @ fund @ proj_yz[:, i]) < eps:
                good_indices.append(i)
        if prov_max_good < len(good_indices):
            prov_max_good = len(good_indices)
            prov_good = good_indices
    return prov_good


def test():
<<<<<<< HEAD
    def test_case():
        """
        220 samples = noise 20 + spiral 200
        """
        random_num = 20
        p1 = np.random.uniform(-0.4, 0.4, (2, random_num))
        p1 = np.concatenate((p1, np.ones((1, random_num))))
        p2 = np.random.uniform(-0.4, 0.4, (2, random_num))
        p2 = np.concatenate((p2, np.ones((1, random_num))))
        s1, s2 = generate_spiral_corn()
        scr1 = np.concatenate((s1, p1), axis=1)
        scr2 = np.concatenate((s2, p2), axis=1)
        return scr1, scr2
    scr1, scr2 = test_case()
    prov_good_indices = ransac(scr1, scr2, 10, 8, 0.01)
    print(f"Good indices are {prov_good_indices}")
=======
    proj_xy, proj_yz = generate_points(10)
    proj_xy = np.concatenate((proj_xy, np.array([[1,2,1]])), axis = 0)
    proj_yz = np.concatenate((proj_yz, np.array([[10,4,1]])), axis = 0)
    proj_xy = np.concatenate((proj_xy, np.array([[2,2,1]])), axis = 0)
    proj_yz = np.concatenate((proj_yz, np.array([[1,5,1]])), axis = 0)
    prov_good = ransac(proj_xy, proj_yz, 10, 8, 0.001)
    print(f"Prov good = {prov_good}")
>>>>>>> cad0cfa9ac766d70bb63c2ae6670c0ba78c610f8


if __name__ == "__main__":
    test()
