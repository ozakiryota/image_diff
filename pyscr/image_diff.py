import numpy as np

import torch
from torchvision import models


class ImageDiff:
    def __init__(self, use_feature=True):
        if use_feature:
            self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
            self.model = models.vgg16(weights=models.VGG16_Weights.IMAGENET1K_V1).features.to(self.device)
            print(self.model)

    def getDiffImage(self, img_0_np, img_1_np, max_value=255):
        img_0_np = 255 / max_value * img_0_np
        img_1_np = 255 / max_value * img_1_np
        diff_img_np = np.abs(img_0_np.astype(int) - img_1_np.astype(int))
        diff_img_np = diff_img_np[:, :, 0] + diff_img_np[:, :, 1] + diff_img_np[:, :, 2]
        return diff_img_np


    def getDiffFeature(self, img_0_np, img_1_np):
        img_0_np = img_0_np.transpose(2, 0, 1).astype(np.float32)
        img_1_np = img_1_np.transpose(2, 0, 1).astype(np.float32)
        with torch.set_grad_enabled(False):
            img_0_tensor = torch.from_numpy(img_0_np).clone().to(self.device)
            img_1_tensor = torch.from_numpy(img_1_np).clone().to(self.device)
            img_0_tensor = self.model(img_0_tensor)
            img_1_tensor = self.model(img_1_tensor)
            diff_img = torch.abs(img_0_tensor - img_1_tensor)
        diff_img = diff_img.cpu().detach().numpy().transpose((1, 2, 0)).mean(axis=2)
        return diff_img