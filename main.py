""" This program converts your non-even profile images to a cropped frontal profile image. 
    This program uses Tensorflow framework to work (because of MTCNN network) and OpenCV, 
    so you should install them before starting to use it. 
    Please provide path of your images which aimed to profile it, and let the program does the rest! """

import os
import sys
import cv2
import math
import ntpath
import argparse
import numpy as np
from mtcnn import MTCNN
from scipy import ndimage
from util import get_coordinates, crop_image


def main(args):
    input_path = args.image_path
    dir_path, file_name = ntpath.split(input_path)
    original_image = cv2.imread(input_path)
    height, width, depth = original_image.shape
    detector = MTCNN()
    landmarks = detector.detect_faces(original_image)
    old_landmark = landmarks[0] # you have just one face in your profile, otherwise you pick the image with most confident
    _, _, nose, theta = get_coordinates(old_landmark)
    rotated_image = ndimage.rotate(original_image, theta + 180.0)
    new_height, new_width, _ = rotated_image.shape
    delta_width = abs(new_width - width) // 2
    delta_height = abs(new_height - height) // 2
    cropped_image = crop_image(delta_width, new_width - delta_width, delta_height, new_height - delta_height, rotated_image)
    cv2.imwrite(os.path.join(dir_path, 'rotated_' + file_name), cropped_image)

    # new_landmarks = detector.detect_faces(rotated_image)
    # new_landmark = new_landmarks[0] # you have just one face in your profile, otherwise it picks up a face with the most confident
    # _, _, nose_new, theta_new = get_coordinates(new_landmark)
    # masked_image = mask_image(width, height, nose_new)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='program parameters')
    parser.add_argument('image_path', metavar='path', type=str, help='the path to target image')
    args = parser.parse_args()
    main(args)