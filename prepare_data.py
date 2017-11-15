from __future__ import print_function
import os
from os import listdir
from os.path import join, isfile, isdir
from shutil import copyfile, rmtree
from PIL import Image

RAW_PATH = './Face'
DATA_PATH = './data'
TRAIN = 'Train'
TEST = 'Test'
IMAGE_SIZE = 28, 28


def move_and_rename(path_type):
    if not path_type:
        return
    print("Moving %s data" % path_type)
    IN_PATH = join(RAW_PATH, path_type)
    OUT_PATH = join(DATA_PATH, path_type)
    if isdir(OUT_PATH):
        rmtree(OUT_PATH)
    os.mkdir(OUT_PATH)

    name_all = [name for name in listdir(IN_PATH) if '.' not in name]
    for people_name in name_all:
        people_path = join(IN_PATH, people_name)
        people_images = []

        images_folders = [
            folder for folder in listdir(people_path)
            if '.' not in folder
        ]
        for images_folder in images_folders:
            images_path = join(people_path, images_folder)
            images = [
                join(images_path, img) for img in listdir(images_path)
                if img.endswith('.jpg')
            ]
            people_images.extend(images)
        for i, img in enumerate(people_images):
            new_name = "{0}_{1:04}.jpg".format(people_name, i)
            dst = join(OUT_PATH, new_name)
            copyfile(img, dst)
    print("Moving %s data done" % path_type)


def resize(path_type):
    print("Resizing %s data" % path_type)
    images_path = join(DATA_PATH, path_type)
    out_path = join(DATA_PATH, path_type + "_resized")
    if isdir(out_path):
        rmtree(out_path)
    os.mkdir(out_path)
    images_name = [
        image_name for image_name in listdir(images_path)
        if image_name.endswith('.jpg')
    ]
    for image_name in images_name:
        try:
            img = Image.open(join(images_path, image_name))
            img = img.convert('L')
            img = img.resize(IMAGE_SIZE)
            img.save(join(out_path, image_name))
        except:
            pass
    print("Resizing %s data done" % path_type)

if __name__ == '__main__':
    # move_and_rename(TRAIN)
    # move_and_rename(TEST)
    resize(TRAIN)
    resize(TEST)
