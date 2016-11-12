from os import listdir
from os.path import isfile, join
import imutils
import os
import cv2
import util


def create_info():
    path = "train"
    pos_str = ''
    neg_str = ''
    pos_count = 0
    neg_count = 0
    for r in listdir(path):
        file_path = join(path, r)
        if r.index('.pgm') != -1:
            img = cv2.imread(file_path)
            height = img.shape[0]
            width = img.shape[1]
            abs_path = os.path.abspath(file_path)
            print abs_path
            if r.startswith("pos"):
                item_str = '' + str(file_path) + ' 1 0 0 ' + str(width) + ' ' + str(height) + ' \n'
                pos_str += item_str
                pos_count += 1
            elif r.startswith("neg"):
                item_str = '' + str(file_path) + '\n'
                neg_str += item_str
                neg_count += 1
    pos_str = pos_str[:-1]
    neg_str = neg_str[:-1]
    print pos_count
    print neg_count
    util.write_to_file('car_pos.info', pos_str)
    util.write_to_file('car_neg.info', neg_str)


# create vec file: opencv_createsamples -info car_pos.info -num 550 -w 100 -h 40 -vec cars_pos.vec
# check vec file: opencv_createsamples -w 100 -h 40 -vec cars_pos.vec
# train cascade: opencv_traincascade -data data -vec cars_pos.vec -bg car_neg.info -numPos 550 -numNeg 500 -numStages 2 -w 100 -h 40 -featureType LBP

create_info()
