print("aufteilung startet")

import os
import shutil
import random

# Pfad zur Quelle (relativ vom Skript aus)
source_folder = 'data/traffic_lights_all_jpg'

# Pfad zum Ziel (relativ vom Skript aus)
target_folder = 'data/traffic_lights'

for split in ['train', 'val', 'test']:
    for cls in ['green', 'yellow', 'white']:
        os.makedirs(os.path.join(target_folder, split, cls), exist_ok=True)

train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

for cls in ['white']:
    cls_path = os.path.join(source_folder, cls)
    cls_files = os.listdir(cls_path)
    random.shuffle(cls_files)
    total = len(cls_files)
    train_end = int(total * train_ratio)
    val_end = train_end + int(total * val_ratio)

    for i, file in enumerate(cls_files):
        if i < train_end:
            split = 'train'
        elif i < val_end:
            split = 'val'
        else:
            split = 'test'

        src_path = os.path.join(cls_path, file)
        dst_path = os.path.join(target_folder, split, cls, file)
        shutil.copy2(src_path, dst_path)
        print(f'Copied {file} to {split}/{cls}')


print("aufteilung vorbei")