def disambiguation_camera_pose(camera_confs, points):
    """
    args:
    -   camera_confs: [(c1, r1), (c2, r2), (c3, r3), (c4, r4)]
    -   points: [p1, p2, ... pn] (pi: np.array of shape (3))
    return: 
    -   exact (ci, ri) which satisfies cheirality condition
    """
    max = -1
    argmax = -1
    for i in range(4):
        ci, ri = camera_confs[i]
        counter = 0
        for pi in points:
            pih = pi.reshape(1, 3)
            cih = ci.reshpae(1, 3)
            counter += 1 if ri[2] @ (pih - cih) > 0 else 0
        
        if counter > max: 
            max = counter
            argmax = i
    
    return camera_confs[argmax]
    
    
    
