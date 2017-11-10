from __future__ import print_function
import os
from os import listdir
from os.path import isfile, join
import numpy as np
from imageio import imread
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

DATA_PATH = './data'


def read_data(path_type):
    if not path_type:
        return
    data_path = join(DATA_PATH, path_type + "_resized")
    images_path = [
        join(data_path, f) for f in listdir(data_path)
        if isfile(join(data_path, f)) and 'jpg' in f
    ]
    images, labels = [], []
    for image_path in images_path:
        image = imread(image_path)
        image = image.reshape(32*32)
        image = [i/255. for i in image]
        image_label = image_path.split('/')[-1].split('_')[0]
        images.append(image)
        labels.append(image_label)
    return np.array(images), np.array(labels)


def main():
    train_images, train_labels = read_data('Train')
    test_images, test_labels = read_data('Test')
    clf = SVC(kernel='poly', C=1e5)
    clf.fit(train_images, train_labels)
    pred_labels = clf.predict(test_images)
    print(accuracy_score(test_labels, pred_labels))


if __name__ == '__main__':
    main()
