from __future__ import print_function
import os
from os import listdir
from os.path import isfile, join
import cv2
import sys
import numpy as np
import cifar10

DATA_PATH = "./data"
LABELS = [
    'nguyennt3', 'hieubq', 'trangdnt', 'diepdt2', 'tiennd', 'phuongnt3',
    'nhanlt3', 'dathv', 'thanhnt', 'tuannm4', 'anhpt4', 'ChiHoaLaoCong',
    'anhnp2', 'anhnh2', 'thanhpv2', 'truongtd4', 'huyencm', 'thanhlc',
    'hadn', 'hieuvm', 'thaontp2', 'thaonp2', 'chaudtb', 'thuybt', 'nhungvth',
    'vinhnd2', 'anhpq']


def convert(path_type):
    if not path_type:
        return
    output_file = open(
        'data/cifar10_data/cifar-10-batches-bin/{0}_batch.bin'
        .format(path_type.lower()), 'ab')
    data_path = "./data/{0}_resized".format(path_type)
    images_path = [
        join(data_path, f) for f in listdir(data_path)
        if isfile(join(data_path, f)) and 'jpg' in f
    ]

    for image_path in images_path:
        im = cv2.imread(image_path)
        r = im[:, :, 0].flatten()
        g = im[:, :, 1].flatten()
        b = im[:, :, 2].flatten()
        label = LABELS.index(image_path.split('/')[-1].split('_')[0])
        output = np.array([label] + list(r) + list(g) + list(b), dtype=np.uint8)
        output.tofile(output_file)
    output_file.close()

if __name__ == '__main__':
    convert('Train')
    convert('Test')
