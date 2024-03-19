import glob
import os
import shutil
from math import floor

from tqdm import tqdm

input_folders = [
    "flower_photos/daisy",
    "flower_photos/roses",
    "flower_photos/sunflowers",
    "flower_photos/dandelion"
]

out_train = "D:/PyTorch/prepared/train/"
out_val = "D:/PyTorch/prepared/test/"

ratio = [80, 20]
exception = ["classes"]


def split_data(input_folders, out_train, out_val, ratio, exception):
    for folder in input_folders:
        files = glob.glob(os.path.join(folder, '*'))
        files = [file for file in files if not any(exc in file for exc in exception)]

        num_files = len(files)
        num_train = floor(num_files * ratio[0] / 100)
        num_val = num_files - num_train

        train_files = files[:num_train]
        val_files = files[num_train:]

        for file in tqdm(train_files, desc=f"Copying {folder} to train"):
            shutil.copy(file, os.path.join(out_train, os.path.basename(folder)))

        for file in tqdm(val_files, desc=f"Copying {folder} to test"):
            shutil.copy(file, os.path.join(out_val, os.path.basename(folder)))


split_data(input_folders, out_train, out_val, ratio, exception)