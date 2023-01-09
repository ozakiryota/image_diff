import numpy as np


def getDiffImage(img_0_np, img_1_np, max_value=255):
    img_0_np = 255 / max_value * img_0_np
    img_1_np = 255 / max_value * img_1_np
    diff_img_np = np.abs(img_0_np.astype(int) - img_1_np.astype(int))
    diff_img_np = diff_img_np[:, :, 0] + diff_img_np[:, :, 1] + diff_img_np[:, :, 2]
    return diff_img_np