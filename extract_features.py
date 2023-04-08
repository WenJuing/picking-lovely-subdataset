import os
import torch
from torchvision import models as models
from torchvision import transforms
from PIL import Image
import numpy as np
import torch.nn as nn
from tqdm import tqdm


path = "E:/OIQ-10k/viewports/"
img_name_list = os.listdir(path)
img_name_list = sorted(img_name_list, key=lambda x: int(''.join(filter(str.isdigit, x))))   # 按数字升序排序
f = open("./feature.txt", "w")

transform = transforms.ToTensor()
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT).cuda()
remove_head = nn.Sequential()
model.fc = remove_head

model.eval()
# 分别对每张图片的多个视口进行特征提取
for img_name in tqdm(img_name_list):
    vp_list = []
    vp_name_list = os.listdir(os.path.join(path, img_name))
    for vp_name in vp_name_list:
        vp = Image.open(os.path.join(path, img_name, vp_name))
        vp = transform(vp).unsqueeze(0)
        vp_list.append(vp)
        vp_batch = torch.cat(vp_list, dim=0)        # [8, 3, 512, 512]
        vp_feature = model(vp_batch.cuda())         # [8, 512]
        vp_feature = torch.mean(vp_feature, dim=0)  # [512]
    # 将特征保存到 txt 文件
    for i in range(vp_feature.size()[0]):
        if i == 0: f.write(img_name + ',')
        if i != vp_feature.size()[0] - 1:
            f.write(str(np.round(vp_feature[i].item(), 5)) + ',')
        else:
            f.write(str(np.round(vp_feature[i].item(), 5)))
    f.write("\n")
f.close()