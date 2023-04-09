import os
import numpy as np
import pandas as pd
from tqdm import tqdm


img_path = "E:/OIQ-10k/ref/"
data = np.array(pd.read_csv("./feature.txt", header=None))
name_list, data = np.array(data)[:, 0], np.array(data)[:, 1:].astype(float)
print("original shape:", data.shape)
# 使用unique函数删除重复项
unique_data, unique_idx = np.unique(data, axis=0, return_index=True)
duplicate_idx = np.setdiff1d(np.arange(data.shape[0]), unique_idx)
# unique_idx 的顺序是乱的，重新进行排序
idx = np.argsort(unique_idx)
unique_idx = unique_idx[idx]
unique_data = unique_data[idx]

print("new shape:", unique_data.shape)
print("delete same image...")
if duplicate_idx is None:
    print("not same image.")
else:
    for i in tqdm(range(len(duplicate_idx))):
        os.remove(os.path.join(img_path, name_list[duplicate_idx[i]]))

print("save new feature to unique_feature.txt...")
f = open("unique_feature.txt", "w")
for idx in unique_idx:
    # 将特征保存到 txt 文件
    for i in range(unique_data.shape[1]):
        if i == 0: f.write(name_list[idx] + ',')
        if i != unique_data.shape[1] - 1:
            f.write(str(data[idx, i].item()) + ',')
        else:
            f.write(str(data[idx, i].item()))
    f.write("\n")
f.close()
print("All the work has been done!")

