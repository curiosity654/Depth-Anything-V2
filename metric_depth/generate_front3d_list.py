import json
import os
import glob
from tqdm import tqdm

info_path = '/mnt/data/users/yuchen.wu/code/OmniOcc/OmniScene/datasets/front3d/meta/val_3d.json'
img_path = '/mnt/data/users/yuchen.wu/code/OmniOcc/OmniScene/datasets/front3d/data'

with open(info_path, 'r') as f:
    infos = json.load(f)

filelist = []

for info in tqdm(infos):
    scene_id, image_id = info["scene_id"], info["image_id"]
    filename = os.path.join(img_path, scene_id, f'rgb_{image_id}.png')
    depthname = os.path.join(img_path, scene_id, f'depth_{image_id}.exr')
    filelist.append([filename, depthname])

with open("dataset/splits/front3d/val.txt", "w") as file:
    for item in filelist:
        file.write(f"{item[0]} {item[1]}\n")