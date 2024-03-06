import os
import numpy as np
import argparse



DEFAULT_MATCHES_FOLDER = 'Data/P3Data'
DEFAULT_CALIBRATION_FILEPATH = 'Data/P3Data/calibration.txt'


def parse_matching_file(file_num: int, folder_path = DEFAULT_MATCHES_FOLDER):
    """
    args: 
        file_num
        folder_path
    returns:
        "file_num concatenated with im_id":
            (
                [(u1 file_num image, v1 file_num image), (u2 file_num image, v2 file_num image) ... ],
                [(u1 file_num image, v1 file_num image), (u2 file_num image, v2 file_num image) ... ]
            )
        
    """
    file_path = os.path.join(os.getcwd(), folder_path, f"matching{file_num}.txt")
    correspondences = []
    with open(file_path, 'r') as f:
        correspondences = f.readlines()
    correspondences = [l.split() for l in correspondences[1:]]
    
    matches_dict = {}
    for x in correspondences:
        correspondences = x[1:6]
        u_file = float(x[4])
        v_file = float(x[5])
        for i in range(int(x[0]) - 1):
            im_id = x[6 + 3*i]
            u = float(x[6 + 3*i + 1])
            v = float(x[6 + 3*i + 2])
            r_key = str(file_num) + im_id
            if r_key not in matches_dict.keys():
                matches_dict[r_key] = ([], [])
            matches_dict[r_key][0].append((u_file, v_file))
            matches_dict[r_key][1].append((u,v))
    return matches_dict

def K_matrix(calib_file_path=DEFAULT_CALIBRATION_FILEPATH):
    file_path = os.path.join(os.getcwd(), calib_file_path)
    array = np.loadtxt(file_path, dtype=float)
    return array

if __name__ == "__main__":
    print(parse_matching_file(1))
    print(K_matrix())
    

