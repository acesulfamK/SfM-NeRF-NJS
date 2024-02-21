import typing
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ortho_group
import os

def generate_uniform_sphere(num_points: np.ndarray) -> np.ndarray:
    """
    return: np.ndarray of shape (3, n)
    """
    phi = np.random.uniform(0, 2*np.pi, num_points)
    costheta = np.random.uniform(-1, 1, num_points)
    u = np.random.uniform(0, 1, num_points)
    theta = np.arccos(costheta)
    r = u ** (1/3)
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    ret_mat = np.array([x, y, z])
    return ret_mat


def show_points(points_mat):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    xs = points_mat[0]
    ys = points_mat[1]
    zs = points_mat[2]
    ax.scatter(xs, ys, zs, marker = 'o')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    cur_path = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(cur_path, "general_points.png")
    print(f"save_path = {save_path}")
    plt.savefig(save_path)

def show_screen(points_mat):
    plt.figure()
    plt.scatter(points_mat[0], points_mat[1])
    cur_path = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(cur_path, "screen_points.png")
    print(f"screen save path = {save_path}")
    plt.savefig(save_path)

def screen_points(
        points_mat: np.ndarray, ortho: np.ndarray, t:np.ndarray
        ) -> np.ndarray:
    """
    args:
        points_mat of shape (3, n): general coordinates of points
        ortho of shape (3, 3): real orthogonal matrix
        t (1, 3): translation
    return:
        shape (n, 3): coordinates on screen. z=1 in all points
    """
    def proj_screen(mat):
        mat_scr = np.zeros_like(mat)
        mat_scr[0 ,:] = mat[0 ,:]/mat[2 ,:]
        mat_scr[1 ,:] = mat[1 ,:]/mat[2 ,:]
        mat_scr[2 ,:] = np.ones_like(mat_scr[2 ,:])
        return mat_scr
        
    assert t[2, 0] < -1, "The value of t is wrong."
    after_liner = ortho.T @ points_mat - t
    mat_scr = proj_screen(after_liner)
    return mat_scr

def spiral_corn():
    u = np.linspace(0, 1, 200)
    theta = u * 8 * np.pi
    z = u
    r = 2 * u
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    mat = np.array((x, y, z))
    return mat

def generate_spiral_corn():
    points_mat = spiral_corn()
    t1 = np.array([-1, 0, -5])
    t1 = t1.reshape((1, 3)).T
    t2 = np.array([0, 1, -7])
    t2 = t2.reshape((1, 3)).T

    theta = -(1/4)*np.pi
    ortho1= np.array([
        [np.cos(theta), 0, -np.sin(theta)],
        [0, 1, 0],
        [np.sin(theta), 0,np.cos(theta)],
        ])

    phi= -(1/4)*np.pi
    ortho2 = np.array([
        [1, 0, 0],
        [0, np.cos(phi), -np.sin(phi)],
        [0, np.sin(phi),np.cos(phi)],
    ])
    ortho = ortho1 @ ortho2
    mat_scr1 = screen_points(points_mat, ortho, t1)
    mat_scr2 = screen_points(points_mat, np.eye(3), t2)
    return mat_scr1, mat_scr2


