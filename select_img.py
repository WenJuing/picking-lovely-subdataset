import os
import shutil

# 定义源文件路径和目标文件夹路径
source_dir = 'E:/OIQ-10k/ref/'
selected_dir = 'E:/OIQ-10k/selected_ref/'
discard_dir = 'E:/OIQ-10k/discard_ref/'

# 创建目标文件夹
if not os.path.exists(selected_dir):
    os.makedirs(selected_dir)
if not os.path.exists(discard_dir):
    os.makedirs(discard_dir)
    
# 读取文件内容并处理每一行
with open('select_idx.txt', 'r') as f:
    for line in f:
        filename, is_selected = line.strip().split(',')
        src = os.path.join(source_dir, filename)
        if is_selected == 'True':
            # 复制选中的图片到目标文件夹
            dst = os.path.join(selected_dir, filename)
        else:
            dst = os.path.join(discard_dir, filename)
        shutil.copy2(src, dst)
        print(f"{filename} has moved.")